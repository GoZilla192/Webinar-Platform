from pydantic import BaseModel


class LiveKitTokenRequestSchema(BaseModel):
	room_name: str
	is_host: bool
	name: str
	identity: str
