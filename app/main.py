class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    from app.serializers import JSONBookSerializer, XMLBookSerializer
    from app.displayers import ConsoleDisplayer, ReverseDisplayer
    from app.printers import ConsolePrinter, ReversePrinter

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                displayer = ConsoleDisplayer()
                return displayer.display(book)
            elif method_type == "reverse":
                displayer = ReverseDisplayer()
                return displayer.display(book)
        elif cmd == "print":
            if method_type == "console":
                printer = ConsolePrinter()
                return printer.print(book)
            elif method_type == "reverse":
                printer = ReversePrinter()
                return printer.print(book)
        elif cmd == "serialize":
            if method_type == "json":
                serializer = JSONBookSerializer()
                return serializer.serialize(book)
            elif method_type == "xml":
                serializer = XMLBookSerializer()
                return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
