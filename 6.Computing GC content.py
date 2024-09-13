from Bio import SeqIO

GC_count = 0
nucl_count = 0
dic_GC_content = {}
for sequence in SeqIO.parse("datasets/rosalind_gc.txt", "fasta"):
    print(sequence.id)
    for letter in sequence:
        if letter == "G" or letter == "C":
            GC_count += 1
        nucl_count += 1

    print(f"Nucleotides: {nucl_count}")
    print(f"GC count: {GC_count}")

    GC_content = GC_count * 100 / nucl_count
    print(f"GC content: {GC_content} %")
    print("")

    dic_GC_content[sequence.id] = GC_content

    nucl_count = 0
    GC_count = 0

max = 0
winner = ""
for key in dic_GC_content:
    if dic_GC_content[key] > max:
        max = dic_GC_content[key]
        winner = key
print(f"The highest GC content:\n{winner}\n{max}")