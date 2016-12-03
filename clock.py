import random
import tkinter as tk
from PIL import Image 
from PIL import ImageTk
from time import sleep
    
tkint = tk.Tk()
    
canvas = tk.Canvas(tkint, width=800, height=800, bg='#32a245')
canvas.pack()    

#Image import and card dimensions
card_images = Image.open("classic-playing-cards.jpg")
card_back = tk.PhotoImage(file='card-back.gif')
card_x=73
card_y=98
x_stack_shift=15

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
ace_heart=ImageTk.PhotoImage(card_images.crop((ace_left*card_x,heart_top*card_y,ace_right*card_x,heart_bottom*card_y)))
two_heart=ImageTk.PhotoImage(card_images.crop((two_left*card_x,heart_top*card_y,two_right*card_x,heart_bottom*card_y)))
three_heart=ImageTk.PhotoImage(card_images.crop((three_left*card_x,heart_top*card_y,three_right*card_x,heart_bottom*card_y)))
four_heart=ImageTk.PhotoImage(card_images.crop((four_left*card_x,heart_top*card_y,four_right*card_x,heart_bottom*card_y)))
five_heart=ImageTk.PhotoImage(card_images.crop((five_left*card_x,heart_top*card_y,five_right*card_x,heart_bottom*card_y)))
six_heart=ImageTk.PhotoImage(card_images.crop((six_left*card_x,heart_top*card_y,six_right*card_x,heart_bottom*card_y)))
seven_heart=ImageTk.PhotoImage(card_images.crop((seven_left*card_x,heart_top*card_y,seven_right*card_x,heart_bottom*card_y)))
eight_heart=ImageTk.PhotoImage(card_images.crop((eight_left*card_x,heart_top*card_y,eight_right*card_x,heart_bottom*card_y)))
nine_heart=ImageTk.PhotoImage(card_images.crop((nine_left*card_x,heart_top*card_y,nine_right*card_x,heart_bottom*card_y)))
ten_heart=ImageTk.PhotoImage(card_images.crop((ten_left*card_x,heart_top*card_y,ten_right*card_x,heart_bottom*card_y)))
jack_heart=ImageTk.PhotoImage(card_images.crop((jack_left*card_x,heart_top*card_y,jack_right*card_x,heart_bottom*card_y)))
queen_heart=ImageTk.PhotoImage(card_images.crop((queen_left*card_x,heart_top*card_y,queen_right*card_x,heart_bottom*card_y)))
king_heart=ImageTk.PhotoImage(card_images.crop((king_left*card_x,heart_top*card_y,king_right*card_x,heart_bottom*card_y)))

#diamonds
ace_diamond=ImageTk.PhotoImage(card_images.crop((ace_left*card_x,diamond_top*card_y,ace_right*card_x,diamond_bottom*card_y)))
two_diamond=ImageTk.PhotoImage(card_images.crop((two_left*card_x,diamond_top*card_y,two_right*card_x,diamond_bottom*card_y)))
three_diamond=ImageTk.PhotoImage(card_images.crop((three_left*card_x,diamond_top*card_y,three_right*card_x,diamond_bottom*card_y)))
four_diamond=ImageTk.PhotoImage(card_images.crop((four_left*card_x,diamond_top*card_y,four_right*card_x,diamond_bottom*card_y)))
five_diamond=ImageTk.PhotoImage(card_images.crop((five_left*card_x,diamond_top*card_y,five_right*card_x,diamond_bottom*card_y)))
six_diamond=ImageTk.PhotoImage(card_images.crop((six_left*card_x,diamond_top*card_y,six_right*card_x,diamond_bottom*card_y)))
seven_diamond=ImageTk.PhotoImage(card_images.crop((seven_left*card_x,diamond_top*card_y,seven_right*card_x,diamond_bottom*card_y)))
eight_diamond=ImageTk.PhotoImage(card_images.crop((eight_left*card_x,diamond_top*card_y,eight_right*card_x,diamond_bottom*card_y)))
nine_diamond=ImageTk.PhotoImage(card_images.crop((nine_left*card_x,diamond_top*card_y,nine_right*card_x,diamond_bottom*card_y)))
ten_diamond=ImageTk.PhotoImage(card_images.crop((ten_left*card_x,diamond_top*card_y,ten_right*card_x,diamond_bottom*card_y)))
jack_diamond=ImageTk.PhotoImage(card_images.crop((jack_left*card_x,diamond_top*card_y,jack_right*card_x,diamond_bottom*card_y)))
queen_diamond=ImageTk.PhotoImage(card_images.crop((queen_left*card_x,diamond_top*card_y,queen_right*card_x,diamond_bottom*card_y)))
king_diamond=ImageTk.PhotoImage(card_images.crop((king_left*card_x,diamond_top*card_y,king_right*card_x,diamond_bottom*card_y)))

#clubs
ace_club=ImageTk.PhotoImage(card_images.crop((ace_left*card_x,club_top*card_y,ace_right*card_x,club_bottom*card_y)))
two_club=ImageTk.PhotoImage(card_images.crop((two_left*card_x,club_top*card_y,two_right*card_x,club_bottom*card_y)))
three_club=ImageTk.PhotoImage(card_images.crop((three_left*card_x,club_top*card_y,three_right*card_x,club_bottom*card_y)))
four_club=ImageTk.PhotoImage(card_images.crop((four_left*card_x,club_top*card_y,four_right*card_x,club_bottom*card_y)))
five_club=ImageTk.PhotoImage(card_images.crop((five_left*card_x,club_top*card_y,five_right*card_x,club_bottom*card_y)))
six_club=ImageTk.PhotoImage(card_images.crop((six_left*card_x,club_top*card_y,six_right*card_x,club_bottom*card_y)))
seven_club=ImageTk.PhotoImage(card_images.crop((seven_left*card_x,club_top*card_y,seven_right*card_x,club_bottom*card_y)))
eight_club=ImageTk.PhotoImage(card_images.crop((eight_left*card_x,club_top*card_y,eight_right*card_x,club_bottom*card_y)))
nine_club=ImageTk.PhotoImage(card_images.crop((nine_left*card_x,club_top*card_y,nine_right*card_x,club_bottom*card_y)))
ten_club=ImageTk.PhotoImage(card_images.crop((ten_left*card_x,club_top*card_y,ten_right*card_x,club_bottom*card_y)))
jack_club=ImageTk.PhotoImage(card_images.crop((jack_left*card_x,club_top*card_y,jack_right*card_x,club_bottom*card_y)))
queen_club=ImageTk.PhotoImage(card_images.crop((queen_left*card_x,club_top*card_y,queen_right*card_x,club_bottom*card_y)))
king_club=ImageTk.PhotoImage(card_images.crop((king_left*card_x,club_top*card_y,king_right*card_x,club_bottom*card_y)))

#spades
ace_spade=ImageTk.PhotoImage(card_images.crop((ace_left*card_x,spade_top*card_y,ace_right*card_x,spade_bottom*card_y)))
two_spade=ImageTk.PhotoImage(card_images.crop((two_left*card_x,spade_top*card_y,two_right*card_x,spade_bottom*card_y)))
three_spade=ImageTk.PhotoImage(card_images.crop((three_left*card_x,spade_top*card_y,three_right*card_x,spade_bottom*card_y)))
four_spade=ImageTk.PhotoImage(card_images.crop((four_left*card_x,spade_top*card_y,four_right*card_x,spade_bottom*card_y)))
five_spade=ImageTk.PhotoImage(card_images.crop((five_left*card_x,spade_top*card_y,five_right*card_x,spade_bottom*card_y)))
six_spade=ImageTk.PhotoImage(card_images.crop((six_left*card_x,spade_top*card_y,six_right*card_x,spade_bottom*card_y)))
seven_spade=ImageTk.PhotoImage(card_images.crop((seven_left*card_x,spade_top*card_y,seven_right*card_x,spade_bottom*card_y)))
eight_spade=ImageTk.PhotoImage(card_images.crop((eight_left*card_x,spade_top*card_y,eight_right*card_x,spade_bottom*card_y)))
nine_spade=ImageTk.PhotoImage(card_images.crop((nine_left*card_x,spade_top*card_y,nine_right*card_x,spade_bottom*card_y)))
ten_spade=ImageTk.PhotoImage(card_images.crop((ten_left*card_x,spade_top*card_y,ten_right*card_x,spade_bottom*card_y)))
jack_spade=ImageTk.PhotoImage(card_images.crop((jack_left*card_x,spade_top*card_y,jack_right*card_x,spade_bottom*card_y)))
queen_spade=ImageTk.PhotoImage(card_images.crop((queen_left*card_x,spade_top*card_y,queen_right*card_x,spade_bottom*card_y)))
king_spade=ImageTk.PhotoImage(card_images.crop((king_left*card_x,spade_top*card_y,king_right*card_x,spade_bottom*card_y)))

#define clock positions
one_x=534
one_y=99
two_x=628
two_y=249
three_x=628
three_y=400
four_x=628
four_y=550
five_x=534
five_y=701
six_x=376
six_y=701
seven_x=216
seven_y=701
eight_x=120
eight_y=550
nine_x=120
nine_y=400
ten_x=120
ten_y=249
eleven_x=216
eleven_y=99
twelve_x=376
twelve_y=99
centre_x=376
centre_y=400

#define deck
deck={ace_heart:1, two_heart:2, three_heart:3, four_heart:4, five_heart:5, six_heart:6, seven_heart:7, eight_heart:8, nine_heart:9, ten_heart:10, jack_heart:11, queen_heart:12, king_heart:13, ace_diamond:1, two_diamond:2, three_diamond:3, four_diamond:4, five_diamond:5, six_diamond:6, seven_diamond:7, eight_diamond:8, nine_diamond:9, ten_diamond:10, jack_diamond:11, queen_diamond:12, king_diamond:13, ace_club:1, two_club:2, three_club:3, four_club:4, five_club:5, six_club:6, seven_club:7, eight_club:8, nine_club:9, ten_club:10, jack_club:11, queen_club:12, king_club:13, ace_spade:1, two_spade:2, three_spade:3, four_spade:4, five_spade:5, six_spade:6, seven_spade:7, eight_spade:8, nine_spade:9, ten_spade:10, jack_spade:11, queen_spade:12, king_spade:13}
        
#shuffle the deck
keys=list(deck.keys())
random.shuffle(keys)
shuffled_deck=[(key) for key in keys]

#set card starting positions
#centre
canvas.create_image(centre_x+(0*x_stack_shift), centre_y, image=(card_back))
canvas.create_image(centre_x+(1*x_stack_shift), centre_y, image=(card_back))
canvas.create_image(centre_x+(2*x_stack_shift), centre_y, image=(card_back))
canvas.create_image(centre_x+(3*x_stack_shift), centre_y, image=(card_back))
#one
canvas.create_image(one_x+(0*x_stack_shift), one_y, image=(card_back))
canvas.create_image(one_x+(1*x_stack_shift), one_y, image=(card_back))
canvas.create_image(one_x+(2*x_stack_shift), one_y, image=(card_back))
canvas.create_image(one_x+(3*x_stack_shift), one_y, image=(card_back))
#two
canvas.create_image(two_x+(0*x_stack_shift), two_y, image=(card_back))
canvas.create_image(two_x+(1*x_stack_shift), two_y, image=(card_back))
canvas.create_image(two_x+(2*x_stack_shift), two_y, image=(card_back))
canvas.create_image(two_x+(3*x_stack_shift), two_y, image=(card_back))
#three
canvas.create_image(three_x+(0*x_stack_shift), three_y, image=(card_back))
canvas.create_image(three_x+(1*x_stack_shift), three_y, image=(card_back))
canvas.create_image(three_x+(2*x_stack_shift), three_y, image=(card_back))
canvas.create_image(three_x+(3*x_stack_shift), three_y, image=(card_back))
#four
canvas.create_image(four_x+(0*x_stack_shift), four_y, image=(card_back))
canvas.create_image(four_x+(1*x_stack_shift), four_y, image=(card_back))
canvas.create_image(four_x+(2*x_stack_shift), four_y, image=(card_back))
canvas.create_image(four_x+(3*x_stack_shift), four_y, image=(card_back))
#five
canvas.create_image(five_x+(0*x_stack_shift), five_y, image=(card_back))
canvas.create_image(five_x+(1*x_stack_shift), five_y, image=(card_back))
canvas.create_image(five_x+(2*x_stack_shift), five_y, image=(card_back))
canvas.create_image(five_x+(3*x_stack_shift), five_y, image=(card_back))
#six
canvas.create_image(six_x+(0*x_stack_shift), six_y, image=(card_back))
canvas.create_image(six_x+(1*x_stack_shift), six_y, image=(card_back))
canvas.create_image(six_x+(2*x_stack_shift), six_y, image=(card_back))
canvas.create_image(six_x+(3*x_stack_shift), six_y, image=(card_back))
#seven
canvas.create_image(seven_x+(0*x_stack_shift), seven_y, image=(card_back))
canvas.create_image(seven_x+(1*x_stack_shift), seven_y, image=(card_back))
canvas.create_image(seven_x+(2*x_stack_shift), seven_y, image=(card_back))
canvas.create_image(seven_x+(3*x_stack_shift), seven_y, image=(card_back))
#eight
canvas.create_image(eight_x+(0*x_stack_shift), eight_y, image=(card_back))
canvas.create_image(eight_x+(1*x_stack_shift), eight_y, image=(card_back))
canvas.create_image(eight_x+(2*x_stack_shift), eight_y, image=(card_back))
canvas.create_image(eight_x+(3*x_stack_shift), eight_y, image=(card_back))
#nine
canvas.create_image(nine_x+(0*x_stack_shift), nine_y, image=(card_back))
canvas.create_image(nine_x+(1*x_stack_shift), nine_y, image=(card_back))
canvas.create_image(nine_x+(2*x_stack_shift), nine_y, image=(card_back))
canvas.create_image(nine_x+(3*x_stack_shift), nine_y, image=(card_back))
#ten
canvas.create_image(ten_x+(0*x_stack_shift), ten_y, image=(card_back))
canvas.create_image(ten_x+(1*x_stack_shift), ten_y, image=(card_back))
canvas.create_image(ten_x+(2*x_stack_shift), ten_y, image=(card_back))
canvas.create_image(ten_x+(3*x_stack_shift), ten_y, image=(card_back))
#eleven
canvas.create_image(eleven_x+(0*x_stack_shift), eleven_y, image=(card_back))
canvas.create_image(eleven_x+(1*x_stack_shift), eleven_y, image=(card_back))
canvas.create_image(eleven_x+(2*x_stack_shift), eleven_y, image=(card_back))
canvas.create_image(eleven_x+(3*x_stack_shift), eleven_y, image=(card_back))
#twelve
canvas.create_image(twelve_x+(0*x_stack_shift), twelve_y, image=(card_back))
canvas.create_image(twelve_x+(1*x_stack_shift), twelve_y, image=(card_back))
canvas.create_image(twelve_x+(2*x_stack_shift), twelve_y, image=(card_back))
canvas.create_image(twelve_x+(3*x_stack_shift), twelve_y, image=(card_back))

#lists of exposed cards
aces=[]
twos=[]
threes=[]
fours=[]
fives=[]
sixes=[]
sevens=[]
eights=[]
nines=[]
tens=[]
jacks=[]
queens=[]
kings=[]

def arse():
    tkint.after(4000)
    canvas.create_image(twelve_x+(0*x_stack_shift), twelve_y, image=(card_back))
    canvas.create_image(twelve_x+(1*x_stack_shift), twelve_y, image=(card_back))
    canvas.create_image(twelve_x+(2*x_stack_shift), twelve_y, image=(card_back))
    canvas.create_image(twelve_x+(3*x_stack_shift), twelve_y, image=(card_back))

for x in range(0,52):
        if deck[shuffled_deck[x]] == 1:
            if len(aces) == 3:
                aces.append(shuffled_deck[x])
                canvas.create_image(twelve_x+(0*x_stack_shift), twelve_y, image=(aces[0]))
                canvas.create_image(twelve_x+(1*x_stack_shift), twelve_y, image=(aces[1]))
                canvas.create_image(twelve_x+(2*x_stack_shift), twelve_y, image=(aces[2]))
                canvas.create_image(twelve_x+(3*x_stack_shift), twelve_y, image=(aces[3]))
                tkint.after(2000)
            if len(aces) == 2:
                aces.append(shuffled_deck[x])
                canvas.create_image(twelve_x+(1*x_stack_shift), twelve_y, image=(aces[0]))
                canvas.create_image(twelve_x+(2*x_stack_shift), twelve_y, image=(aces[1]))
                canvas.create_image(twelve_x+(3*x_stack_shift), twelve_y, image=(aces[2]))
                tkint.after(2000)            
            if len(aces) == 1:
                aces.append(shuffled_deck[x])
                canvas.create_image(twelve_x+(2*x_stack_shift), twelve_y, image=(aces[0]))
                canvas.create_image(twelve_x+(3*x_stack_shift), twelve_y, image=(aces[1]))
                tkint.after(2000) 
            if len(aces) == 0:
                aces.append(shuffled_deck[x])
                canvas.create_image(twelve_x+(3*x_stack_shift), twelve_y, image=(aces[0]))
                tkint.after(2000)      

btn = tk.Button(tkint, text="click me", command=arse)
btn.pack()

#for k, v in deck.items():
#    if v == 2:
#        print(k, v)

tk.mainloop()
