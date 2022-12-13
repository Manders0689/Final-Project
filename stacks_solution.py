def func(text):
    stack = []
    for letter in text:
        stack.append(letter)
        
    result = ""
    while len(stack) > 0:
        result += stack.pop()
        
    return result

print(func("kayak"))
print(func("reward"))
print(func("mr owl at my metal worm"))