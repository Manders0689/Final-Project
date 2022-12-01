def mystery(text):
    stack = []
    for letter in text:
        stack.append(letter)
        
    result = ""
    while len(stack) > 0:
        result += stack.pop()
        
    return result

print(mystery("racecar"))
print(mystery("stressed"))
print(mystery("a nut for a jar of tuna"))