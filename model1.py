class ClassOne:
    def __init__(self, name="User"):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}! This is ClassOne."

    def add(self, a, b):
        return a + b
