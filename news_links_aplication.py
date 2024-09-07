import requests
from tkinter import *
from bs4 import BeautifulSoup

# screen 
screen = Tk()
screen.title("Weather Aplication")
screen.minsize(600,600)
screen.config(padx=20,pady=20)


FONT = ("Arial",24,"normal")


# entering label
entry_label = Label(text="Enter your website for links ",font=FONT,padx=5,pady=5)
entry_label.pack()

# entering 
link_entry = Entry(bg="light blue",width=35)
link_entry.pack()

#texting label 
texting_label = Label(text="Checkout:",font=FONT,padx=5,pady=5)
texting_label.pack()

# texting
texting = Text(width=50,height=35,bg="light blue")
texting.pack()


found_links = []

def making_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    return soup


def get_links():
    links = making_request(link_entry.get())
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0]
            if "https://" in found_link and found_link not in found_links:
                found_links.append(found_link)
                texting.insert("1.0",found_link+"\n")
                
# button
clicker = Button(text="Enter",padx=5,pady=5,command=get_links)
clicker.pack()


screen.mainloop()