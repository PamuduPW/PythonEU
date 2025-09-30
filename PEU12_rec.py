def triangle_factors(num_factor,triangle=1,val=1):
    number = 0
    for factor in range(1,int(triangle**0.5)+1):
        if triangle%factor==0:
            if factor**2==triangle:
                number += 1
            else:
                number += 2
    if number<num_factor:
        val += 1
        return triangle_factors(num_factor,Triangle_num(num =val),val)
    else:
        return triangle


def Triangle_num(num=1,triangle=1,element=1):
    if num==1:
        return triangle
    else:
        element += 1
        triangle += element
        return Triangle_num(num-1,triangle,element)




n = int(input("Enter how many factors do you want to be in the trianlge number :"))
print(triangle_factors(num_factor=n))