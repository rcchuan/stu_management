class CustormException(Exception):
    def __init__(self, code, msg,data=None):
        self.code = code
        self.msg = msg
        self.data = data