from fastapi import Depends

from app.livekit.service import LiveKitService
from app.livekit.settings import LiveKitSettings


def get_livekit_settings() -> LiveKitSettings:
	"""
	For FastAPI Dependency Injection mechanism
	If I will change LiveKitSetting, I will change this function only
	"""
	return LiveKitSettings()


def get_livekit_service(
		settings: LiveKitSettings = Depends(get_livekit_settings)
) -> LiveKitService:
	return LiveKitService(settings=settings)
