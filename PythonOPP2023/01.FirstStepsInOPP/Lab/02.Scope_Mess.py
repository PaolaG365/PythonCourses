x = "global"  # global


def outer():  # enclosing
    x = "local"

    def inner():  # local
        nonlocal x  # takes from enclosing var x and changes it
        x = "nonlocal"
        print("inner:", x)

    def change_global():  # local
        global x  # takes global var x and rewrites it
        x = "global: changed!"

    print("outer:", x)  # enclosing
    inner()
    print("outer:", x)
    change_global()


print(x)  # global
outer()
print(x)
