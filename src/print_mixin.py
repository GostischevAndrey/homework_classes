class PrintMixin:

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        super().__init__()
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})" # type: ignore # noqa
