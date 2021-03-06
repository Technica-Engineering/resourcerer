# Resourcerer - an automation tool for OneDrive

## Features

Resourcerer is a Python project that gives you an easy way of getting resources from OneDrive and other sources.

## Use cases

What we use Resourcerer for is sharing unit test and integration test resources accros projects that need it. Resources like these don't belong in artifact repositories or in GitLab/GitHub, so it makes most sense to store them on a network drive or in the cloud. Our first choice was OneDrive, since our team was already using it extensively to share all kinds of information.

### How to use this for resource sharing

1. Write a `resources.yaml` file and place it at the root of your project. For example the way we use it to get PCAPs:

    ```yaml
    test_resources:
    - "analog.pcap"

    source_folder: 'Software/resources'
    target_folder: './tests/res'
    ```

    - `source_folder` is the path within the source driver, e.g. OneDrive with your test resource files you want to point to.

    - `target_folder` is the path to a target directory where resources should be downloaded. It's relative with respect to the root of the project folder (for predictable behavior with CI tools).

    - `test_resources` is a list of filenames (with file extensions) that should be fetched for this particular repository. It's important to explicitly specify which files are required, because the application always checks whether a resource exists before downloading it. We don't want to re-download hundreds of megabytes of files if we already have them stored.

2. For OneDrive: in your environment (or in your CI pipeline), specify the following environment variables:

    - `MSGRAPH_API_KEY` -> Secret for the Azure the application of choice (see `portal.azure.com`), you can also set it as a credential `MSGraphApiKey`, e.g. using Python's `keyring` package.
    - `MSGRAPH_CLIENT_ID` -> Client ID for the application of choice
    - `MSGRAPH_TENANT_ID` -> Azure Tenant ID
    - `MSGRAPH_SITE_ID` -> Site ID for your OneDrive or SharePoint

3. Run the `get_resources` script in your CI pipeline or anytime you want to download test resources. This Python package installs an executable script that should be available from within an environment in which it was installed.

    So for example in `.gitlab-ci.yml`:

    ```yaml
    variables:
      # connection to OneDrive:
      MSGRAPH_CLIENT_ID: "<client-id>"
      MSGRAPH_TENANT_ID: "<tenant-id>"
      MSGRAPH_SITE_ID: "<site-id>"

    before_script:
      - pip install resourcerer
      - get_resources
    ```

    The `get_resources` script will notify you whenever a file was encountered that was already there and it will also give you info on what files were specifically downloaded for easy debugging.

### Importable functions

You may of course decide to use this within your own Python app somewhere. In such case, we export two main functions that can be used:

- `download_file` -> takes in a target path (with filename) and a URL, downloads from a publicly accessible location.
- `download_from_onedrive` -> takes in a source path to a given file from OneDrive and a target path (without filename) to where the file should be downloaded. This function does not rename the downloaded resource.

There is also a protected function `_download_from_onedrive` which can be used with custom OAuth2 token and custom `site_id` if you need this.
