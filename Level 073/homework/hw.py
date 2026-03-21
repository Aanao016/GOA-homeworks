# 1
def string_clean(s):
    for i in "0123456789":
        s = s.replace(i , "")
    return s

# 2
def reverse(st):
    words = st.split()
    words = words[::-1]
    return " ".join(words)
# 3
def quote(fighter):
    fighter = fighter.lower()
    
    if fighter == "george saint pierre":
        return "I am not impressed by your performance."
    else:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
# 4
def replace_exclamation(st):
    vowels = 'aeiouAEIOU'
    for i in vowels:
        st = st.replace(i , '!')
    return st
# 5
def stringy(size):
    result = ''
    for i in range(size):
        if i % 2 == 0:
            result += '1'
        else:
            result += '0'
    return result

