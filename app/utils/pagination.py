def paginate(items:list, skip:int, limit:int):
    return items[skip: skip + limit]