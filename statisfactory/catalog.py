#! /usr/bin/python3

# main.py
#
# Project name: Caisse Dépôts et Placements du Québec.
# Author: Hugo Juhel
#
# description:
"""
    Implements the single entry point to the datasources
"""

#############################################################################
#                                 Packages                                  #
#############################################################################

# system
from pathlib import Path

# project
from .logger import MixinLogable
from .errors import errors
from .models import CatalogData, Artefact, Connector
from .artefact_interactor import (
    CSVInteractor,
    ODBCInteractor,
    XLSXInteractor,
    ArtefactInteractor,
)

# third party
from filelock import FileLock
import pandas as pd

#############################################################################
#                                  Script                                   #
#############################################################################


class Catalog(MixinLogable):
    """Catalog represent a loadable / savabale set of dataframes living locally or in far, far aways distributed system.
    The catalog mixes a monitor with a facade pattern (yeup, quick dev)

    TODO : test a replication flow with a context
    TODO : Add context injection from pipeline
    """

    # Map each artefact type to it's corresponding interactor
    interactorMapper = {
        "odbc": ODBCInteractor,
        "csv": CSVInteractor,
        "xslx": XLSXInteractor,
    }

    def __init__(self, path: str, context=None):
        """Build a new catalog for the root 'path'.

        The catalog loads:
            * a "catalog.yaml" file
        """

        super().__init__()
        self.debug("preflight : check...")

        self._context = context

        # Check that the path exists
        path = Path(path)
        if not path.exists():
            raise errors.E010(
                __name__, path=path
            )  # moups, pas d'erreur dans un init ;)

        # If so, lock the folder
        lock_path = FileLock(path.joinpath("statisfactory.lock"))
        with lock_path:

            # Check that a data folder exists
            data_path = path.joinpath("Data")
            if not data_path.exists() or not data_path.is_dir:
                raise errors.E011

            # Check that the catalog.yaml file exits
            catalog_path = path.joinpath("catalog.yaml")
            if not catalog_path.exists():
                raise errors.E012

            # load it
            try:
                self._data = CatalogData.from_file(catalog_path)
            except BaseException as err:
                raise errors.E013 from err

        self.debug("preflight : ...ok")

    def _get_connector(self, artefact: Artefact) -> Connector:
        """
        Retrieve the connector of an Artefact

        Args:
            artefact (Artefact): the artefact to extract the connector for
        """

        name = artefact.connector
        conn = None
        if name:

            for key, connector in self._data.connectors:
                if key == name:
                    break
            else:
                raise errors.E032.format(name=name)

            conn = connector

        return conn

    def _get_artefact(self, name: str) -> Artefact:
        """
        Retrieve the FIRST artefact matching the given name currently living in the catalog.
        """

        try:
            artefact = self._data.artefacts[name]
        except KeyError:
            raise errors.E030.format(name=name)

        return artefact

    def _get_interactor(self, artefact: Artefact) -> ArtefactInteractor:
        """
        Retrieve the interactor matchin the type of the artefact.
        """

        try:
            interactor = Catalog.interactorMapper[artefact.type]
        except KeyError:
            raise errors.E031.format(name=artefact.type)

        return interactor

    def load(self, name: str) -> pd.DataFrame:
        """Load an asset from the catalogue

        Args:
            name (str): the name of the artefact to load.

        TODO : Add context injection from pipeline
        """

        artefact = self._get_artefact(name)
        connector = self._get_connector(artefact)
        # BUILD A GET CONTEXT METHOD

        # INJECT A CONTEXT DATACLASS WITH THE CURRENT PATH
        interactor = self._get_interactor(artefact)(artefact, connector=connector)

        return interactor.load()

    def save(self, name, asset):
        """Save an asset using the path from the catalogue

        Args:
            name ([type]): [description]
            asset ([type]): [description]

        Raises:
            BaseException: [description]
        """

        pass


#############################################################################
#                                   main                                    #
#############################################################################

if __name__ == "__main__":
    # (*cough*cough) Smoke-test
    raise BaseException("catalog.py can't run in standalone")
