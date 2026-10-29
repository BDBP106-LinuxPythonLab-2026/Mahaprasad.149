#Write a function analyse_dna(sequence) that defines an inner function gc_content() to calculate GC% . The outer function should print whether the given DNA is AT rich or GC rich sequence.
def analyse_dna(sequnce):
    def gc_content():
        gc=sequnce.count('G')+sequnce.count('C')
        return(gc/len(sequnce))*100
    gc=gc_content()
    print(gc,"%")
    if gc>50:
        print("GC rich sequnce")
    else:
        print("AT rich sequence")
analyse_dna("GCGCCGTACGTAAT")