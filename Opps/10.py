class School():

    school_name=" Dashghara High School"

    def __init__(self,name_of_the_Students):

        self.Name = name_of_the_Students
        self.school_name1="Dashghara Higher Secondary School"

        print("The Name of the School is : ",School.school_name)
        print("The Name of the School is : ",self.school_name1)
        print("The Name of the Student is : ",name_of_the_Students)

sc1=School("Sounava Mitra")

