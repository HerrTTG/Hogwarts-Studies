dial_code = [("country", 'Tokoy'), ("remark", 321)]

new = {i: j for i, j in dial_code}


def abc(record: dict) -> list:
    ls = []
    match record:
        case {"country": "Tokoy", **details} as T if len(details) > 0:
            for i, j in enumerate(T):
                ls.append((i, j))
            return ls
        case _:
            print("wrong")


print(abc(new))
