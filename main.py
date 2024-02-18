def main():
    text=""
    with open("books/frankenstein.txt") as file:
        text=file.read()
    words=text.split()
    print(f"{len(words)} words found in the document")
    letters={"":0}
    mangled_text=""
    
    for word in words:
        mangled_text+=word.lower()
    for letter in mangled_text:
        letters[letter]=0
    for letter in mangled_text:
        letters[letter]+=1
    
    
    
    to_sort=[]

    for key in letters:
        if key.isalpha():
            to_sort.append({"char":key, "num": letters[key]})
    
    to_sort.sort(reverse=True, key=sort_on)
    for entry in to_sort:
        print(entry)

def sort_on(dict):
    return dict["num"]


    




main()