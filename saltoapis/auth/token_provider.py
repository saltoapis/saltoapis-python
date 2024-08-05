import urllib.request
import time    
import json

from typing import Optional, Iterable

class OAuthClientCredentialsProvider:
    """A client credentials provider that provides an access token."""

    def get_access_token() -> str:
        """Returns the access token."""
        pass

class SaltoapisOAuthClientCredentialsProvider(OAuthClientCredentialsProvider):
    """A client credentials provider that uses the Saltoapis OAuth2 API to get an access token."""
    
    access_token: Optional[str] = ""
    access_token_expiration_time: int = 0

    def __init__(self, client_id: str, client_secret: str, scopes: Iterable[str], discovery_host: str = "account.saltosystems.com"):
        """Initializes the client credentials provider.

        Args:
            client_id: The client id of your application.
            client_secret: The client secret of your application.
            scopes: The scopes to request.
            discovery_host: The host to use to discover the OAuth2 API. Defaults to "account.saltosystems.com".
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = scopes
        self.discovery_host = discovery_host

    def get_access_token(self) -> str:
        if int(time.time()) >= self.access_token_expiration_time:
            self._refresh_token()
        
        return self.access_token

    def _refresh_token(self):
        # get oidc config
        oidc_config_uri = 'https://%s/.well-known/openid-configuration' % self.discovery_host 

        with urllib.request.urlopen(oidc_config_uri) as response:
            oidc_config = json.loads(response.read())
            if not oidc_config.get('token_endpoint'):
                raise Exception("The oidc config is missing the token_endpoint. Check that the JSON in %s includes this field." % oidc_config_uri)
            
            # request new token
            self._request_new_token(oidc_config['token_endpoint'])
    
    def _request_new_token(self, token_endpoint: str):
        """Requests a new token from the token endpoint using client credentials.

        Args:
            token_endpoint: The token endpoint to request a new token from.
        """
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': ' '.join(self.scopes)
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        request = urllib.request.Request(token_endpoint, data=urllib.parse.urlencode(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(request) as response:
            response_data = json.loads(response.read())

            if 'access_token' not in response_data:
                raise Exception("The response from the token endpoint did not contain an access_token. Check that the JSON in %s includes this field." % token_endpoint)
            
            if 'expires_in' not in response_data:
                raise Exception("The response from the token endpoint did not contain an expires_in field. Check that the JSON in %s includes this field." % token_endpoint)

            self.access_token = response_data['access_token']
            self.access_token_expiration_time = int(time.time()) + response_data['expires_in']
