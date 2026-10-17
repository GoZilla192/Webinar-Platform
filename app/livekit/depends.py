from app.livekit.service import LiveKitService


def get_livekit_service() -> LiveKitService:
	return LiveKitService()
