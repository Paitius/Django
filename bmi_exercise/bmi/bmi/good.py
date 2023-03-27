

def dec(func):
    def wrapper(funkcja):
        print("----")
        func()
        print("----")
    return wrapper


@dec
def funkcja():
    print("hello")
