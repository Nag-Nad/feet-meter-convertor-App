import PySimpleGUI as sg
from feet_meter_convertor import converter

sg.theme('LightGreen7')
lable_feet = sg.Text('Enter feet: ', font= 9)
input_feet = sg.InputText(tooltip='Enter feet', key='feet')
lable_inches = sg.Text('Enter inches: ', font= 9)
input_inches = sg.InputText(tooltip='Enter feet', key='inches')
lable_output = sg.Text("The output is: ", key="output", font= 9, text_color='Yellow')
button = sg.Button('Convert', button_color= 'Black', mouseover_colors= 'Black')
col1 = sg.Column([[lable_feet], [lable_inches]])
col2 = sg.Column([[input_feet], [input_inches]])

window = sg.Window('Convertor', layout=[[col1, col2],
                                        [button, lable_output]])

while True:
    event, values = window.read()
    match event:
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
    
    try:
        feet = float(values['feet'])
        inches = float(values['inches'])
        results = converter(feet, inches)
        window['output'].update(
        value=f'The output is: {results} m', text_color='white')
    except ValueError:
        sg.popup('Both Boxes cannot be emoty!', font=9, text_color='Red', background_color='White')


window.close()
