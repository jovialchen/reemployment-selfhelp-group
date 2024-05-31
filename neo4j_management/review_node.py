import json

from py2neo import Node, Relationship

class ReviewNode:
    def __init__(self, graph, n_matcher, r_matcher ):
        self._graph = graph
        self._n_matcher  = n_matcher
        self._r_matcher  = r_matcher

    def create_review_node(self, node_properties):
        node = self._n_matcher.match("Review", **{"review_id": node_properties["review_id"]}).first()
        if node is None:
            node = Node("Review", **node_properties)
            self._graph.create(node)
        return node

    def create_review_node_relation(self, content_node_value, people_value, review_properties):
        review_node = self.create_review_node(review_properties)
        content_node = self._n_matcher.match("Content", **{"content_uniquev": content_node_value}).first()
        if content_node is not None:
            existing_relation = self._r_matcher.match([content_node, review_node], "HAS_REVIEW")
            if len(existing_relation) == 0:
                relationship = Relationship(content_node, "HAS_REVIEW", review_node)
                self._graph.create(relationship)
        else:
            print (f"{content_node_value} does not exist")
        people_node = self._n_matcher.match("PeopleNode", **{"handle": people_value}).first()
        if people_node is not None:
            existing_relation = self._r_matcher.match([review_node, people_node], "BELONG_TO")
            if len(existing_relation) == 0:
                relationship = Relationship(review_node, "BELONG_TO", people_node)
                self._graph.create(relationship)
        else:
            print (f"{people_value} does not exist")


    @classmethod
    def create_review_nodes(cls, graph, n_matcher, r_matcher):
        review_node = cls(graph, n_matcher, r_matcher)
        json_file = "review_node_info.json"
        with open(json_file, 'r') as file:
            review_data = json.load(file)

        for entry in review_data:
            content_uniquev = entry["content_uniquev"]
            reviewer = entry["reviewer"]
            properties = entry["properties"]
            review_node.create_review_node_relation(content_uniquev, reviewer, properties)

        return review_node

