from tkinter import *
import requests
from bs4 import BeautifulSoup

my_screen = Tk()
foundLinks = []

FONT = ("Times New Roman", 18, "normal")

my_screen.title("Any App")
my_screen.minsize(width=600, height=600)


def get_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def crawl(url):
    links = get_url(url)
    for link in links.find_all('a'):
        found_link = link.get('href')

        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0]
            if my_new_url in found_link and found_link not in foundLinks:
                foundLinks.append(found_link)
                text_box.insert(END, found_link + "\n")  # Bağlantıyı metin kutusuna ekle
                # recursive
                crawl(found_link)


# Main text
label_main = Label(text="Car Shop", font=FONT)
label_main.pack()

# Entry
url_entry = Entry(width=60)
url_entry.pack()


def enter_url():
    global my_new_url
    my_new_url = "https://www." + url_entry.get() + ".com"
    crawl(my_new_url)


# Enter URL button
url_enter_button = Button(text="Enter URL", width=20, command=enter_url)
url_enter_button.pack()

# Textbox
text_box = Text(width=60, height=20, wrap=WORD)
text_box.pack()

my_screen.mainloop()