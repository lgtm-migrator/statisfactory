#! /usr/bin/python3

# viz.py
#
# Project name: statisfactory
# Author: Hugo Juhel
#
# description:
"""
    Implements Graph Visualizer (potentially various)
"""

#############################################################################
#                                 Packages                                  #
#############################################################################

# system
# Third party
import networkx as nx
from networkx.algorithms import transitive_reduction

# project
from statisfactory.errors import Errors

# TODO : To be fully reworked : "quick" way to get a graphical representation of the pipeline.
#############################################################################
#                                  Script                                   #
#############################################################################


class Graphviz:
    """
    Display a Networkx graph using GraphViz.
    """

    def __call__(self, G):
        """
        Plot the graph in GraphViz
        """

        try:
            import graphviz
        except ImportError:
            raise Errors.E054(dep="graphviz")  # type: ignore

        try:
            import pygraphviz  # noqa
        except ImportError:
            raise Errors.E054(dep="pygraphviz")  # type: ignore

        # Remove redondencies
        reduction = transitive_reduction(G)

        # Tranform the Graph into an AGraph one
        A = nx.nx_agraph.to_agraph(reduction)
        A.layout("dot")

        return graphviz.Source(A.to_string())


#############################################################################
#                                   main                                    #
#############################################################################

if __name__ == "__main__":
    raise BaseException("viz.py can't be run in standalone")