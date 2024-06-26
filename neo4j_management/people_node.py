from py2neo import Node


class PeopleNode:
    def __init__(self, graph, n_matcher):
        self._graph = graph
        self._n_matcher = n_matcher

    def create_people_node(self, node_properties):
        node = self._n_matcher.match("PeopleNode", **{"handle": node_properties['handle']}).first()
        if node is None:
            node = self._graph.create(Node("PeopleNode", **node_properties))
        return node

    @classmethod
    def create_people_nodes(cls, graph, n_matcher):
        people_node = cls(graph, n_matcher)
        jora_properties = {"handle": "jora", "name": "Jo Rahelios", "bio": "Gemini|Hogwarts Alumni|ENFP"}
        people_node.create_people_node(jora_properties)

        return
