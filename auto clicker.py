from tkinter import * # built into python
import pyautogui # may need to download this on it's own

# some globals to make things easier
app = Tk()
mouseX = 0
mouseY = 1
clickAmount = 0


# create gui for the user
def window():

    global clickAmount

    noticeLabel = Label(app, text="make sure to double click\n where you want the mouse to be\n")
    noticeLabel.grid(row=0, columnspan=2, padx=10)

    button1 = Button(app, text="click here to choose location", command=userChooseLocation)
    button1.grid(row=10, columnspan=2, padx=30)

    amountClicksLabel = Label(app, text="enter the amount of clicks you want")
    amountClicksLabel.grid(row=30, columnspan=2, pady=10)

    clickAmount = clickEntry = Entry(app, text="enter how many clicks you want")
    clickEntry.grid(row=40, columnspan=2)

    button2 = Button(app, text="click to start", command=startTheThing)
    button2.grid(row=50,columnspan=2, pady=30)


# starts left mouse click for a specified amount of times, can't move the mouse in the meantime
def startTheThing():
    global clickAmount
    clicks = int(clickAmount.get())

    # make sure the user wants to click a valid amount before loop
    if(clicks >= 1):
        app.iconify()
        for i in range(clicks):
            pyautogui.click(mouseX, mouseY)
        app.deiconify()


# lets user click on the location they want
def userChooseLocation():
    # finds position relative to the window so we need to make it fullscreen during this time
    app.wm_attributes("-fullscreen", True)
    # then we make it see through so user can see where they want to click
    app.attributes("-alpha",0.01)
    app.bind("<Double-Button-1>", userClick)


# sets the position of the pointer when the user double clicks on the position
def userClick(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
    app.attributes("-alpha", 1.0)
    app.wm_attributes("-fullscreen", False)



# run application
def main():
    window()
    app.mainloop()


if __name__ == "__main__":
    main()