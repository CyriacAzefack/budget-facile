from fastapi import FastAPI, Request, Response

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
async def webhook_handler(request: Request, response: Response):
    """
    Handle Webhook

    Args:
        request (Request): _description_
        response (Response): _description_

    Returns:
        _type_: _description_
    """
    params = dict(request.query_params)

    if "error" in params:
        # Handle Error in the Webhook handler
        return f"Error : {params['error']}"

    return f"Parameters : {params}"
