import json
from py2neo import Graph, Node, Relationship
from py2neo.matching import NodeMatcher, RelationshipMatcher

class KnowledgeTree:
    def __init__(self, graph, n_matcher, r_matcher):
        self._graph = graph
        self._n_matcher = n_matcher
        self._r_matcher = r_matcher

    def create_knowledge_tree_node(self, value, name):
        node = self._n_matcher.match("KnowledgeTreeEle", unique_property=value).first()
        if node is None:
            node_properties = {"unique_property": value, "name": name}
            node = Node("KnowledgeTreeEle", **node_properties)
            self._graph.create(node)
        return node

    def create_knowledge_tree_relation(self, node1, node2):
        existing_relation = self._r_matcher.match((node1, node2), "KT_LINK")
        if not existing_relation:
            relationship = Relationship(node1, "KT_LINK", node2)
            self._graph.create(relationship)

    def build_tree_from_dict(self, parent_node, tree_dict):
        for child in tree_dict.get("children", []):
            child_node = self.create_knowledge_tree_node(child["name"], child["name"])
            self.create_knowledge_tree_relation(parent_node, child_node)
            self.build_tree_from_dict(child_node, child)

    @classmethod
    def create_knowledge_tree(cls, graph, n_matcher, r_matcher):
        knowledge_tree = cls(graph, n_matcher, r_matcher)
        file_path = "knowledge_tree_info.json"
        with open(file_path, 'r') as file:
            tree_data = json.load(file)
        knowledge_tree_root = knowledge_tree.create_knowledge_tree_node(tree_data["name"], "Knowledge Tree Root")
        knowledge_tree.build_tree_from_dict(knowledge_tree_root, tree_data)
        return knowledge_tree