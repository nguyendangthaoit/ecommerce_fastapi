from pydantic import BaseModel, EmailStr, field_validator


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    age: int
    phone: str

    @field_validator("age")
    def check_age(cls, v):
        if v < 0:
            raise ValueError("Age must be positive")
        return v

    @field_validator("phone")
    def check_phone(cls, v):
        if len(v) < 8:
            raise ValueError("Phone too short")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    age: int
    phone: str

    class Config:
        from_attributes = True
