# HTMLNode
# - Our "HTMLNode" class will represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents). It can be block level or inline, and is designed to only output HTML.

# Define HTMLNode class with 4 members. (tag, value, children, props). All members default to None.

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # Add a to_html(self) method. For now, it should just raise a NotImplementedError. Child classes will override this method to render themselves as HTML.
    def to_html(self):
        raise NotImplementedError("To be implemented by child nodes")

    # Add a props_to_html(self) method. It should return a formatted string representing the HTML attributes of the node.
    def props_to_html(self):
        # Initilise string for return
        html_string = ""
        # If no attributes, return empty string
        if self.props == None:
            return html_string
        # for each entry in props dictionary, add to html string. Each attribute has a leading whitespace
        for attribute in self.props:
            html_string += f' {attribute}="{self.props[attribute]}"'
        # Return attribute string
        return html_string

    # dd a __repr__(self) method. Give yourself a way to print an HTMLNode object and see its tag, value, children, and props. 
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

# A LeafNode is a type of HTMLNode that represents a single HTML tag with no children.
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
 
# Our new ParentNode class will handle the nesting of HTML nodes inside of one another.
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
            raise ValueError("Parent Node is missing child/ren")
        # Otherwise, return a string representing the HTML tag of the node and its children. This should be a recursive method
        else:
            string = ""
            for child in self.children:
                string += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{string}</{self.tag}>"
    
    # Overwrite __repr__ for ParentNode
    def __repr__(self):
        return f"ParentNode({self.tag},{self.children},{self.props})"

