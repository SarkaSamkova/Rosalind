k, m, n = 22, 17, 26
# celek
x = k + m + n

# vždy domin fenotyp
# pravděpodobnost AA + AA
pr_1 = (k/x) * ((k-1)/(x-1))
# AA + Aa
pr_2 = (k/x) * (m/(x-1))
# AA + aa
pr_3 = (k/x) * (n/(x-1))

prob_AA = pr_1 + pr_2 + pr_3

# pravděpodobnost Aa + AA
pr_4 = (m/x) * (k/(x-1))
# Aa + Aa - 0,75
pr_5 = (m/x) * ((m-1)/(x-1))
# Aa + aa - tady jen 50% dominantní fenotyp
pr_6 = (m/x) * (n/(x-1))

prob_Aa = pr_4 + (0.75 * pr_5) + (1/2 * pr_6)

# pravděpodobnost aa + AA - 1
pr_7 = (n/x) * (k/(x-1))
# aa + Aa - 1/2
pr_8 = (n/x) * (m/(x-1))
# aa + aa - nn

prob_aa = pr_7 + (1/2 * pr_8)

dom_probability = prob_AA + prob_Aa + prob_aa

print(prob_AA, prob_Aa, prob_aa)
print(dom_probability)


# jednodušší přes komplementární pravděpodobnost

def firstLaw(k,m,n):
    N = float(k+m+n)
    return 1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( N*(N-1) )
print(firstLaw(2,2,2))