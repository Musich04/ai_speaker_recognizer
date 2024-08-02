
# Запись строки в документ
def write_line_in_file(line):
    
    with open('C:\Whisper AI/Text.txt', 'a') as f:
        f.write(line + '\n')
    
    f.close()

# Чтение данных из файла
def read_file():
    lines = []

    with open('C:\Whisper AI/Text.txt', 'r') as f:
        for line in f:
            lines.append(line)
    
    f.close()
    
    return lines

# Удаление всех данных из файла
def delete_data():
     with open('C:\Whisper AI/Text.txt', 'w') as f:
        pass