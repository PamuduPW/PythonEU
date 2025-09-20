#Special pythagorean triplet

for c in range(300,500):
    for b in range(100,400):
        for a in range(100,400):
            if a**2 + b**2 == c**2 and a + b + c == 1000 and a<b<c:
                print(f"a = {a}, b = {b}, c = {c}, then abc = {a*b*c}")