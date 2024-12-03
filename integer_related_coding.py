### to print list of even and ODD in list comphrehension

result = [num if num%2==0 else 'odd' for num in range(1,11)]
print(result)

### to check whether the given number is prime or not

num = int(input('enter the number: '))

if all(num%i !=0 for i in range(2,num)):
    print('true')
else:
    print('false')


a = [(5,'a'),(2,'b'),(3,'d'),(5,'ab')]

## o/p: {5:['a','ab'],2:['b'],3:['d']}

d ={}

for i,k in a:
    d.setdefault(i,[]).append(k)
    # print(d)
    
print(d)


## a=[300,300,200,200,200,100,100,100,100,500,600,600]
## based on the input number it should return the values of the times

n = input('enter: ')

d={}

for i in a:
    d.setdefault(i,[]).append(i)

print(d)

for k,v in d.items():
    if len(v) == int(n):
        print(k,'values repeated N times')