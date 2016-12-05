from twitter import *
from tkinter import *


def showTweets(x, num):
    # display a number of new tweets and usernames
    for i in range(0, num):line1 = (x[i]['user']['screen_name'])
    line2 = (x[i]['text'])
    w = Label(master, text=line1 + "\n" + line2 + "\n\n")
    w.pack()


def getTweets():
    x = t.statuses.home_timeline(screen_name="RobertWilliamsJr")
    return x


def tweet():
    global entryWidget

    if entryWidget.get().strip() == "":
        print("Empty")
    else:
        t.statuses.update(status=entryWidget.get().strip())
        entryWidget.delete(0, END)
        print("working")


# Put in token, token_key, con_secret, con_secret_key
t = Twitter(
    auth=OAuth('805338356326563841-qrbTYHwhSyUY5HFiJ4IzTn4fostBgFz', 'qGDgTnRhce89hLrDdaQKa8Voeigu85kPA22VzAAgYgbuf',
               'ZlmrsEGVpvCU21Jk9YRQxA45p', '9wxvAq4MpV4eRCcsqhpfmGMpMQOKrSqxN2NZ36VuQ1LikvGOKB'))

numberOfTweets = 10

master = Tk()
showTweets(getTweets(), numberOfTweets)

master.title("Tkinter Entry Widget")
master["padx"] = 40
master["pady"] = 20
# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(master)
# Create a Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Make a new Tweet:"
entryLabel.pack(side=LEFT)
# Create an Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()
button = Button(master, text="Submit", command=tweet)
button.pack()

master.mainloop()

