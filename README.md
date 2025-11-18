# GoHighLevel Python SDK


Official Python SDK for the GoHighLevel API. This library provides a convenient way to interact with GoHighLevel's APIs from applications written in Python.

## Installation

```bash
# Install the SDK 
pip install gohighlevel-api-client
```

## Quick Start

### Basic Usage

```python
from highlevel import HighLevel

# Or initialize with OAuth credentials
client = HighLevel(
    client_id="your_client_id",
    client_secret="your_client_secret"
)
```

### OAuth Flow Example

```python
import asyncio
from highlevel import HighLevel

async def oauth_example():
    client = HighLevel(
        client_id="your_client_id",
        client_secret="your_client_secret"
    )
    
    # Step 1: Get authorization URL
    auth_url = client.oauth.get_authorization_url(
        client_id="your_client_id",
        redirect_uri="https://your-app.com/callback",
        scope="contacts.readonly campaigns.readonly"
    )
    print(f"Visit: {auth_url}")
    
    # Step 2: Exchange code for tokens (after user authorization)
    token_data = await client.oauth.get_access_token({
        "client_id": "your_client_id",
        "client_secret": "your_client_secret",
        "grant_type": "authorization_code",
        "code": "authorization_code_from_callback",
        "redirect_uri": "https://your-app.com/callback"
    })
    
    # Tokens are automatically stored in session storage
    print("OAuth flow completed successfully!")

asyncio.run(oauth_example())
```

## Storage
It can be used to store the access and refresh token for your application. 

### MongoDB Storage
```python
from highlevel import HighLevel
from highlevel.storage import MongoDBSessionStorage

storage = MongoDBSessionStorage(
    connection_string="mongodb://localhost:27017",
    database_name="ghl_sessions",
    collection_name="jwt_tokens"
)

client = HighLevel(
    client_id="your_client_id",
    client_secret="your_client_secret",
    session_storage=storage
)
```

## Documentation

- [Official API Documentation](http://marketplace.gohighlevel.com/docs/)
- [SDK Examples](https://github.com/GoHighLevel/ghl-sdk-examples/tree/main/python)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.
