import os
from pydub import AudioSegment as ass

# get the current working directory
current_working_directory = os.getcwd()
print(current_working_directory+"\n")

all_files = os.listdir();

 


while len(all_files) > 0:
    file = all_files.pop()
    if(file[-4:] == '.wav'):
        print("Changing "+file+"\n")
        absolute_path = os.getcwd()+"\\"+file
        print("Path: "+absolute_path+"\n")
        song = ass.from_wav(absolute_path)
        song = song + (amplify := -16)
        song.export('output\\'+file)




