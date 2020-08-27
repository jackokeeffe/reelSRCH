import PySimpleGUI as sg

theme = sg.theme('LightGrey1')
window = sg.FlexForm('reelSRCH')

layout = [
    [sg.Text('Please enter the name of a movie below')],
    [sg.Text('Movie Title', size=(15, 1)), sg.InputText()],
    [sg.Output(size=(59, 10))],
    [sg.Checkbox('Title', default=False, key='-Title-'), sg.Checkbox('Plot', default=False, key='-Plot-'),
     sg.Checkbox('Year', default=False, key='-Year-'), sg.Checkbox('Director', default=False, key='-Director-'),
     sg.Checkbox('Cast', default=False, key='-Cast-'), sg.Checkbox('Runtime', default=False, key='-Runtime-'),],
    [sg.Button('SEARCH'), sg.Button('EXIT')],
    ]

button, values = window.Layout(layout).Read()
