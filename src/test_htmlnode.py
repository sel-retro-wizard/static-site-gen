# Test cases for HTMLNode class

import unittest
from htmlnode import HTMLNode

class HTMLNodeTest(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("<a>", "some text")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode(tag = "<h1>", value = "some text", props = {"href":"www.link.here"})
        props = ' href="www.link.here"'
        self.assertEqual(node.props_to_html(), props)
        node = HTMLNode(tag="<h1>")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag = "<h1>", value = "Heading One")
        self.assertEqual(repr(node), "HTMLNode(<h1>, Heading One, None, None)") 
       
    def test_values(self):
        node = HTMLNode("div","I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

if __name__ == "__main__":
    unittest.main()

