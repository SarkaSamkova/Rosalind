my_file = open("datasets/rosalind_hamm.txt")
a_seq = my_file.readline()
b_seq = my_file.readline()

print(a_seq)
print(b_seq)

Hamming_distance = 0
for i in range(len(a_seq)-1):
    if a_seq[i] != b_seq[i]:
        Hamming_distance += 1
print(Hamming_distance)


my_file.close()