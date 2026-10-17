from pydantic_settings import BaseSettings, SettingsConfigDict


class LiveKitSettings(BaseSettings):
	LIVEKIT_URL: str
	LIVEKIT_API_KEY: str
	LIVEKIT_API_SECRET: str
	LIVEKIT_ACCESS_TOKEN_EXPIRE: int = 20
	
	model_config = SettingsConfigDict(env_file=".env")
