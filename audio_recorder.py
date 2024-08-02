import pyaudio
import wave
import whisper
import text_editor # type: ignore

CHUNK = 1024 # определяет форму ауди сигнала
FRT = pyaudio.paInt16 # шестнадцатибитный формат задает значение амплитуды
CHAN = 1 # канал записи звука
RT = 44100 # частота 
REC_SEC = 5 #длина записи
OUTPUT = "C:\Whisper AI\output.wav"

def get_record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FRT,channels=CHAN,rate=RT,input=True,frames_per_buffer=CHUNK) # открываем поток для записи
    print("rec")
    frames = [] # формируем выборку данных фреймов

    for i in range(0, int(RT / CHUNK * REC_SEC)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("done")
    # и закрываем поток 
    stream.stop_stream() # останавливаем и закрываем поток 
    stream.close()
    p.terminate()

    w = wave.open(OUTPUT, 'wb')
    w.setnchannels(CHAN)
    w.setsampwidth(p.get_sample_size(FRT))
    w.setframerate(RT)
    w.writeframes(b''.join(frames))
    w.close()

    audio = whisper.load_audio(OUTPUT)
    return audio