#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import music21
from music21 import *
import random

application_path = "/usr/bin/timidity"


music21.environment.set('midiPath', application_path)

model_chords = [['C', 'E', 'G'],['C', 'E', 'G', 'B'],['D', 'F', 'A'],['D', 'F', 'A', 'C'],['E','G','B'],['E','G','B','D'],['F','A','C'],['F','A','C','E'],['G','B','D'],['G','B','D','F'],['A','C','E'],['A','C','E','G'],['B','D','F'],['B','D','F','A']]

oct3_chords = [['C3', 'E3', 'G3'],['C3', 'E3', 'G3', 'B3'],['D3', 'F3', 'A3'],['D3', 'F3', 'A3', 'C4'],['E3','G3','B3'],['E3','G3','B3','D4'],['F3','A3','C4'],['F3','A3','C4','E4'],['G3','B3','D4'],['G3','B3','D4','F4'],['A3','C4','E4'],['A3','C4','E4','G4'],['B3','D4','F4'],['B3','D4','F4','A4']]
oct3_names = ["C3E3G3","C3E3G3B3","D3F3A3","D3F3A3C4","E3G3B3","E3G3B3D4","F3A3C4","F3A3C4E4","G3B3D4","G3B3D4F4","A3C4E4","A3C3E4G4","B3D4F4","B3D4F4A4"]
oct3_names_spaced = ["C3 E3 G3","C3 E3 G3 B3","D3 F3 A3","D3 F3 A3 C4","E3 G3 B3","E3 G3 B3 D4","F3 A3 C4","F3 A3 C4 E4","G3 B3 D4","G3 B3 D4 F4","A3 C4 E4","A3 C3 E4 G4","B3 D4 F4","B3 D4 F4 A4"]


for i in range(len(oct3_names_spaced)):
	score = music21.stream.Stream()
	score.append(chord.Chord(oct3_names_spaced[i]))


	fp = score.write('midi', fp=f"./{oct3_names[i]}.mid")