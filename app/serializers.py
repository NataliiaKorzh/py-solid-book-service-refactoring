import json
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod

from app.main import Book


class BookSerializer(ABC):

    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JSONBookSerializer(BookSerializer):

    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLBookSerializer(BookSerializer):

    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")
