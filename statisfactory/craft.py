#! /usr/bin/python3

# main.py
#
# Project name: statisfactory
# Author: Hugo Juhel
#
# description:
"""
    implements a wrapper to handler assets loading / saving for an arbitrary function.
"""

#############################################################################
#                                 Packages                                  #
#############################################################################

# system
from functools import update_wrapper
from typing import Callable, Dict
from inspect import signature
from collections.abc import Mapping

# project
from .errors import errors
from .logger import MixinLogable
from .catalog import Catalog
from .models import Artefact

#############################################################################
#                                  Script                                   #
#############################################################################


class Craft(MixinLogable):
    """
    Craft wraps a task and take care of data retrieval from / data storage to the catalogue
    """

    _valids_annotations = ["<class 'statisfactory.models.Artefact'>"]

    @staticmethod
    def make(catalog: Catalog):
        """
        Decorator transfroming a callable into a Craft

        Args:
            catalog (Catalog): the catalog to bind the craft to.
        """

        def _(func: Callable):

            return Craft(catalog, func)

        return _

    def __init__(self, catalog: Catalog, callable: Callable):
        """
        Wrap a callable in a craft binded to the given catalog.
        """

        super().__init__()
        self._catalog = catalog
        self._callable = callable
        self._name = callable.__name__
        update_wrapper(self, callable)

    def __call__(self, *args, **kwargs):
        """
        Call the underlying callable
        """

        artefacts = self._get_artefacts(self._callable)

        try:
            out = self._callable(*args, **kwargs, **artefacts)
        except TypeError as err:
            raise errors.E046(__name__, name=self._name) from err
        except BaseException as err:
            raise errors.E040(__name__, func=self._name) from err

        out = self._capture_artefacts(out)

        return out

    @property
    def name(self) -> str:
        """
        Get the name of the craft
        """

        return self._name

    @property
    def catalog(self):
        """
        Catalog getter
        """
        if not self._catalog:
            raise errors.E044(__name__, func=self._name)

        return self._catalog

    @catalog.setter
    def catalog(self, catalog: Catalog):
        """
        Catalog setter to enforce PDC.
        """

        if not self._catalog:
            self._catalog = catalog
        else:
            raise errors.E045(__name__, func=self.__func_name)

    def _capture_artefacts(self, in_: Mapping) -> Mapping:
        """
        Extract and save the artefact of an output dict

        Args:
            out (Dict): the dictionnary to extract artefacts from.
        """

        self.debug(f"craft : capturing artefacts from '{self._name}'")

        if not in_:
            return

        # Only support dictionaries
        if not isinstance(in_, Mapping):
            raise errors.E041(__name__, func=self._name, got=str(type(in_)))

        # Iterate over the artefacts and persist the one existing in the catalog.
        # return only the non-persisted items
        out = {}
        artefacts = []
        for name, artefact in in_.items():
            if name in self.catalog:
                try:
                    self.catalog.save(name, artefact)
                except BaseException as err:  # add details about the callable making the bad call
                    raise errors.E043(__name__, func=self._name) from err
                artefacts.append(name)
            else:
                out[name] = in_[name]

        if artefacts:
            self.info(
                f"craft : artefacts saved from '{self._name}' : '{', '.join(artefacts)}'."
            )

        return out

    def _get_artefacts(self, func: Callable) -> Dict[str, Artefact]:
        """
        Load the artefacts matching a given function.

        Returns:
            Dict[str, Artefact]: a mapping of artefacts
        """

        self.debug(f"craft : loading artefacts for '{self._name}'")

        artefacts = {}
        for param in signature(func).parameters.values():
            if str(param.annotation) in Craft._valids_annotations:
                try:
                    artefacts[param.name] = self.catalog.load(param.name)
                except BaseException as err:  # add details about the callable making the bad call
                    raise errors.E042(__name__, func=self._name) from err

        if artefacts:
            self.info(
                f"craft : artefacts loaded for '{self._name}' : '{' ,'.join(artefacts.keys())}'."
            )

        return artefacts


#############################################################################
#                                   main                                    #
#############################################################################
if __name__ == "__main__":
    raise BaseException("craft.py can't be run in standalone")
