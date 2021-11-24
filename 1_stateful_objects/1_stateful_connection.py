# In the example below, there's conditional logic based on the state of the class.
# If there are many states, each method can quickly turn into a tangled mess of if-statements and conditionals. Is there any way to not code it in that way?


class Connection:
    def __init__(self):
        self.state = "CLOSED"

    def open(self):
        if self.state == "CLOSED":
            self.state = "OPEN"
        elif self.state == "OPEN":
            raise RuntimeError("Connection not closed")

    def close(self):
        if self.state == "CLOSED":
            raise RuntimeError("Connection not open")
        elif self.state == "OPEN":
            self.state = "CLOSED"

    def receive(self):
        if self.state == "CLOSED":
            raise RuntimeError("Connection not open")
        elif self.state == "OPEN":
            print("Receiving")

    def send(self, data):
        if self.state == "CLOSED":
            raise RuntimeError("Connection not open")
        elif self.state == "OPEN":
            print("Sending")
