# gpu-comparison-tool

Multi-cloud GPU comparison tool that is transparent, modular, environmentally conscious and energy aware.

## Overview

The gpu-comparison-tool brings together information from different cloud providers and aggreates different metrics.

## Installation tutorial

## Environment set up

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