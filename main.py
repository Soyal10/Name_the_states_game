import turtle
import pandas
screen=turtle.Screen()
tim=turtle.Turtle()
tim.penup()
tim.goto(-300,300)
tim.pendown()
screen.title("GUESS THE ALL STATES OF INDIA.")
screen.bgpic("india_img.gif")
tim.penup()

tim.hideturtle()

data= pandas.read_csv('states_data.csv')
all_states=['Goa','Maharashtra','Uttar Pradesh','Madhya Pradesh','Tamil Nadu','Kerala','Jammu And Kashmir','Himachal Pradesh','Punjab',"Uttarakhand",'Rajasthan','Gujarat',
            'Karnataka','Andhra Pradesh','Odisha','Chhattisgarh','Jharkhand','Bihar','West Bengal','Sikkim','Assam','Meghalaya','Tripura','Mizoram','Manipur','Nagaland',
            'Arunachal Pradesh','Haryana']
score=0
guessed_states=[]
is_on= True
while is_on:
    answer_state=screen.textinput(f"SCORE: {score}/28",'ANOTHER STATE').title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        score=score+1

        state_data= data[data.States == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.pendown()
        tim.write(answer_state)
        tim.penup()
    elif answer_state== "Exit":
        is_on= False



screen.mainloop()
