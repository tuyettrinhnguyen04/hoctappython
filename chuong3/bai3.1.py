import math
a=float(input())
b=float(input())
c=float(input())
p=((a+b+c)/2)
if a+b>c and a+c>b and b+c>a:
    print('dien tich=','sqrt(p*(p-a)*(p-b)*(p-c))',math.sqrt(p*(p-a)*(p-b)*(p-c)))
else :
    print('khong hop le')
    

    


