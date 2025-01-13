# gpu-comparison-tool

Multi-cloud GPU comparison tool that is transparent, modular and environmentally conscious.

## Overview

The GPU Comparison Tool simplifies the process of comparing GPU options available from popular cloud providers. It gathers information about GPU availability, pricing, and specifications, allowing developers and researchers to choose the best options for their workloads.

## Install 

## Set up credentials

In order to query the cloud platforms APIs without manual intervention you need to set up your authentication. Following each of the sections add your credentials to the .env file.

### GCP

To be able to query the Compute Engine API and follow best security pratices you need to create a service account. Your application will call Google APIs on behalf of the service account generating an OAuth2 token.

In the Google Cloud Console go to IAM & Admin then Service Accounts and then create a service account. Assign the role Compute Viewer to grant read access to Compute Engine resources. Download the JSON key for the service account and store it in the credentials folder. Add to a .env file:

- export GCP_SERVICE_ACCOUNT_FILE = "../credentials/{service_account}.json"
- export GCP_PROJECT_ID = "{gcp_project_id}"

The GCP API that we will query are:

- Cloud Billing API: Fetch SKU (Stock Keeping Units) that has information regarding GPU prices

- Compute Engine: Fetch available for every regions