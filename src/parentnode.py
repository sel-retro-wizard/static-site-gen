# Our new ParentNode class will handle the nesting of HTML nodes inside of one another.

from htmlnode import HTMLNode

# Create another child class of HTMLNode called ParentNode
class ParentNode(HTMLNode):
    # Build Constructor
    def __init__(self, tag, child, props = None):
        # The tag and children arguments are not optional
        # It doesn't take a value argument
        # props is optional
        super().__init__(tag = tag, children = child, props = props)

    # Add a .to_html method
    def to_html(self):
        # If the object doesn't have a tag, raise a ValueError.
        if self.tag == None:
            raise ValueError("Parent Node is missing tag")
        # If children is missing, raise a ValueError with a different message.
        elif self.children == None:
            raise ValueError("Parent Node is missing child")
        # Otherwise, return a string representing the HTML tag of the node and its children. This should be a recursive method
        else:
            return "success"

    # Overwrite __repr__ for ParentNode
    def __repr__(self):
        return f"ParentNode({self.tag},{self.children},{self.props})"

if __name__ == "__main__":
    node = ParentNode("p", ["somenode"])
    print(node.to_html())
