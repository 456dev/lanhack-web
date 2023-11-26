from typing import Literal, Union, Annotated

from pydantic import BaseModel, Field


class SuccessfulResponse(BaseModel):
    status: Literal["success"] = "success"


class ErroredResponse(BaseModel):
    status: Literal["error"] = "error"
    message: str


BaseStatusResponse = Annotated[
    Union[SuccessfulResponse, ErroredResponse], Field(discriminator="status")
]


class UIDEntry(BaseModel):
    uid: str
    timestamp: str


class GetUidResponse(SuccessfulResponse):
    uids: list[UIDEntry]
