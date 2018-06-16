def Current_value(PA,rate,t):
    temp = 0
    for n in range(t):
        temp = temp + PA/(pow(1+rate,n+1))
        print(n)
    return temp

