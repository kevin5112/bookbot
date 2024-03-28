def main():
  book_path = "./books/frankenstein.txt"
  text = get_book_text(book_path)
  wc = count_words(text)
  letterDict = count_letters(text)
  letterList = convert_to_list(letterDict)
  letterList.sort(reverse=True, key=sort_on)
  
  print_report(book_path, wc, letterList)


def print_report(book, numWords, letterList):
  print(f"--- Begin report of {book} ---")
  print(f"{numWords} words found in the document\n")
  for char in letterList:
    print(f"The '{char["letter"]} character was found {char["count"]} times")
  print("--- End report ---")

def convert_to_list(letterDict):
  letterList = []
  for c in letterDict:
    letterList.append({"letter": c, "count": letterDict[c]})
  return letterList

def sort_on(dict):
  return dict["count"]

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  return len(text.split())

def count_letters(text):
  text = text.lower()
  letterDict = {}
  for c in text:
    if c.isalpha():
      letterDict[c] = 1 + letterDict.get(c, 0)
  return letterDict


main()
