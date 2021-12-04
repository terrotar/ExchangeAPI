# FastAPI
from fastapi import FastAPI

# Server
import uvicorn

# Routers
from routers import mercado_bitcoin
from routers import kraken


# FastAPI instance
api = FastAPI()


# Include routers
api.include_router(mercado_bitcoin.router)
api.include_router(kraken.router)


# Run the api
if __name__ == '__main__':
    uvicorn.run('main:api',
                host='0.0.0.0',
                port=8080,
                reload=True,
                debug=True)
