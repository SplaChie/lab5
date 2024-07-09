from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operation()
        self.base_operation2()

    def base_operation1(self):
        print("AbstractClass: base operation 1 is called")

    def base_operation2(self):
        print("AbstractClass: base operation 2 is called")

    @abstractmethod
    def required_operation(self):
        pass

class ConcreteClass(AbstractClass):
    def required_operation(self):
        print("ConcreteClass: overridden required operation is called")


def main():
    concrete = ConcreteClass()
    concrete.template_method()


if __name__ == "__main__":
    main()
