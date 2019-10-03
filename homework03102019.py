def remove_shots(string):
    longonly = [word for word in string if len(word) > 4]
    return longonly

def detect_palindromes(some_list):                                       
    palindroms = {word: word == word[::-1] for word in some_list}        
    return palindroms

def change_case(string):
    new_string = [''.join(l.upper() if l.islower() else l.lower() for l in string)]
    return new_string


