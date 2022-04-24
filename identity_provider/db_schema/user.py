from typing import Literal
from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr, SecretStr
from identity_provider.db_schema.type_lib.field_utils import PyObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str = Field(max_length=50)
    middle_name: str | None = Field(default=None, max_length=50)
    last_name: str = Field(max_items=50)
    email: EmailStr = Field(...)
    email_verified: bool = False
    hased_password: SecretStr
    government_id: str | None
    id_issueing_government: Literal["Nepal", "China"] | None
    government_id_type: str | None
    government_id_verified: bool = False

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
