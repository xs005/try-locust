import logging

import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

# Set the logging level to WARNING
logging.basicConfig(level=logging.WARNING)

# Set the timeout values
timeout_keep_alive = 100


@app.post("/payload_length")
async def payload_length(payload: Request):
    payload = await payload.json()
    return len(str(payload))


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=timeout_keep_alive)
