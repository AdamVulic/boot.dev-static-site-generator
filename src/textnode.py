from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        equal = True
        if self.text != other.text:
            equal = False
        if self.text_type != other.text_type:
            equal = False
        if self.url != other.url:
            equal = False
        return equal

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    text = text_node.text
    type = text_node.text_type
    match type:
        case type.TEXT:
            return LeafNode(None, text)
        case type.BOLD:
            return LeafNode("b", text)
        case type.ITALIC:
            return LeafNode("i", text)
        case type.CODE:
            return LeafNode("code", text)
        case type.LINK:
            return LeafNode("a", text, {"href": text_node.url})
        case type.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text})
        case _:
            raise ValueError("error: text type not recognised")
