import PySimpleGUI as sg
from PythonMETAR import *

##metar search function
def metar_Search(airport_code):
    try:
        metar_result = Metar(airport_code.upper())
    except:
        metar_result = 'No METAR Found'
    return metar_result

sg.set_options(font=('Helvetica', 18))
show_results = ''

##column
column_one = [
    [sg.Input("", size=(6), key = '-ICAO_CODE-', background_color='#656565', text_color='white', border_width='0', expand_y=True, do_not_clear=False), 
     sg.Button("Search", bind_return_key=True, button_color=('#DCDCDC', '#656565'), border_width='0')],
]
##window layout
layout = [[sg.VPush(background_color='#3B3B3B')],
    [sg.Text("Type ICAO Code:", text_color='#DCDCDC', background_color='#3B3B3B')],
    [sg.Column(column_one, background_color='#3B3B3B', element_justification='c', expand_x=True)],
    [sg.Text("", key = '-RESULT-', text_color='#DCDCDC', background_color='#3B3B3B')],
[sg.VPush(background_color='#3B3B3B')]]
##window itself
window = sg.Window("METAR Viewer", layout, element_justification='center', background_color='#3B3B3B', resizable=True, size=(800,400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #user closes window
        break
    if event == "Search":
        window['-RESULT-'].update(metar_Search(values['-ICAO_CODE-']))
        window['-RESULT-'].update(background_color='#656565', text_color='#DCDCDC')
        if metar_Search(values['-ICAO_CODE-']) == 'No METAR Found':
            window['-RESULT-'].update(text_color='#E2941E')