# Store an enum called TextType. It should cover all inline text types.
# Inline refers to text inside a larger block of text

# Import Enum from enum
from enum import Enum
# Import LeafNode from htmlnode
from htmlnode import LeafNode

# Create enum called TextType. Should contain all types specified in project outline
class TextType(Enum):
    PLAIN = "text(plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

# Create class called TextNode that contains 3 properities. 
class TextNode():
    def __init__(self, text: str, text_type: TextType, url = None):
        # self.text - The text content of the node
        self.text = text
        # self.text_type - The type of text in the node. Which is a member of the enum.
        self.text_type = text_type
        # self.url - The URL of the link or image. Defaults to None.
        self.url = url
    # Create __eq__ equality method to compare self and another instance (other). Return True if all properties are equal
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
    # Create __repr__ method to return string representation of TextNode object - TextNode(TEXT, TEXT_TYPE, URL)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


# Convert TextNode to LeafNode
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    # handle each type of the TextType enum.
    # If it gets a TextNode that is none of those types, it should raise an exception. Otherwise return a new LeafNode object.
    try:
        match text_node.text_type:
            # TextType.TEXT: no tag, text
            case TextType.PLAIN:
                return LeafNode(None, text_node.text)
            # TextType.BOLD: "b" tag, text
            case TextType.BOLD:
                return LeafNode("b", text_node.text)
            # TextType.ITALIC: "i" tag, text
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            # TextType.CODE: "code" tag, text
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            # TextType.LINK: "a" tag, anchor text, and "href" prop
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href":text_type.url})
            # TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
            case TextType.IMAGE:
                return LeafNode("img", None, {"src":text_type.url, "alt":text_type.text})

    except AttributeError as e:
        raise e


