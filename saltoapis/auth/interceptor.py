import collections
import grpc

from .token_provider import OAuthClientCredentialsProvider, SaltoapisOAuthClientCredentialsProvider

from typing import Optional, Iterable

class _ClientCallDetails(
    collections.namedtuple(
        "_ClientCallDetails", ("method", "timeout", "metadata", "credentials")
    ),
    grpc.ClientCallDetails,
):
    pass

class SaltoapisAuthInterceptor(grpc.UnaryUnaryClientInterceptor):
    """Intercepts gRPC calls and adds an authorization header with an access token."""

    def __init__(self, 
                 token_provider: Optional[OAuthClientCredentialsProvider] = None,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 scopes: Optional[Iterable[str]] = None,
                 discovery_host: Optional[str] = None):
        """Initializes the interceptor.

        You need to provide either a token_provider or your client_id and client_secret.
        
        Args:
            token_provider: An OAuthClientCredentialsProvider to use to get an access token.
            client_id: The client id of your application.
            client_secret: The client secret of your application.
        """

        if token_provider is not None:
            self.token_provider = token_provider
        elif client_id is not None and client_secret is not None:
            self.token_provider: OAuthClientCredentialsProvider = SaltoapisOAuthClientCredentialsProvider(client_id, client_secret, scopes, discovery_host)
        else:
            raise Exception("you need to provide either a token_provider or your client_id and client_secret") 

    def intercept_unary_unary(self, continuation, client_call_details, request):
        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)

        metadata.append(('authorization', 'Bearer ' + self.token_provider.get_access_token()))
                
        new_client_call_details = _ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
        )

        response = continuation(new_client_call_details, next(iter((request,))))
        return response
