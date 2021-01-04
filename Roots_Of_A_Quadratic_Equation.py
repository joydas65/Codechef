# Question Link https://www.codechef.com/problems/QUADROOT

a = int(input())

b = int(input())

c = int(input())

d = (((b**2)-(4*a*c))**0.5)

x1,x2 = (-b+d)/(2*a),(-b-d)/(2*a)

print(x1)
print(x2)
