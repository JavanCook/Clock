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

suits=['club', 'spade', 'heart', 'diamond']
cards=['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
card_coords={}

for suit in range(0,4):
    for card in range(0,13):
        card_top=suit
        card_bottom=suit+1
        card_left=card
        card_right=card+1
        card_name='{0}_{1}'.format(cards[card], suits[suit])
        card_image=ImageTk.PhotoImage(card_images.crop((card_left*card_x,card_top*card_y,card_right*card_x,card_bottom*card_y)))
        card_coords.update({card_name: card_image})

#define clock positions
clock_coords={'one_x': 534, 'one_y': 99, 'two_x': 628, 'two_y': 249, 'three_x': 628, 'three_y': 400, 'four_x': 628, 'four_y': 550, 'five_x': 534, 'five_y': 701, 'six_x': 376, 'six_y': 701, 'seven_x': 216, 'seven_y': 701, 'eight_x': 120, 'eight_y': 550, 'nine_x': 120, 'nine_y': 400, 'ten_x': 120, 'ten_y': 249, 'eleven_x': 216, 'eleven_y': 99, 'twelve_x': 376, 'twelve_y': 99, 'centre_x': 376, 'centre_y': 400}

positions=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","centre"]

#set card starting positions
def reset():
    for place in range(0,13):
        for stack in range(0,4):
            position_x="{0}_x".format(positions[place])
            position_y="{0}_y".format(positions[place])
            canvas.create_image(clock_coords[position_x]+(stack*x_stack_shift), clock_coords[position_y], image=(card_back))

#define deck
deck={'ace_heart':0, 'two_heart':1, 'three_heart':2, 'four_heart':3, 'five_heart':4, 'six_heart':5, 'seven_heart':6, 'eight_heart':7, 'nine_heart':8, 'ten_heart':9, 'jack_heart':10, 'queen_heart':11, 'king_heart':12, 'ace_diamond':0, 'two_diamond':1, 'three_diamond':2, 'four_diamond':3, 'five_diamond':4, 'six_diamond':5, 'seven_diamond':6, 'eight_diamond':7, 'nine_diamond':8, 'ten_diamond':9, 'jack_diamond':10, 'queen_diamond':11, 'king_diamond':12, 'ace_club':0, 'two_club':1, 'three_club':2, 'four_club':3, 'five_club':4, 'six_club':5, 'seven_club':6, 'eight_club':7, 'nine_club':8, 'ten_club':9, 'jack_club':10, 'queen_club':11, 'king_club':12, 'ace_spade':0, 'two_spade':1, 'three_spade':2, 'four_spade':3, 'five_spade':4, 'six_spade':5, 'seven_spade':6, 'eight_spade':7, 'nine_spade':8, 'ten_spade':9, 'jack_spade':10, 'queen_spade':11, 'king_spade':12}
        
#function to shuffle the deck
def shuffle():
    keys=list(deck.keys())
    random.shuffle(keys)
    shuffled_deck=[(key) for key in keys]
    return shuffled_deck

#function to start exposing and placing cards
def start():
    reset()
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
    another_list=[aces,twos,threes,fours,fives,sixes,sevens,eights,nines,tens,jacks,queens,kings]
    test_deck=shuffle()
    for x in range(0,52):
        #tkint.after(1000)
        #tkint.update()
        key_value=(test_deck[x])
        for y in range(0,13):
            if deck[key_value] == y:
                x_value='{0}_x'.format(positions[y])
                y_value='{0}_y'.format(positions[y])
                if len(another_list[y]) == 3:
                    another_list[y].append(key_value)
                    canvas.create_image(clock_coords[x_value]+(0*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[0]]))
                    canvas.create_image(clock_coords[x_value]+(1*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[1]]))
                    canvas.create_image(clock_coords[x_value]+(2*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[2]]))
                    canvas.create_image(clock_coords[x_value]+(3*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[3]]))
                if len(another_list[y]) == 2:
                    another_list[y].append(key_value)
                    canvas.create_image(clock_coords[x_value]+(1*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[0]]))
                    canvas.create_image(clock_coords[x_value]+(2*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[1]]))
                    canvas.create_image(clock_coords[x_value]+(3*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[2]]))
                if len(another_list[y]) == 1:
                    another_list[y].append(key_value)
                    canvas.create_image(clock_coords[x_value]+(2*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[0]]))
                    canvas.create_image(clock_coords[x_value]+(3*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[1]]))
                if len(another_list[y]) == 0:
                    another_list[y].append(key_value)
                    canvas.create_image(clock_coords[x_value]+(3*x_stack_shift), clock_coords[y_value], image=(card_coords[(another_list[y])[0]]))
                
reset()

reset_btn = tk.Button(tkint, text="Reset", command=reset)
reset_btn.pack()
start_btn = tk.Button(tkint, text="Start", command=start)
start_btn.pack()

tk.mainloop()
