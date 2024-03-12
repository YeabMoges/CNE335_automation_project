import os


class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        return os.system(f"ping -n 1 {self.server_ip}")
