from fastapi import APIRouter, Depends

from app.schemas.livekit import LiveKitTokenRequestSchema
from app.services.livekit import LiveKitService
from app.dependencies.livekit import get_livekit_service

router = APIRouter(tags=["LiveKit Server"])


@router.post("/get-livekit-token")
async def get_livekit_token(
		token_request: LiveKitTokenRequestSchema,
		livekit_service: LiveKitService = Depends(get_livekit_service)
):
	return livekit_service.get_token(token_request)
	
