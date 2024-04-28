import os
from pydub import AudioSegment as ass

# get the current working directory
current_working_directory = os.getcwd()
print(current_working_directory+"\n")

all_files = os.listdir();

# set a positive value to increase wav volume and a negitive value to decrease it
amplify = -16


while len(all_files) > 0:
    file = all_files.pop()
    if(file[-4:] == '.wav'):
        print("Changing "+file+"\n")
        absolute_path = os.getcwd()+"\\"+file
        print("Path: "+absolute_path+"\n")
        song = ass.from_wav(absolute_path)
        song = song + amplify
        song.export('output\\'+file, format='wav')




