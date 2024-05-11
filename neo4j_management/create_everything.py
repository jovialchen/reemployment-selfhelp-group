from py2neo import Graph, NodeMatcher, RelationshipMatcher

from knowledge_tree import KnowledgeTree
from people_node import PeopleNode
from content_node import ContentNode
from review_node import ReviewNode

# Create a graph object
graph = Graph("neo4j://localhost:7687", auth=("neo4j", "1234"))
# 创建NodeMatcher对象
n_matcher = NodeMatcher(graph)
r_matcher = RelationshipMatcher(graph)

knowledge_trees = KnowledgeTree.create_knowledge_tree(graph, n_matcher, r_matcher)
people_nodes = PeopleNode.create_people_nodes(graph, n_matcher)
content_nodes = ContentNode.create_content_nodes(graph, n_matcher, r_matcher)
review_nodes = ReviewNode.create_review_nodes(graph, n_matcher, r_matcher)