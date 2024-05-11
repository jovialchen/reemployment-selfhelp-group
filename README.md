🌳 Welcome to our ***EX BER BER TEA*** Team! 🌟 We're a group of avid learners 📚 who are passionate about 🤓 understanding and sharing our knowledge 🧠 with each other. Our mission 🚀 is to cultivate a diverse garden 🌱 of insights and wisdom 💡, nurturing each other's growth 🌱 along the way. From the roots 🌿 of foundational concepts to the vibrant blooms 🌺 of cutting-edge discoveries, we're committed to 🤝 supporting one another on our learning journey. Together, we'll explore 🌍 new branches 🌿 of knowledge and chart the course 🗺️ to greater understanding. Join us as we embark on this exciting adventure! 🚀✨


## Installation
### Installation Guide for Neo4j on Windows

#### Step 1: Install Java
1. Download and install Java Development Kit (JDK) from [Oracle's official website](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
2. Set up the Java environment path.

#### Step 2: Install Neo4j
1. Download Neo4j Desktop from the [official Neo4j website](https://neo4j.com/download/).
2. Install Neo4j Desktop and follow the installation instructions.
3. Set up the Neo4j environment path.

## Running Python App
After installing Neo4j, run your Python application using `python app.py`.

## Neo4j Database Structure
### Node Types:
- `Content`: Represents different types of content in the database.
- `KnowledgeTreeEle`: Nodes in the knowledge tree.
- `PeopleNode`: Nodes representing people who review content.
- `Review`: Represents reviews for each content.

### Relationships:
- `(:KnowledgeTreeEle)-[:HAS_CONTENT]->(:Content)`: Indicates that a node in the knowledge tree has associated content.
- `(:Content)-[:HAS_REVIEW]->(:Review)`: Content nodes have reviews associated with them.
- `(:Review)-[:BELONG_TO]->(:PeopleNode)`: Reviews belong to specific people.

## Key Points
### Maintaining Knowledge Tree
- Maintain a tree structure of the knowledge tree.
- Add content to the most leaf tag on the knowledge tree.
- The knowledge tree can only be updated when at least 3 members of the core team reach an agreement.

### Content Types:
1. Project
2. Course
3. Book
4. Mentorship
5. Certificate
6. Self-Summary
7. Achievement
8. Event
9. SharingSession

## References
- [Neo4j Installation Guide (Chinese)](https://www.cnblogs.com/ljhdo/p/5521577.html)
