def mystery(text):
    stack = []
    for letter in text:
        stack.append(letter)
        
    result = ""
    while len(stack) > 0:
        result += stack.pop()
        
    return result

print(mystery("kayak"))
print(mystery("reward"))
print(mystery("mr owl at my metal worm"))