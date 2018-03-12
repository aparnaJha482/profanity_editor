def edit_file():
    quotes = open("text_file/file.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()

def check_profanity(text_to_check):
    urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)







edit_file()