from abc import ABC, abstractmethod

class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass

class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"Visitor is visiting {element.__class__.__name__}")

    def visit_concrete_element_b(self, element):
        print(f"Visitor is visiting {element.__class__.__name__}")


def main():
    elements = [ConcreteElementA(), ConcreteElementB()]
    visitor = ConcreteVisitor()

    for element in elements:
        element.accept(visitor)


if __name__ == "__main__":
    main()
