""" This module prepares midi file data and feeds it to the neural
    network for training """
import glob
import numpy
from music21 import converter, instrument, note, chord, analysis, scale

def get_valid_scales(p):
    length = len( p.recurse().notes)

    ''' fox dot scales that are in music21
    'chromatic', 'major', 'dorian',  'harmonicMinor','locrian', 'locrianMajor', 'lydian',
    'minor','phrygian','wholeTone'
    '''

    scales = [scale.MajorScale(), scale.MinorScale(),
            scale.ChromaticScale(),
            scale.DiatonicScale(),
            scale.DorianScale(),
            scale.HarmonicMinorScale(),
            scale.LocrianScale(),
            scale.LydianScale(),
            scale.MelodicMinorScale(),
            scale.PhrygianScale(),
            scale.WholeToneScale()
            ]
    allvalid = []
    for sc1 in scales:
        ranked = sc1.deriveRanked(p)
        valid = [s for (c,s) in ranked if length == c]
        if(len(valid)):
            if("ChromaticScale" in valid[0].classes):
                allvalid.append(scale.ChromaticScale("C3"))
            else:    
                allvalid.extend(valid) 
            
    #print(p, allvalid)#, comparisonAttribute='name'))
    return allvalid

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

                #p.makeMeasures(inPlace=True)
                #print(p)
                #p.show('text', addEndTimes=True)
                #ka = analysis.floatingKey.KeyAnalyzer(p)
                #ka.windowSize = ka.numMeasures // 2
                #ka.run()
                #print(ka.getInterpretationByMeasure(0))
                #keys = ka.getRawKeyByMeasure()
                #keys = p.getKeySignatures()
                #print("keys", len(keys), keys)

                print(p, get_valid_scales(p))#, comparisonAttribute='name'))
                


                currkey = None
                '''
                for m in p.getElementsByClass('Measure'):
                    ranked = sc1.deriveRanked(m)
                    (maxc, maxs) = ranked[0]
                    best = [s for (c,s) in ranked if maxc == c]
                    #print("best", best) 
                    if currkey in best :
                        pass
                        #print("keeping ", currkey )
                    else:
                        currkey = best[0]
                        print("change to ", currkey )
                    #, comparisonAttribute='name'))
                '''
                
                
                
                '''
                nameOctaveCount = analysis.pitchAnalysis.pitchAttributeCount(p, 'name')
                print("nameOctaveCount")
                for n in sorted(nameOctaveCount):
                    print("%3s: %2d" % (n, nameOctaveCount[n]))
                '''
            #exit()
            #notes_to_parse = [s2.parts[i].recurse() for i in s2.part]
        except: # file has notes in a flat structure
            notes_to_parse = midi.flat.notes

            print("midi", get_valid_scales(midi))#, comparisonAttribute='name'))
                
        '''
        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))
        
        exit()
        print( notes)
    '''
        
    #with open('data/notes', 'wb') as filepath:
    #    pickle.dump(notes, filepath)
    #print( notes)
    #return notes

if __name__ == '__main__':
    get_notes()