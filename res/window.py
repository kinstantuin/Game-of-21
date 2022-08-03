from tkinter import *
import sys

# Функция закрытия окна по нажатию на кнопку "esc"
def close(event):
    root.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing


# функция для отображения карт
def img(card):
    img = PhotoImage(file=f"cards_images/{card}")
    label = Label(frame_for_cards, image=img, bg="yellow")
    label.image_ref = img
    label.pack(side=LEFT)

# функция возвращения пути к определенной карте
# необходима для отображения конкретной карты в графическом интерфейсе
def give_path_for_card(card): 
    return

root = Tk() # главное окно 
# рамка для карт (необходима для того, чтобы карты располагались
# сверху слева)
frame_for_cards = LabelFrame(text="frame") 
frame_for_cards.pack(fill=X)
root.bind('<Escape>', close) # установка функции закрытия 
# окна при нажатии на клавишу "esc"

root.geometry("700x400")
take_card = Button(text="test", command=img)
take_card.pack(side=BOTTOM)
root.mainloop()