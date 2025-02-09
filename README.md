# gpu-comparison-tool

Multi-cloud GPU comparison tool that is transparent, modular, environmentally conscious and energy aware.

## Overview

The gpu-comparison-tool brings together information from different cloud providers, pre-process it and aggreates it with different metrics.

## Set up environment

In order to use this code he recommend setting up the gpu-comparison-tool environment using Conda, follow these steps:

- 1. Install Conda

- 2. Clone the repository: 
```
git clone https://github.com/your-username/gpu-comparison-tool.git
cd gpu-comparison-tool
```

- 3. Create the Conda environment and activate it:
```
conda env create -f environment.yml
conda activate gpu-comparison-tool
```


## Set up credentials

In order to query the cloud platforms APIs without manual intervention you need to set up your authentication. Following each of the sections add your credentials to the .env file.

### GCP

To be able to query the Compute Engine API and follow best security pratices you need to create a service account. Your application will call Google APIs on behalf of the service account generating an OAuth2 token.

In the Google Cloud Console go to IAM & Admin then Service Accounts and then create a service account. Assign the role Compute Viewer to grant read access to Compute Engine resources. Download the JSON key for the service account and store it in the credentials folder. Add to a .env file:

- export GCP_SERVICE_ACCOUNT_FILE = "credentials/{service_account}.json"
- export GCP_PROJECT_ID = "{gcp_project_id}"

The GCP APIs that we will query are:

- Cloud Billing API: Fetch SKU (Stock Keeping Units) that has information regarding GPU prices

- Compute Engine: Fetch available for every regions


### AWS

Enable your AWS account for all regions that you are going to query. By the default some regions are not activated. 

Open the IAM Console:
In the search bar, type IAM and select it from the results.

Add a New User:

In the IAM dashboard’s left-hand navigation, click Users, then click the Add users button.
Enter a user name (for example, MultiRegionReadOnlyUser).
Under Select AWS access type, check Programmatic access. This creates an access key and a secret access key for use with the CLI, SDKs, or APIs.
Attach Existing Managed Policies:

- export AWS_SECRET_ACCESS_KEY ="{secret_access_key}"
- export AWS_ACCESS_KEY_ID="{access_key_id}"