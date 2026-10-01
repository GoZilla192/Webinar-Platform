from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
	full_name: str = Field(min_length=2, max_length=128)
	username: str = Field(min_length=3, max_length=32)


class UserCreateSchema(UserBaseSchema):
	password: str = Field(min_length=8, max_length=256)


class UserReadSchema(UserBaseSchema):
	id: int
	