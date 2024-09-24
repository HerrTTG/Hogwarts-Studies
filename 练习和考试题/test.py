def abc(i):
    match i:
        case "test":
            print("OK")
        case _:
            print("wrong")


abc("test")
abc(123123)
