from items import ItemBase


def add_item(item_in: ItemBase):
    item = item_in.model_dump()
    return {
        "success": True,
        "item": item,
    }
