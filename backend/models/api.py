from typing import Literal, Union, Annotated

from pydantic import BaseModel, Field


class Success(BaseModel):
    status: Literal['success'] = "success"


class Error(BaseModel):
    status: Literal['error'] = "error"
    message: str


Status = Annotated[Union[Success, Error], Field(discriminator='status')]


class UIDEntry(BaseModel):
    uid: str
    timestamp: str


class GetUidResponse(BaseModel):
    status: Literal['success'] = "success"
    data: list[UIDEntry]
