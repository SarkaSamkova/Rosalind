s = "AATATGTGTCAATTGCACAAACGAAGTTAGTCTTTTCGGGCTGATTTGGGCAAGAAGAATTCTGGCAACCCTAAGGCTTTAGGTTGGCTCTGCACGGTCATCAGACAGAGTCCAACTTGCGACCCAACCGGACAAGGTAAGGGCTCTCCCTCCGAGTTTCTGCTGTTCCTCACACCATGGCGGCTGCCGCGCTTATGGCCTTGCCAGGATGAGAACGTTTGTCACGCCGAACGTGATTGACCCGTGAGATGCTACTATGAAGCAATGATGCCTGGCGCCAGTCGGCATGGCGGAAAGATACACGACAATGTTACGGTACGCTGTCGCTGCCATGATCGTAGCGGTTTGCCATGGGAGGTCTATTATCCAGATACTTGCGTCGGTTTCGGTCGTCCAACATCTGTTTCCGACCGCCAGAGCATTCAGACCATATTCGCCATCGCCGCCCGGTGCACAGAAAAAGTTTCGACATTGTAATTACCAAAACCCGTGATCACTCTAATAATTGTGAACCGAAAAACATGTAATATAATGGTCCGATAATACTGAGTCTGTAGCCCAAAACGTATCTTGAACCGAGGAGAATTAGACTACGGAGTTTTTGTCCGCCAAGGTGGCGGGCTACTTAGGTCGAAATGGACCCTCGAGGCCGTACTCCTTATTCGGGCCCATTTCATAAAATTGTACGACTGGGGAAGCAGATGCACCTCAATGGCCAGATTCTACCTGACCCTGCATTCAGTTGTTATACTTCCATTCCCGCATGTGGCTAATTAATTATCACCGGATGCAAAGCCTTGGAAGCGCAGTGTATAACATGACCGATACTCACGGCCCCTTTCTTCTTGTGGCCACATAACAAGTTTAGTTCTTTTGACATTAATAACAACACAGCCT"

A = 0
C = 0
G = 0
T = 0
print(len(s))
for i in range(len(s)):
    if s[i] == "A":
        A += 1
    elif s[i] == "C":
        C += 1
    elif s[i] == "G":
        G += 1
    elif s[i] == "T":
        T += 1
print(f"{A} {C} {G} {T}")