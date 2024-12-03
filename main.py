import sounddevice as sd
import soundfile as sf
import csv
from csv_tools import save_csv,read_csv

def main():
    # save_csv('recording1.mp3')
    # read_csv()

    # duration = 5
    # samplerate = 44100
    # print('Recording started...')

    # audio = sd.rec(int(duration * samplerate),samplerate = samplerate,channels = 2)
    # sd.wait()

    # print('Recording end')

    # sf.write(f'{filename}.mp3',audio,samplerate)
    # print('File saved!')
    
    options = """
Options:
1. Recording audio
2. Show  recording history
3. Play existing record
"q" - close program
"""
    while True:
        print(options)
        user_option = input()

        if user_option == 'q':
            print('Bye. See you later!')
            return
        elif user_option == '1':
            print('record audio')
            # record_audio()
        elif user_option == '2':
            print('show_history')
            # show_history()
        elif user_option == '3':
            print('play_record')
            # play_record()
        else:
            print('Input error. Try again!')

if __name__ == '__main__':
    main()