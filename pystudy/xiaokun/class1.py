class Stu:
    def __init__(self,Name,ID):
        self.Name = Name
        self.ID = ID 
    def SetID(self, id):
        self.ID = id 
    def Prt(self):
        print(self.ID)
        print(self.Name)
#if __init__ == '__main__':
s1=Stu("xi",1)
s1.Prt()

