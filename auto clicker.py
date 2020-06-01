import time
from tkinter import * # built into python
import pyautogui # may need to download this on it's own

class Click:

    def __init__(self, x, y, amount, delay):
        self.mouseX = x
        self.mouseY = y
        self.clickAmount = amount
        self.clickDelay = delay



# some globals to make things easier
app = Tk()
mouseX = 0
mouseY = 1
clickAmount = 0
clickDelay = 0
loopDelay = 0
clickLocations = []
actions = 0
clickIterations = 1

mainwindow = Frame(app)
optionswindow = Frame(app)
testwindow = Frame(app)

def raiseFrame(frame: Frame):
    frame.tkraise()
    # frame.focus()

def test(frame: Frame):
    print("test valuie")
    global testwindow

    frame.grid()

    btt = Button(frame, text="hello", command=goToMainWindow).pack()

def goToMainWindow():
    global mainwindow
    mainWindow(mainwindow)

def onLoopDelayEnter():
    print("in loop delay enter")


# create gui for the user
def mainWindow(frame: Frame):

    global clickAmount
    global mainwindow
    global loopDelay
    global clickIterations


    noticeLabel = Label(frame, text="make sure to double click\n where you want the mouse to be\n")
    noticeLabel.grid(row=0, columnspan=2, padx=10)

    optionsButton = Button(frame, text="click here to add location", command=goToOptionsWindow)
    optionsButton.grid(row=10, columnspan=2, padx=30)

    amountClicksLabel = Label(frame, text="enter the amount of interations you want")
    amountClicksLabel.grid(row=30, columnspan=2, pady=10)

    clickIterations = clickAmountEntry = Entry(frame, text="")
    clickAmountEntry.grid(row=40, columnspan=2)

    loopDelayLabel = Label(frame, text="add delay after loop\n (default is 0 seconds)")
    loopDelayLabel.grid(row=50, columnspan=2)

    loopDelay = loopEntry = Entry(frame, text="")
    loopEntry.grid(row=60, columnspan=2)

    startButton = Button(frame, text="click to start", command=startTheThing)
    startButton.grid(row=70, columnspan=2, pady=30)

    clearButton = Button(frame, text="click to clear cache", command=clearClicks)
    clearButton.grid(row=80, columnspan=2, pady= 10)

    raiseFrame(mainwindow)


def goToOptionsWindow():
    global optionswindow
    optionsWindow(optionswindow)


def optionsWindow(frame: Frame):
    print("making options window")
    global clickAmount
    global clickDelay


    noticeLabel = Label(frame, text="make sure to double click\n where you want the mouse to be\n")
    noticeLabel.grid(row=0, columnspan=2, padx=10)

    button1 = Button(frame, text="click here to add location", command=userChooseLocation)
    button1.grid(row=10, columnspan=2, padx=30)

    amountClicksLabel = Label(frame, text="enter the amount of clicks you want")
    amountClicksLabel.grid(row=30, columnspan=2, pady=10)

    clickAmount = clickEntry = Entry(frame, text="enter how many clicks you want")
    clickEntry.grid(row=40, columnspan=2)

    clickDelayLabel = Label(frame, text="add delay after click\n (default is 0 seconds)")
    clickDelayLabel.grid(row=50, columnspan=2)

    clickDelay = delayclickEntry = Entry(frame, text="add delay after click\n (default is 0 seconds)")
    delayclickEntry.grid(row=60, columnspan=2, pady=10)

    finishButton = Button(frame, text="Add", command=AddClick)
    finishButton.grid(row=70, columnspan=2, pady= 10)

    raiseFrame(frame)

def AddClick():
    global mouseX
    global mouseY
    global clickAmount
    global clickDelay

    localCLickAmount = 0
    localClickDelay = 0

    print("adding click")
    if(isinstance(mouseX, int)):
        print("mouseX: " + str(mouseX))
    if(isinstance(mouseY, int)):
        print("mouseY: " + str(mouseY))
    if(clickAmount.get() == ""):
        localCLickAmount = 1
    else:
        localCLickAmount = int(clickAmount.get())
    if(clickDelay.get() == ""):
        # print(int(clickDelay.get()))
        localClickDelay = 0
    else:
        localClickDelay = int(clickDelay.get())

    global clickLocations
    clickLocations.append(Click(mouseX, mouseY, localCLickAmount, localClickDelay))

    for c in clickLocations:
        # print(type(c))
        print(c.clickAmount)

    global actions
    actions = len(clickLocations)

    goToMainWindow()




def clickWindow():
    print("in click window")

def clearClicks():
    print("clearning cache")
    global clickLocations
    clickLocations = []



# starts left mouse click for a specified amount of times, can't move the mouse in the meantime
def startTheThing():
    global actions
    global clickLocations
    global loopDelay
    global clickIterations
    # clicks = int(clickAmount.get())

    localLoopDelay = 0
    localIterations = 1

    if(clickIterations.get() != ""):
        localIterations = int(clickIterations.get())

    print("loop delay" + loopDelay.get())

    if(loopDelay.get() != ""):
        localLoopDelay = int(loopDelay.get())

    app.iconify()




    # make sure the user wants to click a valid amount before loop
    for i in range(localIterations):

        for click in clickLocations:
            for c in range(click.clickAmount):
                pyautogui.click(click.mouseX, click.mouseY)
                time.sleep(click.clickDelay)

        time.sleep(localLoopDelay)

    app.deiconify()


# lets user click on the location they want
def userChooseLocation():
    # finds position relative to the window so we need to make it fullscreen during this time
    app.wm_attributes("-fullscreen", True)
    # then we make it see through so user can see where they want to click
    app.attributes("-alpha",0.51)
    app.bind("<Double-Button-1>", userClick)


# sets the position of the pointer when the user double clicks on the position
def userClick(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
    app.attributes("-alpha", 1.0)
    app.wm_attributes("-fullscreen", False)
    print(mouseX, mouseY)

def setFrames():
    testwindow.grid(row=0, column=0, sticky='news')
    mainwindow.grid(row=0, column=0, sticky='news')
    optionswindow.grid(row=0, column=0, sticky='news')

# run application
def main():
    setFrames()
    # test(testwindow)
    mainWindow(mainwindow)
    # optionsWindow(optionswindow)
    raiseFrame(mainwindow)
    app.mainloop()


if __name__ == "__main__":
    main()