from py2neo import Graph, NodeMatcher, RelationshipMatcher
from collections import defaultdict

# 连接到Neo4j数据库
graph = Graph("bolt://localhost:7687", auth=("neo4j", "1234"))  # 替换为你的数据库地址、用户名和密码
node_matcher = NodeMatcher(graph)
relationship_matcher = RelationshipMatcher(graph)


# 通过节点匹配器检索树结构
def get_tree():
    root_node = node_matcher.match("KnowledgeTreeEle", unique_property="knowledge_tree_root").first()
    tree = {'name': root_node['name'], 'link': root_node['unique_property'], 'children': {}}
    get_children(tree, root_node)
    return tree


def get_children(parent, parent_node):
    for rel in relationship_matcher.match((parent_node, None), "KT_LINK"):
        child_node = rel.end_node
        has_content = any('Content' in rel.end_node.labels and True for rel in
                          relationship_matcher.match((child_node, None), 'HAS_CONTENT'))
        child = {'name': child_node['name'], 'link': child_node['unique_property'], 'has_content': has_content,
                 'children': {}}
        parent['children'][child_node['name']] = child
        get_children(child, child_node)


def get_node_data(node, node_link):
    node_data = {
        'node_name': node['name'],
        'unique_value': node_link,
        'contents': defaultdict(list)
    }
    return node_data


def get_content_info(content_node):
    content_info = {
        'unique_value': content_node['content_uniquev'],
        'other_tags': [],
        'type': content_node['type'],
        'info': content_node['info'],
        'reviews': []
    }
    return content_info


def get_tag_info(tag_node):
    tag_info = {
        'link': tag_node['unique_property'],
        'name': tag_node['name'],
    }
    return tag_info


def get_review_data(review_node):
    review_data = {
        'comments': review_node['comments'],
        'stars': review_node['stars'],
        'status': review_node['status'],
        'people': None,
        'bio': None
    }
    return review_data


def get_people_info(review_node):
    people_relationship = relationship_matcher.match((review_node, None), 'BELONG_TO').first()
    people_node = people_relationship.end_node
    if people_node and 'PeopleNode' in people_node.labels:
        return people_node['name'], people_node['bio']
    return None, None


def process_node_relationships(node, node_data):
    node_relationships = get_node_relationships(node)
    for node_relationship in node_relationships:
        content_node = node_relationship.end_node
        if content_node and 'Content' in content_node.labels:
            content_name = content_node['name']
            content_info = get_content_info(content_node)
            process_tag_relationships(content_node, content_info)
            process_review_relationships(content_node, content_info)
            node_data['contents'][content_name] = content_info

def get_node_relationships(node):
    return relationship_matcher.match((node, None), 'HAS_CONTENT').all()

def process_tag_relationships(content_node, content_info):
    tag_relationships = relationship_matcher.match((None, content_node), 'HAS_CONTENT').all()
    for tag_relationship in tag_relationships:
        tag_node = tag_relationship.start_node
        if tag_node and 'KnowledgeTreeEle' in tag_node.labels:
            tag_info = get_tag_info(tag_node)
            content_info['other_tags'].append(tag_info)

def process_review_relationships(content_node, content_info):
    review_relationships = relationship_matcher.match((content_node, None), 'HAS_REVIEW').all()
    for review_relationship in review_relationships:
        review_node = review_relationship.end_node
        if review_node and 'Review' in review_node.labels:
            review_data = get_review_data(review_node)
            people_info = get_people_info(review_node)
            if people_info:
                review_data['people'], review_data['bio'] = people_info
            content_info['reviews'].append(review_data)

def get_node_data_and_process_relationships(node_link):
    # Assuming get_node_data_and_process_relationships function takes node_link as input
    node = node_matcher.match("KnowledgeTreeEle", **{"unique_property": node_link}).first()
    if not node:
        return None  # Return None if node not found

    node_data = get_node_data(node, node_link)
    process_node_relationships(node, node_data)

    return node_data
