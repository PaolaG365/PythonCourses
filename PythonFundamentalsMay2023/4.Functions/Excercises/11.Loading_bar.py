def loading_bar(n):
    loaded = n // 10
    if loaded == 10:
        print("100% Complete!\n[%%%%%%%%%%]")
    else:
        print(f"{n}% [{'%' * loaded}{'.' * (10 - loaded)}]")
        print("Still loading...")


percent_loaded = int(input())
loading_bar(percent_loaded)
