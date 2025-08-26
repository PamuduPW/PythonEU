#largest product within 13 continuity numbers

def product(m):
    fn = 0
    ln = 13
    pro = 0
    while ln<=len(m):
        mul = 1
        for i in range(fn,ln):
            mul = mul*int(m[i])
        if mul>=pro:
            pro = mul
            x = m[fn:ln]
        fn+=1
        ln+=1
        num = "*".join(x)
    return print(f"The largest product by 13 continuity numbers is {num} = {pro}")

n =input("Enter the number :")
product(n)