# FastAPI
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

# Server
import uvicorn

# Routers
from app.routers import mercado_bitcoin
from app.routers import kraken
from app.routers import cheaper


# FastAPI instance
api = FastAPI()


# Include routers
api.include_router(mercado_bitcoin.router)
api.include_router(kraken.router)
api.include_router(cheaper.router)


# Redirect root to API docs
@api.get("/")
def index_docs():
    return RedirectResponse(url="/docs")


# Run the api
if __name__ == '__main__':
    uvicorn.run('main:api',
                host='0.0.0.0',
                port=8080,
                reload=True,
                debug=True)
