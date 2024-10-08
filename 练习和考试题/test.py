def func(record: dict) -> list:
    match record:
        case {"type": 'book', "api": 2, "authors": [*name]}:
            return name  # 解析类型出满足type api 且author 映射为一个序列。返回满足条件的所有序列。
        case {"type": 'book', "api": 1, "authors": name}:
            return [name]  # author 映射为任意对象，且返回由这些对象组成的序列
        case {"type": 'book'}:
            raise ValueError(f"所有type book均无效，则抛出异常")
        case {"type": 'movie', "director": name}:
            return [name]
        case _:
            raise ValueError(f"均无匹配，抛出异常{record!r}")
