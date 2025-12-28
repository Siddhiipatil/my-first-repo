def even_or_odd(num):
    if num%2==0:
        print ("numbber is even",num)
    else:
        print ("numbber is odd",num)
even_or_odd(22)


def armstrong(num):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum += digit**3
        temp//=10
        
    return sum == num
print(armstrong(153))

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact =fact*i
    return fact
print(fact(7))