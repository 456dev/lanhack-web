from typing import Literal, Union, Annotated

from pydantic import BaseModel, Field, ValidationError

class Success(BaseModel):
    status: Literal['success']


class Error(BaseModel):
    status: Literal['error']
    message: str


Status = Annotated[Union[Success, Error], Field(discriminator='status')]


