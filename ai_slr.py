from audio_recorder import get_record_audio # type: ignore
from whisper_ai import language_detector # type: ignore
import text_editor # type: ignore
import threading
import time
import PySimpleGUI as sg

language_type = 'en\n'

# Вычисление процентов выбранного языка
def get_language_percent(language_name):

    language_value = 0

    lines = text_editor.read_file()

    if len(lines) == 0:
        return 0

    for line in lines:
        if line == language_name:
            language_value += 1
    
    value = (language_value / len(lines)) * 100

    print(f'Language {language_name} percentage: {value}')
    return value


# Запуск цикла распознавания речи
def start_ai():
    while not stop_event.is_set():
        audio = get_record_audio()
        language = language_detector(audio)
        text_editor.write_line_in_file(language)
        window['PERCENT'].update(get_language_percent(language_type))


# Определение макета окна 
layout = [ 
     
    [sg.Text('Speaker Language Recognition', key='MAIN_NAME', pad=((120,0),(10,0)), font=('Arial', 18), text_color='black')],
    [sg.Text('START', key='INIT_EXT', pad=((250,0),(25,0)), font=('Arial', 16), background_color='lightblue', text_color='black')],
    [sg.Text('Language: English', key='LANGUAGE', pad=((50,0),(20,0)), font=('Arial', 14), text_color='black'),
    sg.Text(get_language_percent(language_type), key='PERCENT', pad=((20,0),(20,0)), font=('Arial', 14), text_color='black'),],

    [sg.Button('Record', size=(15,4), pad=((150,0),(50,0))), 
    sg.Button('Stop', size=(15,4), pad=((50,0),(50,0)))],
    [sg.Button('Clear All', size=(10,2), pad=((500,0),(100,0)))]
] 
 
# Создание окна 
window = sg.Window('AI System for SLR', layout, size=(600, 400)) 

stop_event = threading.Event()

# Чтение событий и обработка их 
while True: 
    event, values = window.read() 
    print('Event:', event)
    if event == sg.WINDOW_CLOSED:
        if stop_event.is_set():
            stop_event.set()
        
        break 
    
    if event == 'Record': 
        thread = threading.Thread(target=start_ai)
        stop_event.clear()
        thread.start()
        window['INIT_EXT'].update('Record')

    if event == 'Stop': 
        stop_event.set()    
        window['INIT_EXT'].update('Stop')
        

    if event == 'Clear All': 
        text_editor.delete_data()
        window['PERCENT'].update('0%')
        window['INIT_EXT'].update('Clear All Data')

 
# Закрытие окна 
window.close()