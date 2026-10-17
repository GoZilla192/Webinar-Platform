from fastapi import FastAPI

from app.livekit.routes import router as livekit_router


app = FastAPI()
app.include_router(livekit_router)
