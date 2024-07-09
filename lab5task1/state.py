from abc import ABC, abstractmethod

class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

    def set_state(self, state):
        self._state = state

class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA is handling the request")

class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB is handling the request")

def main():
    context = Context(ConcreteStateA())
    context.request()

    context.set_state(ConcreteStateB())
    context.request()


if __name__ == "__main__":
    main()
