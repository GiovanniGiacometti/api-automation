from enum import Enum

from api_automation.constants import GOOGLE_BASE_URL


class GoogleScope(Enum):

    CALENDAR = 'calendar'
    GMAIL_READONLY = 'gmail.readonly'
    GMAIL_MODIFY = 'gmail.modify'

    def get_url(self) -> str:

        if self == GoogleScope.CALENDAR:
            return "/".join([GOOGLE_BASE_URL, "calendar"])
        elif self == GoogleScope.GMAIL_READONLY:
            return "/".join([GOOGLE_BASE_URL, "gmail.readonly"])
        elif self == GoogleScope.GMAIL_MODIFY:
            return "/".join([GOOGLE_BASE_URL, "gmail.modify"])

        raise ValueError(f"Unknown GoogleScope: {self}")

    def get_token_path(self) -> str:
        if self == GoogleScope.CALENDAR:
            return "calendar"
        elif self == GoogleScope.GMAIL_MODIFY:
            return "gmail_modify"
        elif self == GoogleScope.GMAIL_READONLY:
            return "gmail_readonly"

        raise ValueError(f"Unknown GoogleScope: {self}")
