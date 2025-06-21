# saltoapis-python

A Python SDK for interacting with Salto APIs using gRPC, including built-in authentication helpers.

## Getting started

1. Check requirements
2. Install the SDK
3. Authenticate and use the APIs

## Requirements

- Python 3.7+
- `pip` (Python package manager)
- Access to this repository (if private)

## Installation

You can install the SDK directly from GitHub.
Use a specific commit hash or branch.

**In `requirements.txt`:**

```text
saltoapis-python @ git+https://github.com/saltoapis/saltoapis-python.git@<commit-hash-or-tag>
```

**Or with pip:**

```sh
pip install git+https://github.com/saltoapis/saltoapis-python.git@<commit-hash-or-tag>
```

Replace `<commit-hash-or-tag>` with a specific commit, branch, or release tag (e.g., `main` or `v1.0.0`).

## Usage

Once installed, import the SDK and set up authentication.
The SDK provides a gRPC interceptor to handle access tokens automatically.

### Minimal example

```python
import grpc
from saltoapis.auth.interceptor import SaltoapisAuthInterceptor
from saltoapis.nebula.user.v1 import user_pb2, user_pb2_grpc

# Create a secure gRPC channel
channel = grpc.secure_channel('nebula.saltoapis.com', grpc.ssl_channel_credentials())

# Set up authentication interceptor
intercept_channel = grpc.intercept_channel(
    channel, SaltoapisAuthInterceptor(
        client_id='<YOUR_CLIENT_ID>',
        client_secret='<YOUR_CLIENT_SECRET>',
        # Replace with your actual client ID and secret
        scopes=["openid", "offline", "profile", "email", "https://saltoapis.com/auth/nebula"]
    )
)

# Create a service stub
stub = user_pb2_grpc.UserServiceStub(intercept_channel)

# Call an API
response = stub.ListUsers(user_pb2.ListUsersRequest(parent="<your parent installation id>", page_size=10))
for user in response.users:
    print(user.display_name)

# Close the channel when done
channel.close()
```

> **Note:** Always request the following scopes when authenticating:
> `openid, offline, profile, email, https://saltoapis.com/auth/nebula`

You can find more information about authentication at [Salto Nebula API authentication](https://developer.saltosystems.com/nebula/api/authentication/).

### Further examples

Here are some examples of how to use the SDK for common tasks.
Remember to replace variables like `CLIENT_ID`, `CLIENT_SECRET` or `INSTALLATION_NAME` with real values.

#### Create, update and delete user

```python
import grpc
from saltoapis.auth.interceptor import SaltoapisAuthInterceptor
from saltoapis.nebula.user.v1 import user_pb2, user_pb2_grpc
from google.protobuf import field_mask_pb2 as field_mask

# Set your credentials and installation name here
CLIENT_ID = "<YOUR_CLIENT_ID>"
CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
INSTALLATION_NAME = "<YOUR_INSTALLATION_NAME>"

# create grpc channel
channel = grpc.secure_channel('nebula.saltoapis.com', grpc.ssl_channel_credentials())

intercept_channel = grpc.intercept_channel(
    channel, SaltoapisAuthInterceptor(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scopes=['https://saltoapis.com/auth/nebula'],
        # Optionally, you can specify a different discovery host for testing
        discovery_host='account.saltosystems.com'
    )
)

# create service stub (remember to use the intercepted channel)
stub = user_pb2_grpc.UserServiceStub(intercept_channel)

email = "example@saltosystems.com"

# create a new user
response: user_pb2.User = stub.CreateUser(user_pb2.CreateUserRequest(
    parent=INSTALLATION_NAME,
    user=user_pb2.User(
        given_name="Test",
        family_name="User",
        display_name="Test User",
        email=email,
    )
))

# show users
print("Initial users after create:")
response_users: user_pb2.ListUsersResponse = stub.ListUsers(user_pb2.ListUsersRequest(parent=INSTALLATION_NAME, page_size=10))
for user in response_users.users:
    print(user.display_name)

# update the user created name
response: user_pb2.User = stub.UpdateUser(user_pb2.UpdateUserRequest(
    user=user_pb2.User(
        name=response.name,
        family_name="User Updated",
    ),
    update_mask=field_mask.FieldMask(paths=["family_name"])
))

print("\nUsers after updated:")
response_users: user_pb2.ListUsersResponse = stub.ListUsers(user_pb2.ListUsersRequest(parent=INSTALLATION_NAME, page_size=10))
for user in response_users.users:
    print(user.display_name)

# delete the user created
response: user_pb2.User = stub.DeleteUser(user_pb2.DeleteUserRequest(name=response.name))

print("\nUsers after delete:")
response_users: user_pb2.ListUsersResponse = stub.ListUsers(user_pb2.ListUsersRequest(parent=INSTALLATION_NAME, page_size=10))
for user in response_users.users:
    print(user.display_name)

# when you're done, you can close the channel
channel.close()
```

#### Remote unlock

```python
import grpc
from saltoapis.auth.interceptor import SaltoapisAuthInterceptor
from saltoapis.nebula.electroniclock.v1 import electronic_lock_pb2, electronic_lock_pb2_grpc
from saltoapis.nebula.accesspoint.v1 import access_point_pb2, access_point_pb2_grpc

# Set your credentials and installation name here
CLIENT_ID = "<YOUR_CLIENT_ID>"
CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
INSTALLATION_NAME = "<YOUR_INSTALLATION_NAME>"

# create grpc channel
channel = grpc.secure_channel('nebula.saltoapis.com', grpc.ssl_channel_credentials())

intercept_channel = grpc.intercept_channel(
    channel, SaltoapisAuthInterceptor(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scopes=['https://saltoapis.com/auth/nebula'],
        # Optionally, you can specify a different discovery host for testing
        discovery_host='account.saltosystems.com'
    )
)

# create service stub (remember to use the intercepted channel)
stub_el = electronic_lock_pb2_grpc.ElectronicLockServiceStub(intercept_channel)

# get the first electronic lock in the installation
response_el = stub_el.ListElectronicLocks(
    electronic_lock_pb2.ListElectronicLocksRequest(parent=INSTALLATION_NAME, page_size=1)
)

if not response_el.electronic_locks:
    print("No electronic locks found")
    channel.close()
    exit()

print("Choosing the first electronic lock")
electronic_lock = response_el.electronic_locks[0]
print(f"Display name: {electronic_lock.display_name}")
print(f"Name: {electronic_lock.name}")
print(f"Electronic lock's Access Point: {electronic_lock.access_point}")

print(f"Opening the electronic lock '{electronic_lock.display_name}'")

stub_ap = access_point_pb2_grpc.AccessPointServiceStub(intercept_channel)
stub_ap.UnlockAccessPoint(
    access_point_pb2.UnlockAccessPointRequest(name=electronic_lock.access_point)
)

print(f"Electronic lock '{electronic_lock.display_name}' opened")

# when you're done, you can close the channel
channel.close()
```

#### Create and delete unit

```python
import grpc
from saltoapis.auth.interceptor import SaltoapisAuthInterceptor
from saltoapis.nebula.unit.v1 import unit_pb2, unit_pb2_grpc

# Set your credentials and installation name here
CLIENT_ID = "<YOUR_CLIENT_ID>"
CLIENT_SECRET = "<YOUR_CLIENT_SECRET>"
INSTALLATION_NAME = "<YOUR_INSTALLATION_NAME>"

# create grpc channel
channel = grpc.secure_channel('nebula.saltoapis.com', grpc.ssl_channel_credentials())

intercept_channel = grpc.intercept_channel(
    channel, SaltoapisAuthInterceptor(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scopes=['https://saltoapis.com/auth/nebula'],
        # Optionally, you can specify a different discovery host for testing
        discovery_host='account.saltosystems.com'
    )
)

# create service stub (remember to use the intercepted channel)
stub = unit_pb2_grpc.UnitServiceStub(intercept_channel)

# create a new unit with privacy settings
response: unit_pb2.Unit = stub.CreateUnit(unit_pb2.CreateUnitRequest(
    parent=INSTALLATION_NAME,
    unit=unit_pb2.Unit(
        display_name="Test Unit",
        privacy_settings=unit_pb2.Unit.PrivacySettings(
            enabled=True
        )
    )
))

print(f"Created unit: {response.display_name}")

# delete the unit created
stub.DeleteUnit(unit_pb2.DeleteUnitRequest(name=response.name))
print(f"Deleted unit: {response.display_name}")

# when you're done, you can close the channel
channel.close()
```

See also the [Nebula API documentation](https://developer.saltosystems.com/nebula/api/) for detailed information on available services and methods.

## Troubleshooting

- **Authentication errors:**
  - Ensure your client ID, secret, and scopes are correct.
  - Check your network/firewall settings.
- **Import errors:**
  - Make sure you installed the SDK in the correct environment.
- **gRPC errors:**
  - Confirm the API endpoint and credentials are valid.
