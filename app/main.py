from fastapi import FastAPI

import uvicorn


api = FastAPI()


@api.get('/')
def root():
    return {'message': 'Welcome to ExchangeAPI!'}


if __name__ == '__main__':
    uvicorn.run('main:api',
                host='0.0.0.0',
                port=8080,
                reload=True,
                debug=True)
