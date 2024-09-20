file = open("datasets/rosalind_subs.txt")
dna_seq = file.readline()
motif = file.readline()
dna_seq = dna_seq[0:-1]
motif = motif[0:-1]

print(f"{dna_seq}\n{motif}")

premotif = ""
location = []

for i in range(len(dna_seq)):
    if dna_seq[i] == motif[0]:
        for a in range(len(motif)):
            if i+a >= len(dna_seq):
                pass
            elif dna_seq[i + a] == motif[a]:
                premotif = premotif + motif[a]
        if premotif == motif:
            location.append(i+1)

        premotif = ""

for loc in location:
    print(loc, end=" ")


print("\n----------------------")

# another way
print("This solution doesnt include motifs which are overlapping")
import re

motif2 = re.compile(motif)

for match in motif2.finditer(str(dna_seq)):
    print(match.start() + 1, end=" ")

file.close()