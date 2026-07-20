# Test cases for HTMLNode class

import unittest
import htmlnode

class HTMLNodeTest(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("<a>", "some text")
        node.to_html()

    def test_props_to_html(self):
        node = HTMLNode("<h1>", "Some other text", None, {"H1":"Heading One"})
        node2 = HTMLNode()
        node.props_to_html()
        node2.props_to_html()

    def test_repr(self):
        node = HTMLNode("<h1>", "Some other text", None, {"H1":"Heading One"})
        self.assertEqual("<h1>, Some other text, 

if __name__ == "__main__":
    unittest.main()

