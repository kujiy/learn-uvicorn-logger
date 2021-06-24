import uvicorn
import logging
import os
import sys

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })

    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(sys.stdout)                 # <-----------------------
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.info('info-test')

if __name__ == "__main__":
    uvicorn.run(f"{os.path.basename(__file__).removesuffix('.py')}:app", host="127.0.0.1", port=5000, reload=True, log_level="info")
