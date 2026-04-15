
def count(vowels:str)->int:
    count=0
    if vowels is None:
        raise TypeError("Input cant be none") #error if there is no vowls
    for m in vowels.lower(): #to conver text in lower case
        if  m in "aeiou":
            count+=1
    return count

print(count("aeiou"))


def reverse_string(text:str)->str:
    if text is None:
        raise TypeError("Input cant be none") #error if there is no vowls
    return text[::-1]

print(reverse_string("aeiou"))


def is_palindoram(text:str)->bool:
    if text is None:
        raise TypeError("Input cant be none") #error if there is no vowls
    cleaned = text.replace(" ", "").lower()
    return cleaned==cleaned[::-1]
    
def world_count(text:str)->int:
     if text is None:
        raise TypeError("Input cant be none") 
     return len(text.split())

print(world_count("atre tr"))


def capatilize_words(text:str)->str:
     if text is None:
        raise TypeError("Input cant be none") 
     return text.title()
print(capatilize_words("This is a string"))

def remove_duplicate(text:str)->str:
     if text is None:
        raise TypeError("Input cant be none") 
     if not text:
        return text
     result=[text[0]]
     for ch in text[1:]:
         if ch!=result[-1]:
             result.append(ch)
     return  "".join(list(result))
print(remove_duplicate("abbeei"))