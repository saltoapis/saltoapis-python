# saltoapis-python

## Installation

To install the Python SDK, first you need to make sure that you have access to this repository from your `git` client.

Then, you can install the SDK using `pip`. To do so, simply add this repo as a dependency in your `requirements.txt` file:
```
saltoapis-python @ git+https://github.com/saltoapis/saltoapis-python.git@<commit-hash>
```

Or run the following command:

```
pip install git+https://github.com/saltoapis/saltoapis-python.git@<commit-hash>
```

## Usage

Once you have installed the SDK, you can use it by importing the desired APIs.
Additionaly, the SDK provides a simple gRPC interceptor that will automatically get and refresh valid access tokens and include them in all gRPC requests.

1. Create a gRPC channel:

```python
import grpc

# create grpc channel
channel = grpc.secure_channel(target='nebula.saltoapis.com', credentials=grpc.ssl_channel_credentials())
```

2. And add the saltoapis authentication interceptor:

> **Note**
> You should always request the following scopes when authenticating:
> ```
> openid, offline, profile, email, https://saltoapis.com/auth/nebula
> ```

```python
from saltoapis.auth.interceptor import SaltoapisAuthInterceptor

intercept_channel = grpc.intercept_channel(
    channel, SaltoapisAuthInterceptor(
        client_id='<your-client-id>',
        client_secret='<your-client-secret>',
        scopes=["openid", "offline", "profile", "email", "https://saltoapis.com/auth/nebula"],
        # Optionally, you can specify a different discovery host. This may be useful for testing purposes
        discovery_host="account.saltosystems.com"
    )
)
```

3. Now you can create a new gRPC service stub and call any API you want:

```python
from saltoapis.nebula.user.v1 import user_pb2, user_pb2_grpc

# create service stub (remember to use the intercepted channel)
stub = user_pb2_grpc.UserServiceStub(intercept_channel)

# user the service
response: user_pb2.ListUsersResponse = stub.ListUsers(user_pb2.ListUsersRequest(parent="<your parent installation id>", page_size=10))

for user in response.users:
    print(user.display_name)

# when you're done, you can close the channel
channel.close()
```
