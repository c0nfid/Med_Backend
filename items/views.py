from typing import Annotated

from fastapi import APIRouter, Path

from items import ItemBase
from items import crud

router = APIRouter(prefix="/api/items", tags=["Items"])


@router.post("/")
def add_new_item(item: ItemBase):
    return crud.add_item(item_in=item)


@router.get("/")
def get_list_items():
    return [
        "items",
        "items",
    ]


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {
        "item": {
            "id": item_id,
        }
    }


@router.get("/{item_name}/")
def get_item_by_name(item_name: str):
    return {
        "item": {
            "id": item_name,
        }
    }


@router.get("/run_low/")
def get_run_low_items():
    return {
        "item": "123",
    }
