# Split delimiter
# Create TextNodes from raw markdown strings. 
# Does not support nested inline elements
# import textnode
from textnode import TextNode, TextType
# Import re for regex search
import re

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

# Function to extract images from raw markdown text. Returns a list of tuples.
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

# Funciton to extract links from raw markdown text. Returns list of tuples.
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


# Tempory test
if __name__ == "__main__":
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
