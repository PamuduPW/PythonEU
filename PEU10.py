#The sum of the primes

def prime(m):
    sum = 5
    t = 0
    pnum =[2,3]
    for i in range(5,m+1,2):
        index = 0
        while (j:=pnum[index]) <= int(i**0.5):
            remainder=i%j
            if remainder != 0:
                t = 1
            else:
                t = 0
                break
            index += 1
        if t == 1:
            sum += i
            pnum.append(i)
    return sum

n = int(input("Enter to what numbers do you want to get sum of prime numbers :"))
print(f"The sum of the below {n} prime numbers is {prime(n)}")