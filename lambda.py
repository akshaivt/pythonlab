area_sq=lambda a: a*a
area_rect=lambda l,w:1*w
area_tri=lambda b,h:0.5*b*h
s=float(input("Square side: "))
print("square area=",area_sq(s))
l=float(input("Rectangle length: "))
w=float(input("Rectangle width: "))
print("Rectangle area=",area_rect(l,w))
b=float(input("Triangle base: "))
h=float(input("Triangle height: "))
print("Triangle area=",area_tri(b,h))

