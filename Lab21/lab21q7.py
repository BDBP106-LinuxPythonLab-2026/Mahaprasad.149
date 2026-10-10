#Write a function analyse_dna(sequence) that defines an inner function gc_content()
#to calculate GC% . The outer function should print whether the given DNA is AT rich
#or GC rich sequence.

DNA=str(input("Enter a DNA Sequence: ")).upper()

def analyse_dna(sequence):
    def gc_content():
        G = sequence.count('G')
        C = sequence.count('C')
        return (G + C) / len(sequence) * 100

    GC = gc_content()

    if GC > 50:
        print("GC Rich sequence")
    else:
        print("AT Rich sequence")


analyse_dna(DNA)



