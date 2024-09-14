from Bio.Seq import Seq

ros_file = open("datasets/rosalind_translation.txt")
rna = Seq(ros_file.readline())
protein = rna.translate()
print(protein)

ros_file.close()