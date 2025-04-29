import requests
import pandas as pd
import os

# Configuration
csv_file = "emaillist.csv"
client_id = os.environ.get('M365_CLIENT_ID')  # Set this env variable
tenant_id = os.environ.get('M365_TENANT_ID')  # Set this env variable
client_secret = os.environ.get('M365_CLIENT_SECRET')  # Set this env variable
from_email = os.environ.get('M365_SENDER_EMAIL')  # Set this env variable
html_file = "email_body.html"

# Email content
subject = "put your email subject here"
html_file = "email_body.html"  # HTML email content file

# Read the HTML content
with open(html_file, "r") as file:
    html_body = file.read()

# Obtain an access token
def get_access_token():
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": client_id,
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    response = requests.post(url, headers=headers, data=data)
    ...