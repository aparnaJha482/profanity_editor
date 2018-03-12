import urllib

def edit_file():
    quotes = open("text_file/file.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()






edit_file()