import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def get_credentials(path="keys",scopes=[]):
    url_token = f"{path}/token.json"
    url_credentials = f"{path}/credentials.json"
    creds = None
    # The file credentials.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(url_token):
        creds = Credentials.from_authorized_user_file(url_token, scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(url_credentials, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(url_token, 'w') as token:
            token.write(creds.to_json())
    return creds

if __name__ == '__main__':
    creds=get_credentials("keys")