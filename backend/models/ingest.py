import pydantic


class UIDModel(pydantic.BaseModel):
    uid: str
