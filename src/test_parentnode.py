import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_single_child(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def test_to_html_single_grandchild(self):
        grandchild= LeafNode("b", "grandchild")
        child = ParentNode("i", [grandchild])
        parent = ParentNode("u", [child])
        self.assertEqual(parent.to_html(), "<u><i><b>grandchild</b></i></u>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "bold"),
                LeafNode(None,"plain"),
                LeafNode("i", "italic"),
                LeafNode(None, "plain"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>bold</b>plain<i>italic</i>plain</p>",
        )

    def test_tag_empty(self):
        child = LeafNode("p","text")
        node = ParentNode(None,[child])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "invalid HTML: no tag")

    def test_children_none(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "invalid HTML: no children")

    def test_children_empty(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "invalid HTML: no children")
