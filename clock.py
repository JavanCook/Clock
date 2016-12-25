#Import modules
import random
import tkinter as tk
from PIL import Image 
from PIL import ImageTk
from time import sleep

#Initialise tkinter    
tkint = tk.Tk()

#Create canvas    
canvas = tk.Canvas(tkint, width=800, height=800, bg='#32a245')
canvas.pack()

#Image import and card dimensions
card_images = Image.open("classic-playing-cards.jpg")
card_back = tk.PhotoImage(file='card-back.gif')
card_x=73
card_y=98
x_stack_shift=15

#Define suits and cards
suits=['club', 'spade', 'heart', 'diamond']
cards=['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
card_coords={}
deck={}

#Create dictionary of deck, card names and images
for suit in range(0,4):
    for card in range(0,13):
        card_top=suit
        card_bottom=suit+1
        card_left=card
        card_right=card+1
        card_name='{0}_{1}'.format(cards[card], suits[suit])
        card_image=ImageTk.PhotoImage(card_images.crop((card_left*card_x,card_top*card_y,card_right*card_x,card_bottom*card_y)))
        card_coords.update({card_name: card_image})
        deck.update({card_name: card})        

#define clock co-ordinates and positions
clock_coords={'one_x': 534, 'one_y': 99, 'two_x': 628, 'two_y': 249, 'three_x': 628, 'three_y': 400, 'four_x': 628, 'four_y': 550, 'five_x': 534, 'five_y': 701, 'six_x': 376, 'six_y': 701, 'seven_x': 216, 'seven_y': 701, 'eight_x': 120, 'eight_y': 550, 'nine_x': 120, 'nine_y': 400, 'ten_x': 120, 'ten_y': 249, 'eleven_x': 216, 'eleven_y': 99, 'twelve_x': 376, 'twelve_y': 99, 'centre_x': 376, 'centre_y': 400}
positions=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","centre"]

#set card starting positions
def reset():
    win_lose(0)
    for place in range(0,13):
        for stack in range(0,4):
            position_x="{0}_x".format(positions[place])
            position_y="{0}_y".format(positions[place])
            #canvas.delete(loser)
            canvas.create_image(clock_coords[position_x]+(stack*x_stack_shift), clock_coords[position_y], image=(card_back))
        
#function to shuffle the deck
def shuffle():
    keys=list(deck.keys())
    random.shuffle(keys)
    shuffled_deck=[(key) for key in keys]
    return shuffled_deck

#Function to start exposing and placing cards
def start():
    #Value of first round
    round_number=0
    #Set running until win
    while True:
        reset()
        #Lists of exposed cards
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
        #Counts round number
        canvas.delete('round')
        winner_text=canvas.create_text(20, 780, text=round_number,font=('Times', 30),tags='round')
        #Goes through deck
        for x in range(0,52):
            key_value=(test_deck[x])
            #Lose condition
            if len(kings) == 4:
                win_lose(1)
                round_number=round_number+1
                sleep(0.5)
                break
            #Places card images
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
            tkint.update()
            sleep(0.2)
        #Win condition
        if x == 51:
            win_lose(2)
            break

#Win/lose events
def win_lose(lose_index):
    if lose_index==1:
        loser_box=canvas.create_rectangle(315, 475, 485, 525, fill='white', tags='lose_rectangle')
        loser_text=canvas.create_text(400, 500, text='You Lose',font=('Times', 30),tags='lose')
        tkint.update()
    if lose_index==0:
        canvas.delete('lose')
        canvas.delete('lose_rectangle')
        canvas.delete('win')
        canvas.delete('win_rectangle')
        tkint.update()
    if lose_index==2:
        winner_box=canvas.create_rectangle(315, 475, 485, 525, fill='white', tags='win_rectangle')
        winner_text=canvas.create_text(400, 500, text='You Win',font=('Times', 30),tags='win')
        tkint.update()

#Place cards                
reset()
#Start button
start_btn = tk.Button(tkint, text="Start", command=start)
start_btn.pack()

#Start tkinter
tk.mainloop()
