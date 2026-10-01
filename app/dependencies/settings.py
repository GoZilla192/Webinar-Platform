from app.core.config import PostgresqlServerSettings, JWTSettings


def get_db_settings():
	return PostgresqlServerSettings()

def get_jwt_settings():
	return JWTSettings()