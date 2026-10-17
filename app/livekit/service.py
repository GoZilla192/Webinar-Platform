from livekit import api
from datetime import timedelta

from app.livekit.settings import LiveKitSettings
from app.livekit.schemas import LiveKitTokenRequestSchema

lks = LiveKitSettings()


class LiveKitService:
	def get_token(self, token_request: LiveKitTokenRequestSchema):
		grants = api.VideoGrants(
			room_join=True,
			room=token_request.room_name,
			can_publish=token_request.is_host,
			can_subscribe=True,
		)
		
		token = (
			api.AccessToken(lks.LIVEKIT_API_KEY, lks.LIVEKIT_API_SECRET)
			.with_identity(token_request.identity)
			.with_name(token_request.name)
			.with_grants(grants)
			.with_ttl(timedelta(minutes=lks.LIVEKIT_ACCESS_TOKEN_EXPIRE))
			.to_jwt()
		)
		
		return {"token": token, "url": lks.LIVEKIT_URL}
