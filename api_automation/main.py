from api_automation.authentication.google import GoogleAuthenticationService
from enums.google import GoogleScope


def main():
    for scope in list(GoogleScope):
        
        print(f"Checking credentials for {scope.value}")
        auth_service = GoogleAuthenticationService(required_scope=scope)

        credentials = auth_service.get_credentials()

        assert credentials is not None


if __name__ == "__main__":
    main()
