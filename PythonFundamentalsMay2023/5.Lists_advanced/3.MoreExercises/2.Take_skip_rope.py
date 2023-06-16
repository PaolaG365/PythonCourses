message_hidden_in = input()

nums_in_message = [int(n) for n in message_hidden_in if n.isnumeric()]
symbols_in_message = [s for s in message_hidden_in if not s.isnumeric()]

hidden_message = []
index = 0

for num in range(len(nums_in_message)):
    if num % 2 == 0:
        if nums_in_message[num] > 0:
            hidden_message = hidden_message + symbols_in_message[index:index+nums_in_message[num]]
            index += nums_in_message[num]
    else:
        index += nums_in_message[num]

print("".join(hidden_message))
