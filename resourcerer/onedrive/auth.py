import requests
from resourcerer.utils import response_content_to_dict, try_from_response
from resourcerer.onedrive.model import ApiToken, ClientId, TenantId


def auth_token(client_id: ClientId, tenant_id: TenantId, api_token: ApiToken):
    """Gets MS Graph authentication token from
    OAuth2 authority server.

    Args:
        `client_id` (:obj:`str`): Client ID of the application
            (available in Azure Portal, where you registered
            your application).
        `tenant_id` (:obj:`str`): Tenant ID, unique identifier
            of MS Graph tenancy, can be found in Azure portal
            as well.

    Returns:
        Token string.
    """

    token_request_payload = {
        "client_id": client_id,
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": api_token,
        "grant_type": "client_credentials"
    }

    token_request_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    resp = requests.post(token_request_url, data=token_request_payload)
    resp = response_content_to_dict(resp)

    token = None

    token = try_from_response(resp, 'access_token',
                              "Failed to obtain access token from MS Graph OAuth endpoint.")
    return token
