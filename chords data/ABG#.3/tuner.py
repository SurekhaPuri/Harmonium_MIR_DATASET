import time
import sys
import librosa
import librosa.display
import matplotlib.pyplot as plt
from os import system
import pyaudio, wave, os
from time import sleep

system('cls')


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def recorda(outputName, length):
    bytes = 2048
    recordLength = length
    format = pyaudio.paInt16
    channels = 1
    outputFile = outputName
    rate = 16000
    audioRecorder = pyaudio.PyAudio()
    recorder = audioRecorder.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=bytes)
    myArr = []
    print("Started Recording...")
    for i in range(0, int(rate / bytes * recordLength)):
        data = recorder.read(bytes)
        myArr.append(data)
    print("Wait :D")
    recorder.stop_stream()
    recorder.close()
    audioRecorder.terminate()
    waveFile = wave.open(outputFile, "wb")
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(audioRecorder.get_sample_size(format))
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(myArr))
    waveFile.close()


start = int(input("Enter Start = "))
end = int(input("Enter End = "))

sleep(4)
i = start
while i <= end:
    fff = str(i) + ".wav"
    recorda(fff, 2)
    x, sr = librosa.load(fff)
    hop_length = 512
    chromagram = librosa.feature.chroma_cens(x, sr=sr, hop_length=hop_length)
    plt.figure(figsize=(10, 5))
    librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')
    ff = str(i) + '.png'
    print(ff, "saved.")
    print()
    plt.savefig(ff)
    if i > 1 and i % 100 == 0:
        if i == 300:
            print("300 wav files saved...Exiting.....")
            sys.exit(0)
        elif i == 500:
            print("500 wav files saved...Exiting.....")
            sys.exit(0)
        else:
            total = 60
            j = 0
            while j < total:
                os.system('cls')
                print("60 sec wait time....\n\n")
                progress(j, total, status='')
                time.sleep(1)  # emulating long-playing job
                j += 1
            os.system('cls')
    i += 1
