import asyncio

from fastapi import FastAPI, Response, status
from hypercorn.asyncio import serve
from hypercorn.config import Config


app = FastAPI(docs_url="/")


@app.get("/healthz")
def health_check():
    return Response(status_code=status.HTTP_200_OK)

def start(host, port):
    config = Config()
    config.bind = [host + ":" + str(port)]

    import threading

    thread = threading.Thread(group=None)
    thread.start()

    asyncio.run(serve(app, config))

start("localhost", 9095)
