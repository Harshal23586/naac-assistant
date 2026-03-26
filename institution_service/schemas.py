from pydantic import BaseModel

class ProfileBase(BaseModel):
    name: str
    establishment_year: int
    university_type: str

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    class Config:
        orm_mode = True

