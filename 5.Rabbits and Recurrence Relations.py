#  months, litter of
n, k = 10, 2
# 2, 1 - 1
# 3, 1 = 2
# 4, 1 = 3
# 5,1 = 5
# 6, 1 = 8
# 7, 1 = 13

Fibonacci = [1]
for i in range(1, 41):
    if i == 1:
        Fibonacci.append(i)
    else:
        a = Fibonacci[i-1] + Fibonacci[i-2]
        Fibonacci.append(a)


sequence = [1]
for i in range(1, n):
    # abych zajistila první dva měsíce 1, 1
    if i == 1:
        sequence.append(i)
    else:
        # b = k**i - sequence[i-1]
        # total = 1 + (i-3)*k + (k**(i-3))

        # jako Fibonacci a vždycky dospěje ta generace, co už tam 2 kola byla == ta s i-2, proto se pak násobí k, protože budou mít malé
        total = sequence[i-1] + sequence[i-2]*k
        sequence.append(total)

print(sequence)
print(f"The total number of rabbit pairs after {n} months with litter of {k} rabbit pairs is {sequence[-1]} rabbit pairs.")

""" 
kod z rosalindy:
def fib(n, k):
    previous1, previous2 = 1, 1
    for i in range(2, n):
        previous1, previous2 = previous2, previous1 * k + previous2
    return previous2
"""