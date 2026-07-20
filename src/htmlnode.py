# HTMLNode
# - Our "TextNode" class represents the various types of inline text that can exist in HTML and Markdown.
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
        # If no attributes, return empty string
        if self.props == None:
            return ""
        # Initilise string for return
        html_string = ""
        # for each entry in props dictionary, add to html string. Each attribute has a leading whitespace
        for attribute in self.props:
            html_string += f' {attribute}="{self.props[attribute]}"'
        # Return attribute string
        return html_string

    # dd a __repr__(self) method. Give yourself a way to print an HTMLNode object and see its tag, value, children, and props. 
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"   

