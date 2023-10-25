from collections import deque

ramen_bowls_value = deque(int(x) for x in input().split(", "))
customers_value = deque(int(x) for x in input().split(", "))

while ramen_bowls_value and customers_value:
    served_ramen = ramen_bowls_value.pop()
    current_customer = customers_value.popleft()
    if served_ramen > current_customer:
        ramen_bowls_value.append(served_ramen - current_customer)
    elif served_ramen < current_customer:
        customers_value.appendleft(current_customer - served_ramen)

if customers_value:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers_value)}")
else:
    print("Great job! You served all the customers.")
    if ramen_bowls_value:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen_bowls_value)}")
