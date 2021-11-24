# One way to get rid of the if-statements is to split into two classes, representing each state. (Open and Close).
# Each class then becomes simpler - there are no if-statements, each is single-purpose.


class OpenConnection:
    def open(self):
        raise RuntimeError("Connection not closed")

    def close(self):
        self.state = ClosedConnection

    def receive(self):
        print("Receiving")

    def send(self, data):
        print("Sending")


class ClosedConnection:
    def open(self):
        self.state = OpenConnection

    def close(self):
        raise RuntimeError("Connection not open")

    def receive(self):
        raise RuntimeError("Connection not open")

    def send(self, data):
        raise RuntimeError("Connection not open")


# Glue the classes together
class Connection:
    def __init__(self):
        self.state = ClosedConnection  # One of the classes above

    def open(self):
        self.state.open(self)

    def close(self):
        self.state.close(self)

    def receive(self):
        self.state.receive(self)

    def send(self, data):
        self.state.send(self)


# Calling a function like this may seem strange,
# but this is perfectly valid for all classes.
# >>> con = Connection()
# >>> Connection.open(con) # Same as con.open()
