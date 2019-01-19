from music21 import *

def to_midi_file(flat_midi_notes, path):
    s = stream.Stream()
    
    for midi_note in flat_midi_notes:
        #print(midi_note)
        p = pitch.Pitch()
        p.midi = midi_note
        n = note.Note()
        n.pitch = p
        s.append(n)
    
    fp = s.write('midi', fp=path)
    return (s, fp)