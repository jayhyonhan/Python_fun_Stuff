import webbrowser

def open(link):
    webbrowser.open(link, 1)

def search(search_string):
    open("https://google.com/search?q="+search_string)

def map(loc):
    open(("https://www.google.com/maps/search/%s/"%loc))

def gmail():
    user = input("user(in int):  ")
    open("https://mail.google.com/mail/u/%s/#inbox?compose=new"%user)