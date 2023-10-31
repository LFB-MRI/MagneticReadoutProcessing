import networkx as nx
import pytest
import unittest

from import_pkgs import __fix_import_udpp__
__fix_import_udpp__()

from MRPudpp.UDPPFunctionTranslator import UDPPFunctionTranslator
class TestMRPReading(unittest.TestCase):

    calltree_graph: nx.DiGraph

    def setUp(self) -> None:
        pipelines: dict = UDPPFunctionTranslator.load_pipelines("./assets")
        print(pipelines)

        pipeline: dict = pipelines[0]
        settings: dict = pipeline['settings']
        # EXTRACT STEPS
        # also checks duplicate pipeline steps
        steps = UDPPFunctionTranslator.extract_pipelines_steps(pipeline)
        print("found following valid steps: {}".format(steps))
        # CREATE CALLTREE
        self.calltree_graph: nx.DiGraph = UDPPFunctionTranslator.create_calltree_graph(steps)
        print("calltree generated: {}".format(self.calltree_graph))

    def test_udpp_(self):
        connections: [] = UDPPFunctionTranslator.get_node_connection_list(self.calltree_graph)
        print(connections)


if __name__ == '__main__':
    unittest.main()
