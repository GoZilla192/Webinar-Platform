from pydantic_settings import BaseSettings, SettingsConfigDict


class JWTSettings(BaseSettings):
	SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
	ALGORITHM: str = "HS256"
	ACCESS_TOKEN_EXPIRE_MINUTES: int = 300
	

class PostgresqlServerSettings(BaseSettings):
	HOST: str
	PORT: int
	DB_NAME: str
	USER: str
	PASSWORD: str
	
	DRIVER: str = "postgresql+asyncpg"
	
	model_config = SettingsConfigDict(env_file=".env")
	
	@property
	def url_db(self):
		return (f"{self.DRIVER}://{self.USER}:"
		        f"{self.PASSWORD}@{self.DB_HOST}:"
		        f"{self.DB_PORT}/{self.DB_NAME}")
