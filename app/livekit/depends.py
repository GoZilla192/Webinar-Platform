from fastapi import Depends

from app.livekit.service import LiveKitService
from app.livekit.settings import LiveKitSettings


def get_livekit_settings() -> LiveKitSettings:
	return LiveKitSettings()


def get_livekit_service(
		settings: LiveKitSettings = Depends(get_livekit_settings)
) -> LiveKitService:
	return LiveKitService(settings=settings)
