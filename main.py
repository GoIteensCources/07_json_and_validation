from typing import Any

from fastapi import FastAPI, Query, status
from fastapi.responses import RedirectResponse, JSONResponse
from pydantic import BaseModel, Field, field_validator, model_validator

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


class Item(BaseModel):
    name: str = Field(min_length=4)
    description: str = None
    price: float
    tax: float = Field(5, description="Нaлог на item", ge=0, lt=100)
    inn: str            # number and alpha

    @field_validator("inn", )
    @classmethod
    def valid_inn(cls, v: str):
        if len(v) != 10:
            raise ValueError("len of field 'inn' must be 10")
        elif v.isalnum() is False:
            raise ValueError("field 'inn' only alnum")
        return v.upper()

    @model_validator(mode="after")
    @classmethod
    def set_description(cls, data: Any):
        if data.description == "string":
            data.description = "good description"
        return data

    @model_validator(mode="before")
    @classmethod
    def inn2_omitted(cls, data: Any):
        print(data)
        assert ("inn2" not in data), "inn2 not include in data"
        return data

@app.post("/items/")
async def create_item(item: Item, flag_save: bool = Query(True, description="set True for save")):
    item_dict: dict = item.model_dump()
    # item_json: str = item.model_dump_json()
    item_dict["price_with_tax"] = item.price + item.price*item.tax/100
    if flag_save:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item_dict)
    return JSONResponse(status_code=status.HTTP_200_OK, content=item_dict)
