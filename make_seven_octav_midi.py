#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import music21
from music21 import *
import random

application_path = "/usr/bin/timidity"
music21.environment.set('midiPath', application_path)



letters = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

octaves_limit = 8

one_to_seven = list()

for i in range (1, octaves_limit):
    for j in range(0, len(letters)):

        new_str = letters[j] + str(i)
        new_str_diese = letters[j] + "#" + str(i)

        print(new_str)
        print(new_str_diese)

        one_to_seven.append(new_str)
        one_to_seven.append(new_str_diese)


Notes_1_to_7 = [note.Note(new_note) for new_note in one_to_seven]



i=0
for i in range(0,len(one_to_seven)):
	s = stream.Stream()
	#Notes_1_to_7[i].duration='whole'
	
	s.append(Notes_1_to_7[i])
	
	fp = s.write('midi', fp=f"./{one_to_seven[i]}.mid")