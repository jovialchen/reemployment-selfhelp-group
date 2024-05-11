from flask import Flask, render_template
from flask_neo4j_utils import get_tree, get_node_data_and_process_relationships
app = Flask(__name__)

@app.route('/node/<node_link>')
def node_page(node_link):
    node_data = get_node_data_and_process_relationships(node_link)
    if not node_data:
        return "Node not found"
    return render_template('tag_page.html', node_data=node_data)


@app.route('/')
def index():
    tree = get_tree()
    return render_template('index.html', tree= tree)


if __name__ == '__main__':
    app.run(debug=True)
