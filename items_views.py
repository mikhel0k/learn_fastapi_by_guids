from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/latest/")
def get_last_item():
    return {
        "last_item": {
            "id": 0,
            "name": "item_name",
        },
    }


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(..., ge=1, lt=1_000_000)]):
    return {
        "item_id": item_id,
    }


@router.get("/")
def list_items():
    return [
        "Item 1",
        "Item 2",
        "Item 3",
    ]
