class RSAPException(Exception):
    pass


class InvalidKey(RSAPException):
    pass


class InvalidArgument(RSAPException):
    pass
