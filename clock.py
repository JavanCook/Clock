import random
import tkinter as tk
from PIL import Image 
from PIL import ImageTk

def hello():
    print('hello there')
    
tkint = tk.Tk()
    
canvas = tk.Canvas(tkint, width=800, height=800)
canvas.pack()    

btn = tk.Button(tkint, text="click me", command=hello)
btn.pack()

#Image import and card dimensions
cardimages = Image.open("classic-playing-cards.jpg")
cardx=73
cardy=98

#suit y-postions
heart_top=2
heart_bottom=3
diamond_top=3
diamond_bottom=4
club_top=0
club_bottom=1
spade_top=1
spade_bottom=2

#value x-positions
ace_left=0
ace_right=1
two_left=1
two_right=2
three_left=2
three_right=3
four_left=3
four_right=4
five_left=4
five_right=5
six_left=5
six_right=6
seven_left=6
seven_right=7
eight_left=7
eight_right=8
nine_left=8
nine_right=9
ten_left=9
ten_right=10
jack_left=10
jack_right=11
queen_left=11
queen_right=12
king_left=12
king_right=13

#hearts
aceheart=cardimages.crop((ace_left*cardx,heart_top*cardy,ace_right*cardx,heart_bottom*cardy))
twoheart=cardimages.crop((two_left*cardx,heart_top*cardy,two_right*cardx,heart_bottom*cardy))
threeheart=cardimages.crop((three_left*cardx,heart_top*cardy,three_right*cardx,heart_bottom*cardy))
fourheart=cardimages.crop((four_left*cardx,heart_top*cardy,four_right*cardx,heart_bottom*cardy))
fiveheart=cardimages.crop((five_left*cardx,heart_top*cardy,five_right*cardx,heart_bottom*cardy))
sixheart=cardimages.crop((six_left*cardx,heart_top*cardy,six_right*cardx,heart_bottom*cardy))
sevenheart=cardimages.crop((seven_left*cardx,heart_top*cardy,seven_right*cardx,heart_bottom*cardy))
eightheart=cardimages.crop((eight_left*cardx,heart_top*cardy,eight_right*cardx,heart_bottom*cardy))
nineheart=cardimages.crop((nine_left*cardx,heart_top*cardy,nine_right*cardx,heart_bottom*cardy))
tenheart=cardimages.crop((ten_left*cardx,heart_top*cardy,ten_right*cardx,heart_bottom*cardy))
jackheart=cardimages.crop((jack_left*cardx,heart_top*cardy,jack_right*cardx,heart_bottom*cardy))
queenheart=cardimages.crop((queen_left*cardx,heart_top*cardy,queen_right*cardx,heart_bottom*cardy))
kingheart=cardimages.crop((king_left*cardx,heart_top*cardy,king_right*cardx,heart_bottom*cardy))

#diamonds
acediamond=cardimages.crop((ace_left*cardx,diamond_top*cardy,ace_right*cardx,diamond_bottom*cardy))
twodiamond=cardimages.crop((two_left*cardx,diamond_top*cardy,two_right*cardx,diamond_bottom*cardy))
threediamond=cardimages.crop((three_left*cardx,diamond_top*cardy,three_right*cardx,diamond_bottom*cardy))
fourdiamond=cardimages.crop((four_left*cardx,diamond_top*cardy,four_right*cardx,diamond_bottom*cardy))
fivediamond=cardimages.crop((five_left*cardx,diamond_top*cardy,five_right*cardx,diamond_bottom*cardy))
sixdiamond=cardimages.crop((six_left*cardx,diamond_top*cardy,six_right*cardx,diamond_bottom*cardy))
sevendiamond=cardimages.crop((seven_left*cardx,diamond_top*cardy,seven_right*cardx,diamond_bottom*cardy))
eightdiamond=cardimages.crop((eight_left*cardx,diamond_top*cardy,eight_right*cardx,diamond_bottom*cardy))
ninediamond=cardimages.crop((nine_left*cardx,diamond_top*cardy,nine_right*cardx,diamond_bottom*cardy))
tendiamond=cardimages.crop((ten_left*cardx,diamond_top*cardy,ten_right*cardx,diamond_bottom*cardy))
jackdiamond=cardimages.crop((jack_left*cardx,diamond_top*cardy,jack_right*cardx,diamond_bottom*cardy))
queendiamond=cardimages.crop((queen_left*cardx,diamond_top*cardy,queen_right*cardx,diamond_bottom*cardy))
kingdiamond=cardimages.crop((king_left*cardx,diamond_top*cardy,king_right*cardx,diamond_bottom*cardy))

#clubs
aceclub=cardimages.crop((ace_left*cardx,club_top*cardy,ace_right*cardx,club_bottom*cardy))
twoclub=cardimages.crop((two_left*cardx,club_top*cardy,two_right*cardx,club_bottom*cardy))
threeclub=cardimages.crop((three_left*cardx,club_top*cardy,three_right*cardx,club_bottom*cardy))
fourclub=cardimages.crop((four_left*cardx,club_top*cardy,four_right*cardx,club_bottom*cardy))
fiveclub=cardimages.crop((five_left*cardx,club_top*cardy,five_right*cardx,club_bottom*cardy))
sixclub=cardimages.crop((six_left*cardx,club_top*cardy,six_right*cardx,club_bottom*cardy))
sevenclub=cardimages.crop((seven_left*cardx,club_top*cardy,seven_right*cardx,club_bottom*cardy))
eightclub=cardimages.crop((eight_left*cardx,club_top*cardy,eight_right*cardx,club_bottom*cardy))
nineclub=cardimages.crop((nine_left*cardx,club_top*cardy,nine_right*cardx,club_bottom*cardy))
tenclub=cardimages.crop((ten_left*cardx,club_top*cardy,ten_right*cardx,club_bottom*cardy))
jackclub=cardimages.crop((jack_left*cardx,club_top*cardy,jack_right*cardx,club_bottom*cardy))
queenclub=cardimages.crop((queen_left*cardx,club_top*cardy,queen_right*cardx,club_bottom*cardy))
kingclub=cardimages.crop((king_left*cardx,club_top*cardy,king_right*cardx,club_bottom*cardy))

#spades
acespade=cardimages.crop((ace_left*cardx,spade_top*cardy,ace_right*cardx,spade_bottom*cardy))
twospade=cardimages.crop((two_left*cardx,spade_top*cardy,two_right*cardx,spade_bottom*cardy))
threespade=cardimages.crop((three_left*cardx,spade_top*cardy,three_right*cardx,spade_bottom*cardy))
fourspade=cardimages.crop((four_left*cardx,spade_top*cardy,four_right*cardx,spade_bottom*cardy))
fivespade=cardimages.crop((five_left*cardx,spade_top*cardy,five_right*cardx,spade_bottom*cardy))
sixspade=cardimages.crop((six_left*cardx,spade_top*cardy,six_right*cardx,spade_bottom*cardy))
sevenspade=cardimages.crop((seven_left*cardx,spade_top*cardy,seven_right*cardx,spade_bottom*cardy))
eightspade=cardimages.crop((eight_left*cardx,spade_top*cardy,eight_right*cardx,spade_bottom*cardy))
ninespade=cardimages.crop((nine_left*cardx,spade_top*cardy,nine_right*cardx,spade_bottom*cardy))
tenspade=cardimages.crop((ten_left*cardx,spade_top*cardy,ten_right*cardx,spade_bottom*cardy))
jackspade=cardimages.crop((jack_left*cardx,spade_top*cardy,jack_right*cardx,spade_bottom*cardy))
queenspade=cardimages.crop((queen_left*cardx,spade_top*cardy,queen_right*cardx,spade_bottom*cardy))
kingspade=cardimages.crop((king_left*cardx,spade_top*cardy,king_right*cardx,spade_bottom*cardy))

#define deck
deck=[aceheart, twoheart, threeheart, fourheart, fiveheart, sixheart, sevenheart, eightheart, nineheart, tenheart, jackheart, queenheart, kingheart, acediamond, twodiamond, threediamond, fourdiamond, fivediamond, sixdiamond, sevendiamond, eightdiamond, ninediamond, tendiamond, jackdiamond, queendiamond, kingdiamond, aceclub, twoclub, threeclub, fourclub, fiveclub, sixclub, sevenclub, eightclub, nineclub, tenclub, jackclub, queenclub, kingclub,acespade, twospade, threespade, fourspade, fivespade, sixspade, sevenspade, eightspade, ninespade, tenspade, jackspade, queenspade, kingspade]

#shuffle the deck
shuffled_deck=random.sample(deck, len(deck))

#img=ImageTk.PhotoImage(image=acespade)
#canvas.create_image(0, 0, anchor=tk.NW, image=(img))

canvas.create_image(0, 0, anchor=tk.NW, image=(ImageTk.PhotoImage(image=acespade)))
#ImageTk.PhotoImage(image=acespade)

tk.mainloop()

#kingspade.show()
