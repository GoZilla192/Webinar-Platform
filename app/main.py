from fastapi import FastAPI

from app.routers.livekit import router as livekit_router


app = FastAPI()
app.include_router(livekit_router)
