# Since OpenConnection and CloseConnection are just containers for functions, it can be clearer to write staticmethods (although this is not required).
class Connection:
    def __init__(self):
        self.state = ClosedConnection

    def open(self):
        self.state.open(self)

    def close(self):
        self.state.close(self)

    def receive(self):
        self.state.receive(self)

    def send(self, data):
        self.state.send(self)


class OpenConnection:
    @staticmethod
    def open(connection: Connection):
        raise RuntimeError("Connection not closed")

    @staticmethod
    def close(connection: Connection):
        connection.state = ClosedConnection

    @staticmethod
    def receive(connection: Connection):
        print("Receiving")

    @staticmethod
    def send(connection: Connection, data):
        print("Sending")


class ClosedConnection:
    @staticmethod
    def open(connection: Connection):
        connection.state = OpenConnection

    @staticmethod
    def close(connection: Connection):
        raise RuntimeError("Connection not open")

    @staticmethod
    def receive(connection: Connection):
        raise RuntimeError("Connection not open")

    @staticmethod
    def send(connection: Connection, data):
        raise RuntimeError("Connection not open")
