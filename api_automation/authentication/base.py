from abc import ABC, abstractmethod
from typing import TypeVar

from google.oauth2.credentials import Credentials

from api_automation.exceptions.authentication import AuthenticationException

CREDENTIAL_TYPE = TypeVar("CREDENTIAL_TYPE", Credentials, str, None)


class AuthenticationService(ABC):
    """
    Base class for authentication services.
    """

    @abstractmethod
    def verify(self):
        """
        Method that verifies whether the user
        has the necessary equipment to
        authenticate.

        All subclasses must implement this method.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def credentials(self):
        """
        Method that returns the credentials
        of the user.

        All subclasses must implement this method.
        """
        raise NotImplementedError

    def get_credentials(self) -> CREDENTIAL_TYPE:  # type: ignore
        """
        Method that verifies the user and
        returns its credentials
        """
        try:
            self.verify()
        except Exception as e:
            raise AuthenticationException from e
        return self.credentials
