class ABC():
    class_var=0 # class variable

    def __init__(self,var):

        ABC.class_var +=1

        self.var=var # object VAriable

        print("The value of class variable is : ",ABC.class_var)
        print("The object value is : ", var)


obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)

