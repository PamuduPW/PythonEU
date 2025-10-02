def Collatz(num):
    val1 = 1
    term2 = 1
    max_term_val = 0
    while val1<=num:
        val2 = val1
        term1 = 1
        while val2!=1:
            remainder = val2%2
            if remainder==0:
                val2 = val2/2
            else:
                val2 = val2*3+1
            term1 += 1
        
        if term2<term1:
            term2 = term1
            max_term_val = val1
        
        val1 += 1

    return f"{max_term_val} has the biggest terms in Collatz sequence under number {num} and it has {term2} terms."


n = int(input("From what number below do you want to proceed :"))
print(Collatz(n))