#First Porject LESSSSSSSSSS GOOOOOOOOOOOOOOOOOOOOOOOOO
#(First time so mentioning all Steps for future referance)

#Importing the Module
import PySimpleGUI as sg

#Default Stuff

whitebutton:dict={'size':(7,2),'font':('Arial',20),'button_color':('black','#FFFFFF')}
equaltobutton:dict={'size':(15,2),'font':('Arial',20),'button_color':('black','#FFFFFF')}

#Layout

layout:list= [
    [sg.Text('Welcome to the Calculator!',size=(50,1),justification='left',background_color='#FFFFFF',text_color='black',font=('Arial',14, 'bold'))],
    [sg.Text("0",size=(18,2),justification='right',background_color='#FFFFFF',text_color='black',font=('Arial',40,'bold'))],
    [sg.Button(button_text="C",**whitebutton),sg.Button(button_text="CE",**whitebutton),sg.Button(button_text="%",**whitebutton),sg.Button(button_text="/",**whitebutton)],
    [sg.Button(button_text="7",**whitebutton),sg.Button(button_text="8",**whitebutton),sg.Button(button_text="9",**whitebutton),sg.Button(button_text="*",**whitebutton)],
    [sg.Button(button_text="4",**whitebutton),sg.Button(button_text="5",**whitebutton),sg.Button(button_text="6",**whitebutton),sg.Button(button_text="-",**whitebutton)],
    [sg.Button(button_text="1",**whitebutton),sg.Button(button_text="2",**whitebutton),sg.Button(button_text="3",**whitebutton),sg.Button(button_text="+",**whitebutton)],
    [sg.Button(button_text="0",**whitebutton),sg.Button(button_text=".",**whitebutton),sg.Button(button_text="=",**equaltobutton)]
        ]

#Creating the Window
window=sg.Window("Calculator",layout=layout,background_color='#FFFFFF',size=(580,660))

#Just Testing to See How it turns out
while True:             
    event, values=window.read()
    break
window.close()
