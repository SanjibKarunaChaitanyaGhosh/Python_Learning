# odd ,even Program

class OddEven():

    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def Even_Odd(self,num):
        self.check(num)

        if self.even==1:
            print(num,"The given Number is EVEN")
        else:
            print(num,"The give number is odd")