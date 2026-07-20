# Test cases for HTMLNode class

import unittest
from htmlnode import HTMLNode

class HTMLNodeTest(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("<a>", "some text")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html_with_link(self):
        node = HTMLNode(tag = "<h1>", value = "some text", props = {"href":"www.link.here"})
        props = ' herf="www.link.here"'
        self.assertEqual(node.props_to_html, props)

    def test_props_to_html_no_attributes(self):
        node = HTMLNode("<h1>")
        self.assertEqual(node.props_to_html, None)

    def test_repr(self):
        pass
        
if __name__ == "__main__":
    unittest.main()

