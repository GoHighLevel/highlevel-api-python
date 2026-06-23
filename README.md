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

# Initialize with OAuth credentials
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
    
    # Step 2: Exchange code for tokens (after user authorization).
    # The request body uses camelCase keys.
    token_data = await client.oauth.get_access_token({
        "clientId": "your_client_id",
        "clientSecret": "your_client_secret",
        "grantType": "authorization_code",
        "code": "authorization_code_from_callback",
    })

    # token_data is the raw token response, with camelCase keys:
    # accessToken, refreshToken, expiresIn, userType, and locationId or companyId.
    # Persist it via your session storage to authenticate later requests.
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

## Webhook Integration

The SDK provides comprehensive webhook support for handling GoHighLevel webhook events, including automatic token management and session storage integration.

### Features

- **Automatic Token Management**: Handles `INSTALL` and `UNINSTALL` webhooks automatically
- **Token Storage**: Generates and stores access tokens on `INSTALL`, removes them on `UNINSTALL`
- **Session Management**: Integrates with your chosen session storage (Memory/MongoDB)
- **Auto Token Refresh**: Automatically refreshes expired tokens during API calls if tokens are stored

### Webhook Handler Setup

```python
from highlevel import HighLevel
from highlevel.storage import MemorySessionStorage

# Initialize the SDK client with session storage
client = HighLevel(
    client_id="your_client_id",
    client_secret="your_client_secret",
    session_storage=MemorySessionStorage()
)

# Get the webhook middleware
webhook_middleware = client.webhooks.subscribe()

@app.route('/api/webhooks/ghl', methods=['POST'])
async def handle_ghl_webhook():
    """Handle incoming GoHighLevel webhooks"""
    # Process the webhook using the middleware
    await webhook_middleware(request)
    # Add your custom webhook logic here
    return jsonify({"status": "success"}), 200
```

### Webhook Signature Verification

Incoming webhooks are verified before they are processed. Configure the public key
(available in your app settings) as an environment variable. If no supported signature
header and matching key are present, the middleware logs a warning and skips the
webhook **without processing it** — so configuring a key is required for webhooks to work.

| Scheme | Header | Environment variable | Notes |
|--------|--------|----------------------|-------|
| Ed25519 | `x-ghl-signature` | `WEBHOOK_SIGNATURE_PUBLIC_KEY` | Preferred. Used when present. |
| RSA-SHA256 | `x-wh-signature` | `WEBHOOK_PUBLIC_KEY` | Legacy fallback. |

```bash
# CLIENT_ID is also required — the webhook's appId is matched against it before processing.
export CLIENT_ID="your_client_id"
export WEBHOOK_SIGNATURE_PUBLIC_KEY="your_ed25519_public_key"
# Optional legacy fallback:
export WEBHOOK_PUBLIC_KEY="your_rsa_public_key"
```

## Documentation

- [Official API Documentation](http://marketplace.gohighlevel.com/docs/)
- [SDK Examples](https://github.com/GoHighLevel/ghl-sdk-examples/tree/main/python)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.
