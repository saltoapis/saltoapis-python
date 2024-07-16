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

```python
from saltoapis.nebula.user.v1 import user_pb2, user_pb2_grpc
import grpc

# create grpc channel
channel = grpc.secure_channel(target='nebula.saltoapis.com', credentials=grpc.ssl_channel_credentials())

# create service stub
stub = user_pb2_grpc.UserServiceStub(channel)

# user the service
response: user_pb2.ListUsersResponse = stub.ListUsers(user_pb2.ListUsersRequest(parent="installations/01GP0N4J6DBB6M8RRGCX4F99F6", page_size=10))

for user in response.users:
    print(user.display_name)

channel.close()
```
