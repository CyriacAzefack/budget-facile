from typing import Optional

import requests
from fastapi import FastAPI

app = FastAPI()


secret = "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw"


@app.get("")
def welcome():
    """
    Welcome

    Returns:
        _type_: _description_
    """
    return {"message": "Welcome to the BudgetFacile webhook handler!"}


@app.get("/webhook/")
async def webhook_handler(
    error: Optional[str] = None,
    error_description: Optional[str] = None,
    connection_id: Optional[int] = None,
    code: Optional[str] = None,
):
    """
    Handle Webhook

    Args:
        request (Request): _description_
        response (Response): _description_

    Returns:
        _type_: _description_
    """

    if error:
        # Handle Error in the Webhook handler
        return f"Error : {error}"

    domain = "facilebudget-sandbox"
    client_id = "11546070"
    client_secret = "r2I5XHd3v5wW4oEcMYI2ob1jeok63M1W"
    uri = f"https://{domain}.biapi.pro/2.0/auth/token/access"

    print("Temporary Access token granted!!")

    print("Now Fetching permanent token...")
    response =  requests.post(
        uri,
        data={
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )
    
    # Check the status code and process the response
    if response.status_code == 200:
        data = response.json()
        
        permanent_access_token = data["access_token"]
        permanent_access_token = "SUiq/Qs6vuqpMdNF0kdhq1exunlnlaS1ORbg0Dn9RQs_wleQ0/NXUZEJZ_jn1wpCznXW8QrXr0HV8s3wV/WzLH8mL1huaRWodCT/P598IXqsTsj/4f51bVZ9j6VV8nhH"
    
        print("Permanent Access Token retrieved successfully: " + permanent_access_token)
        # TODO Save the access token
        
        return data
    else:
        return f"Error fetching Permanent Access token : STATUS.{response.status_code}"
