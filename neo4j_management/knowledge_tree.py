from py2neo import Node, Relationship

class KnowledgeTree:
    def __init__(self, graph, n_matcher, r_matcher ):
        self._graph = graph
        self._n_matcher  = n_matcher
        self._r_matcher  = r_matcher

    def create_knowledge_tree_node(self, value, name):
        node = self._n_matcher.match("KnowledgeTreeEle", **{"unique_property": value}).first()
        if node is None:
            node_properties = {"unique_property": value, "name": name}
            node = self._graph.create(Node("KnowledgeTreeEle", **node_properties))
        return node

    def create_knowledge_tree_relation(self, node1, node2):
        existing_relation = self._r_matcher.match([node1, node2], "KT_LINK")
        if len(existing_relation) == 0:
            relationship = Relationship(node1, "KT_LINK", node2)
            self._graph.create(relationship)

    def create_knowledge_tree_root(self):
        knowledge_tree_root = self.create_knowledge_tree_node("knowledge_tree_root", "Knowledge Tree Root")
        return knowledge_tree_root

    def create_technical_tree(self, knowledge_tree_root):
        # Technical
        technical = self.create_knowledge_tree_node("technical", "Technical")
        self.create_knowledge_tree_relation(knowledge_tree_root, technical)

        # Programming Language
        programming_language = self.create_knowledge_tree_node("programming_language", "Programming Language")
        self.create_knowledge_tree_relation(technical, programming_language)

        # Programming Language Branch
        python = self.create_knowledge_tree_node("python", "Python")
        cplusplus = self.create_knowledge_tree_node("cplusplus", "C++")
        javascript = self.create_knowledge_tree_node("javascript", "JavaScript")

        self.create_knowledge_tree_relation(programming_language, python)
        self.create_knowledge_tree_relation(programming_language, cplusplus)
        self.create_knowledge_tree_relation(programming_language, javascript)

        # Machine Learning
        machine_learning = self.create_knowledge_tree_node("machine_learning", "Machine Learning")
        self.create_knowledge_tree_relation(technical, machine_learning)

        deep_learning = self.create_knowledge_tree_node("deep_learning", "Deep Learning")
        self.create_knowledge_tree_relation(machine_learning, deep_learning)

        natural_language_processing = self.create_knowledge_tree_node("natural_language_processing", "Natural Language Processing")
        self.create_knowledge_tree_relation(machine_learning, natural_language_processing)

        large_language_model = self.create_knowledge_tree_node("large_language_model", "Large Language Model")
        self.create_knowledge_tree_relation(natural_language_processing, large_language_model)

        finetuning = self.create_knowledge_tree_node("finetuning", "Finetuning")
        retrieval_augmented_generation = self.create_knowledge_tree_node("retrieval_augmented_generation", "Retrieval Augmented Generation")
        self.create_knowledge_tree_relation(large_language_model, finetuning)
        self.create_knowledge_tree_relation(large_language_model, retrieval_augmented_generation)

        # Tools
        tools = self.create_knowledge_tree_node("tools", "Tools")
        self.create_knowledge_tree_relation(technical, tools)

        kubernetes = self.create_knowledge_tree_node("kubernetes", "Kubernetes")
        self.create_knowledge_tree_relation(tools, kubernetes)

        git = self.create_knowledge_tree_node("git", "Git")
        self.create_knowledge_tree_relation(tools, git)

        vim = self.create_knowledge_tree_node("vim", "Vim")
        self.create_knowledge_tree_relation(tools, vim)
    def create_soft_skill_tree(self, knowledge_tree_root):
        soft_skill = self.create_knowledge_tree_node("soft_skill", "Soft Skill")
        self.create_knowledge_tree_relation(knowledge_tree_root, soft_skill)

        public_speaking = self.create_knowledge_tree_node("public_speaking", "Public Speaking")
        self.create_knowledge_tree_relation(soft_skill, public_speaking)

        toastmasters_pathway = self.create_knowledge_tree_node("toastmasters_pathway", "Toastmasters Pathway")
        self.create_knowledge_tree_relation(public_speaking, toastmasters_pathway)


    @classmethod
    def create_knowledge_tree(cls, graph, n_matcher, r_matcher):
        knowledge_tree = cls(graph, n_matcher, r_matcher)
        knowledge_tree_root = knowledge_tree.create_knowledge_tree_root()
        knowledge_tree.create_technical_tree(knowledge_tree_root)
        knowledge_tree.create_soft_skill_tree(knowledge_tree_root)
        return knowledge_tree

