import PySimpleGUI as sg

theme = sg.theme('LightGrey1')
window = sg.FlexForm('reelSRCH')

layout = [
    [sg.Text('Please enter the name of a movie below')],
    [sg.Text('Movie Title', size=(8, 1)), sg.InputText('', (53,1))],
    [sg.Output(size=(63, 10))],
    [sg.Checkbox('All', default=False, key='-All-'), sg.Checkbox('Title', default=False, key='-Title-'), sg.Checkbox('Plot', default=False, key='-Plot-'),
     sg.Checkbox('Year', default=False, key='-Year-'), sg.Checkbox('Director', default=False, key='-Director-'),
     sg.Checkbox('Cast', default=False, key='-Cast-'), sg.Checkbox('Runtime', default=False, key='-Runtime-'),],
    [sg.Button('SEARCH'), sg.Button('EXIT')],
    ]

button, values = window.Layout(layout).Read()
