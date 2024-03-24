from typing import List, Optional

from api_automation.authentication.base import AuthenticationService
from api_automation.constants import (
    GOOGLE_TOKEN_FILE,
    BASE_CREDENTIAL_PATH,
    GOOGLE_FOLDER,
    GOOGLE_CREDENTIALS_FILE,
    GOOGLE_CREDENTIALS_FOLDER,
    GOOGLE_TOKENS_FOLDER,
)
from api_automation.exceptions.authentication import CredentialCreationException
from enums.google import GoogleScope

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


class GoogleAuthenticationService(AuthenticationService):
    def __init__(self, required_scope: GoogleScope):
        super().__init__()

        # The URL of the scopes, it needs to be a list
        self.scopes_url: List[str] = [required_scope.get_url()]

        self._credentials: Optional[Credentials] = None

        # The path to the credentials file
        self._credentials_folder = os.path.join(
            BASE_CREDENTIAL_PATH, GOOGLE_FOLDER, GOOGLE_CREDENTIALS_FOLDER
        )

        # The path to the token file
        self._token_folder = os.path.join(
            BASE_CREDENTIAL_PATH,
            GOOGLE_FOLDER,
            GOOGLE_TOKENS_FOLDER,
            required_scope.get_token_path(),
        )

    def verify(self):
        # Code taken from Google guide

        token_file = os.path.join(self._token_folder, GOOGLE_TOKEN_FILE)

        # Check if the token file exists.
        if os.path.exists(token_file):
            # If it exists, load the credentials from the file
            self._credentials = Credentials.from_authorized_user_file(
                token_file, self.scopes_url
            )

        else:
            # If the token folder does not exist, create it
            os.makedirs(self._token_folder, exist_ok=True)

        # If the token file is not there, or it's there but credentials are
        # not valid anymore, the user needs to log in.
        if self._credentials is None or not self._credentials.valid:
            # If the credentials are expired, but there is a refresh token,
            # refresh the credentials.
            if (
                self._credentials is not None
                and self._credentials.expired
                and self._credentials.refresh_token  # noqa
            ):
                self._credentials.refresh(Request())

            # If there are no credentials, or they are not valid, let the user
            # log in.
            else:
                credential_path = os.path.join(
                    self._credentials_folder, GOOGLE_CREDENTIALS_FILE
                )

                flow = InstalledAppFlow.from_client_secrets_file(
                    credential_path, self.scopes_url
                )
                self._credentials = flow.run_local_server(port=0)

            if self._credentials is None:
                raise CredentialCreationException("Credentials could not be loaded.")

            # Save the credentials for the next run
            with open(token_file, "w") as token_file:
                token_file.write(self._credentials.to_json())

    @property
    def credentials(self) -> Credentials:
        return self._credentials
