# Store an enum called TextType. It should cover all inline text types.
# Inline refers to text inside a larger block of text

# Import Enum from enum
from enum import Enum

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

