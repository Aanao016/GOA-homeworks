# 1
def maskify(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]

# 2
def get_sum(a, b):
    if a == b:
        return a
    
    start = min(a, b)
    end = max(a, b)
    total = 0
    for num in range(start, end + 1):
        total += num
        
    return total

# 3
def is_isogram(string):
    string = string.lower()
    seen_letters = [] 
    
    for char in string:
        if char in seen_letters:
            return False
        seen_letters.append(char)
        
    return True 

# 4
def well(x):
    good_count = x.count('good')
    
    if good_count == 0:
        return 'Fail!'
    elif good_count <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'

# 5

# 6
def sum_digits(number):
    number = abs(number)
    
    total = 0
    for digit in str(number):
        total += int(digit) 
        
    return total
# 7
# 8
# 9
# 10

