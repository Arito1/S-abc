import math
a=int(input ("a = "))
b=int(input ("b = "))
c=int(input ("c = "))
s=0
p=0
if a + b <= c or a + c <= b or b + c <= a:
    print("ТАКОГО ТРЕУГОЛЬНИКА НАХУЙ НЕ СУЩЕСТВУЕТ")
elif a**2 + b**2 == c**2:
    print("ТРЕУГОЛЬНИК ПРЯМОУГОЛЬНЫЙ")
    s = (a*b)/2
    p = a + b + c
    print("p=",p,"s=",s3)
elif a==b==c:
    print("ТРЕУГОЛЬНИК РАВНОСТОРОНИЙ")
    p = 3*a
    s = math.sqrt((p/2)*((p/2)-a)*((p/2)-b)*((p/2)-c))
    print("p=", p, "s=", s)
elif a==b or a==c or b==c:
    print("ТРЕУГОЛЬНИК РАВНОБЕДРЕННЫЙ")
    p = a+b+c
    s = math.sqrt((p / 2) * ((p / 2) - a) * ((p / 2) - b) * ((p / 2) - c))
    print("p=", p, "s=", s)
elif a!=b and a!=c and b!=c:
    print("ТРЕУГОЛЬНИК ПРОИЗВОЛЬНЫЙ")
    p = a + b + c
    s = math.sqrt((p / 2) * ((p / 2) - a) * ((p / 2) - b) * ((p / 2) - c))
    print("p=", p, "s=", s)