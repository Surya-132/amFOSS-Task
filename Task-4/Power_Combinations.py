def power_sum(X,N,num=1):
    value = X - num ** N
    if value==0:
        return 1
    elif value<0:
        return 0
    else:
        return power_sum(value,N,num+1)+power_sum(X,N,num+1)

X =int(input())
N =int(input())
print(power_sum(X,N))