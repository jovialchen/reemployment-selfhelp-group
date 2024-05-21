from py2neo import Node, Relationship

class ContentNode:
    def __init__(self, graph, n_matcher, r_matcher ):
        self._graph = graph
        self._n_matcher  = n_matcher
        self._r_matcher  = r_matcher

    def create_content_node(self, node_properties):
        node = self._n_matcher.match("Content", **{"content_uniquev": node_properties["content_uniquev"]}).first()
        if node is None:
            node = self._graph.create(Node("Content", **node_properties))
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



    @classmethod
    def create_content_nodes(cls, graph, n_matcher, r_matcher):
        content_node = cls(graph, n_matcher, r_matcher)
        experpert1_kubernetes_properties = {
            "content_uniquev": "experpert1_kubernetes",
            "name": "EXPERPERT #1: Kubernetes Basics",
            "type": "Experpert",
            "info": "temp"
        }
        content_node.create_content_node_relation("kubernetes", experpert1_kubernetes_properties)

        tmpw_innovative_planning = {
            "content_uniquev": "tmpw_innovative_planning",
            "name": "Toastmasters Pathway: Innovative Planning",
            "type": "Course",
            "info": "<p>Find the content from the following link <a href=\"https://www.toastmasters.org/guides\">Toastmasters</a> find the course from Base Camp.</p>"
        }
        content_node.create_content_node_relation("toastmasters_pathway", tmpw_innovative_planning)

        tmpw_dynamic_leadership = {
            "content_uniquev": "tmpw_dynamic_leadership",
            "name": "Toastmasters Pathway: Dynamic Leadership",
            "type": "Course",
            "info": "<p>Find the content from the following link <a href=\"https://www.toastmasters.org/guides\">Toastmasters</a> find the course from Base Camp.</p>"
        }
        content_node.create_content_node_relation("toastmasters_pathway", tmpw_dynamic_leadership)
        logxpert_sbc = {
            "content_uniquev": "logxpert_sbc",
            "name": "LogXpert: efficient log analysis tool for SBC",
            "type": "Project",
            "info": "hahahha</p>"
        }
        content_node.create_content_node_relation("finetuning", logxpert_sbc)
        content_node.create_content_node_relation("retrieval_augmented_generation", logxpert_sbc)
        content_node.create_content_node_relation("python", logxpert_sbc)

        the_daily_stoic = {
            "content_uniquev": "the_daily_stoic",
            "name": "The Daily Stoic",
            "type": "Book",
            "info": "A Journal which you can keep to reflect you life like a stoic philosopher"
        }
        content_node.create_content_node_relation("stoicism", the_daily_stoic)
        what_if = {
            "content_uniquev": "what_if",
            "name": "What if",
            "type": "Book",
            "info": "Author: Randall Munroe"
        }
        content_node.create_content_node_relation("popular_science_books", what_if)
        how_to = {
            "content_uniquev": "how_to",
            "name": "How to",
            "type": "Book",
            "info": "Author: Randall Munroe</p>"
        }
        content_node.create_content_node_relation("popular_science_books", how_to)
        return


