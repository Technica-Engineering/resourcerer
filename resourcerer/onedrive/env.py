import os
from logging import getLogger
from resourcerer.log import add_handlers

log = getLogger(__name__)
add_handlers(log)

SECRET = os.environ.get("MSGRAPH_API_KEY")
CLIENT_ID = os.environ.get("MSGRAPH_CLIENT_ID") or "08e33f13-a595-40d4-99f5-2ebefee0984d"
TENANT_ID = os.environ.get("MSGRAPH_TENANT_ID") or "1f04372a-6892-44e3-8f58-03845e1a70c1"
SITE_ID = os.environ.get("MSGRAPH_SITE_ID") or "5c7ce9f9-d466-437c-b0d1-ecf6e157f37b"

if SECRET is None:
    # try to fall back on `keyring` when `MSGRAPH_KEY`
    # env var is not set
    import keyring
    SECRET = keyring.get_password("MSGRAPH_API_KEY", "system")
    if SECRET is None:
        log.warn("CAUTION! Getting Secret from Credential Store Failed!")
