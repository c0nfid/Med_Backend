from pydantic import BaseModel, conint, HttpUrl


class ItemBase(BaseModel):
    id: conint(ge=1)
    name: str
    amount: conint(ge=0)
    guide: HttpUrl
    type: str
