from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action()

class Receiver:
    def action(self):
        print("Receiver: action is executed")

class Invoker:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        if isinstance(self._command, Command):
            self._command.execute()


def main():
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker()

    invoker.set_command(command)
    invoker.execute_command()


if __name__ == "__main__":
    main()
