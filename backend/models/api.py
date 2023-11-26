from typing import Literal, Union, Annotated

from pydantic import BaseModel, Field


class SuccessfulResponse(BaseModel):
    status: Literal["success"] = "success"


class ErroredResponse(BaseModel):
    status: Literal["error"] = "error"
    message: str = Field(..., description="Description on the encountered error.")


BaseStatusResponse = Annotated[
    Union[SuccessfulResponse, ErroredResponse], Field(discriminator="status")
]


class UIDEntry(BaseModel):
    uid: str
    timestamp: str = Field(..., description="ISO timestamp", example="2023-11-26T00:55:31.866943")


class UidGetResponse(SuccessfulResponse):
    uids: list[UIDEntry] = Field(..., description="List of all uid log entries in storage.")
