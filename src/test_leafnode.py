# Test cases for LeafNode class

import unittest
from leafnode import LeafNode

class LeafNodeTests(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "This is an image", {"src":"url/of/image.jpg", "alt":"Description of image"})
        self.assertEqual(node.to_html(), '<img src="url/of/image.jpg" alt="Description of image">This is an image</img>')
