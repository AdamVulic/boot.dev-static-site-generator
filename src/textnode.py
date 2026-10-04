from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"

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
