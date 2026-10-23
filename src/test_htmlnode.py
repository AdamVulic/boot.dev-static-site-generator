import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html2(self):
        node = HTMLNode(
            "href",
            "https://www.google.com",
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )

        self.assertEqual(
            node.props_to_html(),
            " href=\"https://www.google.com\" target=\"_blank\""
        )

    def test_members(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"class": "primary"}
        )

        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, This is a paragraph, children: None, {'class': 'primary'})"
        )

if __name__ == "__main__":
    unittest.main()
