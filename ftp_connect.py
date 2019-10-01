from ftplib import FTP


class FTPConnect:
    """
    Return a FTP session through a Context Manager and stop it when the process is terminated
    """
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def __enter__(self):
        self.ftps = FTP(self.host)
        self.ftps.login(self.username, self.password)
        return self.ftps

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ftps.close()
