# Unit test for TextNode

import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node.", TextType.PLAIN)
        node2 = TextNode("This is a text node.", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("This is not a url.", TextType.PLAIN)
        self.assertTrue(node.url == None)

    def test_input_url(self):
        node = TextNode("This is a link", TextType.LINK, "www.testcase.dev")
        self.assertFalse(node.url == None)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node2", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.PLAIN, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text(plain), https://www.boot.dev)", repr(node))

if __name__ == "__main__":
    unittest.main()
