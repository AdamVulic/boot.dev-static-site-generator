import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("Hello!", TextType.PLAIN)
        node2 = TextNode("Hello!", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("Hello!", TextType.BOLD)
        node2 = TextNode("BYE", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("Hello!", TextType.BOLD, "http://test.com")
        node2 = TextNode("Hello!", TextType.BOLD, "http://test.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Example text", TextType.ITALIC, "http://test.com")
        self.assertEqual(repr(node), "TextNode(Example text, TextType.ITALIC, http://test.com)")

if __name__ == "__main__":
    unittest.main()
