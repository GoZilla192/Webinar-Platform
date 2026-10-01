from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
	username: str = Field(min_length=3, max_length=32)


class UserCreateSchema(UserBaseSchema):
	password: str = Field(min_length=8, max_length=256)


class UserReadSchema(UserBaseSchema):
	id: int
	