from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Enum

from app.models.base import BaseModel
from app.models.roles import UserRole


class UserModel(BaseModel):
	__tablename__ = "user"
	
	id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
	username: Mapped[str]
	full_name: Mapped[str] = mapped_column(default="Anonymous")
	password_hash: Mapped[str]
	role: Mapped[UserRole] = mapped_column(
		Enum(UserRole, name="user_role"),
		nullable=False,
		default=UserRole.guest,
		server_default=UserRole.guest.value
	)
	
	