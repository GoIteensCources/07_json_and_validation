from fastapi import FastAPI, Query, status
from fastapi.responses import RedirectResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.post("/items/")
async def create_item(item: Item, flag_save: bool = Query(True, description="set True for save")):
    item_dict: dict = item.model_dump()
    # item_json: str = item.model_dump_json()
    item_dict["price_with_tax"] = item.price + item.price*item.tax/100
    if flag_save:
        print("Create")
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item_dict)
    return JSONResponse(status_code=status.HTTP_200_OK, content=item_dict)
