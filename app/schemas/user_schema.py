from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    age: int
    phone: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    age: int
    phone: str

    class Config:
        orm_mode = True
