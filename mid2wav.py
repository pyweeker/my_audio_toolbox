import os
import subprocess

cwd = os.getcwd()


files = [f for f in os.listdir(cwd) if os.path.isfile(f)]


print(files)


sf2 = "./MuseScore_General.sf2"
out_type = "wav"



for file in files:
    if file.endswith('.mid'):

        
        filename, file_extension = os.path.splitext(file)

        print(f" filename {filename}")
        #print(f" file_extension {file_extension}")


        #os.rename(filename, filename[2:-2])
        #os.rename(filename+'.mid', filename+'.wav')


        #os.rename('a.txt', 'b.kml')

        midi_file = file

        out_file = filename + ".wav"

        subprocess.call(['fluidsynth', '-T', out_type, '-F', out_file, '-ni', sf2, midi_file])




"""
inp = "bb_111bpm.mid"
out = "out.wav"




out_type = "wav"
out_file = out
sf2 = "./MuseScore_General.sf2"
midi_file = inp


subprocess.call(['fluidsynth', '-T', out_type, '-F', out_file, '-ni', sf2, midi_file])
"""