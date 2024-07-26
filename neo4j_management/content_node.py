import json
import time

from py2neo import Node, Relationship

class ContentNode:
    def __init__(self, graph, n_matcher, r_matcher ):
        self._graph = graph
        self._n_matcher  = n_matcher
        self._r_matcher  = r_matcher

    def create_content_node(self, node_properties):
        node = self._n_matcher.match("Content", **{"content_uniquev": node_properties["content_uniquev"]}).first()
        if node is None:
            node = Node("Content", **node_properties)
            self._graph.create(node)
        return node

    def create_content_node_relation(self, kt_node_value, content_properties):
        content_node = self.create_content_node(content_properties)
        kt_node = self._n_matcher.match("KnowledgeTreeEle", **{"unique_property": kt_node_value}).first()
        if kt_node is not None:
            existing_relation = self._r_matcher.match([kt_node, content_node], "HAS_CONTENT")
            if len(existing_relation) == 0:
                relationship = Relationship(kt_node, "HAS_CONTENT", content_node)
                self._graph.create(relationship)
        else:
            print (f"{kt_node_value} does not exist")
        return



    @classmethod
    def create_content_nodes(cls, graph, n_matcher, r_matcher):
        content_node = cls(graph, n_matcher, r_matcher)
        json_file = 'content_node_info.json'

        with open(json_file, 'r', encoding="utf-8") as file:
            content_data = json.load(file)

        for entry in content_data:
            relations = entry["relations"]
            properties = entry["properties"]
            for relation in relations:
                content_node.create_content_node_relation(relation, properties)

        return content_node


