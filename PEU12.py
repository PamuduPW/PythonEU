def triangle_num(num_factor):
    element = 1
    triangle = 1
    count = 0
    while count<num_factor:
        count = 0
        element += 1
        triangle += element
        for factor in range(1,int(triangle**0.5)+1):
            remainder = triangle%factor
            if remainder==0:
                if factor**2==triangle:
                    count+=1
                else:
                    count+=2

    return triangle

n = int(input("Enter how many divisors do you want to have in the triangle number :"))
print(triangle_num(n))