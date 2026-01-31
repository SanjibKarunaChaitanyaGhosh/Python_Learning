class Number:

    count=0
    evens=[] # class Variable
    odds=[]
    def __init__(self,num):
        Number.count+=1

        self.num=num

        if num%2==0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)

        print("the counter is hit", Number.count)
        print("Even numbers are : ",Number.evens)
        print("Odd numbers are : ",Number.odds)

N1=Number(20)
N2=Number(25)
N3=Number(23)
N4=Number(28)
N5=Number(46)
N6=Number(26)
N7=Number(2)