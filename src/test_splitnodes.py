# Test cases for split nodes


import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestSplitNodes(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **Bold** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [TextNode("This is text with a ", TextType.PLAIN),TextNode("Bold", TextType.BOLD),TextNode(" word", TextType.PLAIN)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_italic(self):
        node = TextNode("This is text with an _italic_ text", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [TextNode("This is text with an ", TextType.PLAIN),TextNode("italic", TextType.ITALIC),TextNode(" text", TextType.PLAIN)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [TextNode("This is text with a ", TextType.PLAIN),TextNode("code block", TextType.CODE),TextNode(" word", TextType.PLAIN)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_underline(self):
        node = TextNode("This text has a __Underlined__ word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "__", TextType.UNDERLINE)
        expected_nodes = [TextNode("This text has a ", TextType.PLAIN), TextNode("Underlined", TextType.UNDERLINE), TextNode(" word", TextType.PLAIN)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.PLAIN
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.PLAIN),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.PLAIN
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.PLAIN),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    # tests for links and markdown
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images(self):
        matches = extract_markdown_links(
        "This is text with a [link](https://www.test.com)"
        )
        self.assertListEqual([("link", "https://www.test.com")], matches)

if __name__ == "__main__":
    unittest.main()
