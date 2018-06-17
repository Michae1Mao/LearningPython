def Current_value(Anuity,rate,t):
    temp = 0
    for n in range(t):
        temp = temp + Anuity/(pow(1+rate,n+1))
    return temp


def CalAnuity(CV,rate,t):
    temp = 0
    for n in range(t):
        temp = temp + 1/(pow(1+rate,n+1))
    return CV/temp
