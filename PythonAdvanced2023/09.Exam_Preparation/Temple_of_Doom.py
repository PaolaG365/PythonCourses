# huehue
from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = deque(int(x) for x in input().split())


def final_print(**kwargs):
    final_result = []
    for sequence, value in kwargs.items():
        if value:
            final_result.append(f"{sequence}: {', '.join(str(x) for x in value)}")
    return "\n".join(final_result)


while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance

    if result in challenges:
        challenges.remove(result)
    else:
        tool += 1
        substance -= 1
        tools.append(tool)
        if substance > 0:
            substances.append(substance)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if (not tools or not substances) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

print(final_print(Tools=tools, Substances=substances, Challenges=challenges))
