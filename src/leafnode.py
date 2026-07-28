# A LeafNode is a type of HTMLNode that represents a single HTML tag with no children.

from htmlnode import HTMLNode

# Create a child class of HTMLNode called LeafNode. 
class LeafNode(HTMLNode):
    # Constructor should not allow for children.
    # Value and Tag are mandatory, props optional.
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props = props)

    # Add a .to_html() method that renders a leaf node as an HTML string (by returning a string)
    def to_html(self):
     # If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
       if self.value == None:
            raise ValueError("All leaf nodes must have a value")
     # If there is no tag (e.g. it's None), the value should be returned as raw text.
       elif self.tag == None:
            return self.value
     # Otherwise, it should render an HTML tag
       else:
           if self.props == None:
               return f"<{self.tag}>{self.value}</{self.tag}>"
           else:
               return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    # Override the __repr__ method. It should be similar to HTMLNode's but doesn't include children in the string.
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

if __name__ == "__main__":
   node1 = LeafNode("p", "This is a paragraph of text.")
   print(node1)
   print(node1.to_html())
   node2 = LeafNode("a", "Click me!", props = {"href": "https://www.google.com"})
   print(node2)
   print(node2.to_html())
   
