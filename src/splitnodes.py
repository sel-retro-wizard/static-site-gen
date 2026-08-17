# Split delimiter
# Create TextNodes from raw markdown strings. 
# Does not support nested inline elements
# import textnode
from textnode import TextNode, TextType

# Function to create extract and convert markdown strings into TextNodes.
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    # Initialise new_nodes.
    new_nodes = []
    # Loop through old_nodes
    for node in old_nodes:
        # If node is not TypeText.PLAIN, add to new_nodes. 
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        # Split node based on delimiter.
        split_node = node.text.split(delimiter)
        # Sections
        node_sections = []
        # If no closing delimiter, raise invalid markdown syntax.
        if len(split_node)% 2 == 0:
            raise ValueError("Invalid markdown, section not closed")
        # Loop though each section, adding text and delimiter to node_sections
        for i in range(len(split_node)):
            # Skip blank sections
            if split_node[i] == "":
                continue
            # Add odd sections as plain text
            if i % 2 == 0:
                node_sections.append(TextNode(split_node[i], TextType.PLAIN))
            # Add formatted section
            else:
                node_sections.append(TextNode(split_node[i], text_type))
        # Add node sections to new nodes        
        new_nodes.extend(node_sections)
    # Return new_nodes
    return new_nodes

# Tempory test
if __name__ == "__main__":
    node = TextNode("This is text with a _italic_ text", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    print(new_nodes)
