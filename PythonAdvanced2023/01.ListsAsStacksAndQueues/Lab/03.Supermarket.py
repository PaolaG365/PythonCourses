from collections import deque
customer_list = deque()
customer_name = input()
while customer_name != "End":
    if customer_name == "Paid":
        while customer_list:
            print(customer_list.popleft())
    else:
        customer_list.append(customer_name)
    customer_name = input()
print(f"{len(customer_list)} people remaining.")
