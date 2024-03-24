class AuthenticationException(Exception):
    """
    Raised when authentication fails.
    """


class CredentialCreationException(AuthenticationException):
    """
    Raised when the credentials are invalid.
    """
