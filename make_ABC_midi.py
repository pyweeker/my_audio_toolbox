#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import music21
from music21 import *
import random

application_path = "/usr/bin/timidity"
music21.environment.set('midiPath', application_path)

c = note.Note("C4")
d = note.Note("D4")
e = note.Note("E4")
f = note.Note("F4")
g = note.Note("G4")
a = note.Note("A4")
b = note.Note("B4")

"""
z = note.Note("C6")


n = note.Note("D#3")
"""


#n.duration.type = 'half'
dur_not = 'whole'
note_list = [c,d,e,f,g,a,b]
notename_list = ['C4','D4','E4','F4','G4','A4','B4']


#fp = s.write('midi', fp='pathToWhereYouWantToWriteIt')
#fp = s.write('wav')

i=0
for i in range(0,len(note_list)):
	s = stream.Stream()
	note_list[i].duration='whole'
	#s.append(note_list[i])
	s.append(note_list[i])
	#fp = s.write('wave', fp=f"./{notename_list[i]}.wav")
	fp = s.write('midi', fp=f"./{notename_list[i]}.mid")

