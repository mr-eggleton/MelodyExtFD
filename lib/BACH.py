""" This module prepares midi file data and feeds it to the neural
    network for training """
import glob
import numpy
from music21 import converter, instrument, note, chord, analysis


def get_notes():
    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    notes = []

    for file in glob.glob("bach/*.mid"):
        notes = []
        midi = converter.parse(file)

        print("Parsing %s" % file)

        notes_to_parse = None

        try: # file has instrument parts
            s2 = instrument.partitionByInstrument(midi)
            for p in s2.parts:
                p.makeMeasures(inPlace=True)
                print(p)
                ka = analysis.floatingKey.KeyAnalyzer(p)
                ka.windowSize = ka.numMeasures // 2
                ka.run()
                #print(ka.getInterpretationByMeasure(0))
                keys = ka.getRawKeyByMeasure()
                print(len(keys), keys)

            exit()
            notes_to_parse = [s2.parts[i].recurse() for i in s2.part]
        except: # file has notes in a flat structure
            notes_to_parse = midi.flat.notes

        

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

        exit()
        print( notes)
    
    #with open('data/notes', 'wb') as filepath:
    #    pickle.dump(notes, filepath)
    #print( notes)
    #return notes

if __name__ == '__main__':
    get_notes()