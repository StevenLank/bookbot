def get_count_words(doc):
    words = doc.split()
    return len(words) 

def count_characters(book):
    letters = {}
    lower_case = book.lower()
    for l in lower_case:
        if l not in letters:
            letters [l] = 1
        elif l in letters:
            letters [l] += 1
    return letters

def sort_characters(dic):
    sorted = []
    for key in dic:
        tdic = {"char":"", "num":""}
        tdic["char"] = key
        tdic["num"] = dic[key]
        sorted.append(tdic)
    sorted.sort(key=lambda item: item["num"], reverse=True)
    return sorted
   
