
def populare(studenti):

    class timp():
        def __init__(self,numeZiar,timpZiar):
            self.numeZiar = numeZiar
            self.timpZiar = timpZiar
            self.citit=0            #0 neatins 1 in citire 2 terminat
            self.start=0
        def afisare(self):
            print ("Nume ziar: {} Timp Ziar: {}".format(self.numeZiar,self.timpZiar))

    class student():
        def __init__(self,numeStudent,ora):
            self.numeStudent = numeStudent
            self.ora=ora
            self.timp = []
            self.poz = 0
        def afisare(self):
            print ("Poz: {}  Numele studentului: {}  Ora: {}\n".format(self.poz,self.numeStudent,self.ora))
            for element in self.timp:
                print("Ziar: {}   Timp de citire: {}".format(element.numeZiar,element.timpZiar))
            print("\n")

    with open('data','r') as data:
        for lines in data.readlines():
            text=lines.split('  ')
            stud=student(text.pop(0),text.pop(0))
            studenti.append(stud)
            for grup in text:
                vector=grup.split(",")
                if len(vector)>1:
                    stud.timp.append(timp(vector.pop(0).rstrip() ,vector.pop().rstrip()))
            stud=None
    c=0
    for student in studenti:
        student.poz=c
        student.afisare()
        c=c+1


def pot_citi(studenti,citeste,minut):
    for student in studenti:
        if citeste[student.poz] == 2:
            break
        if student.ora+minut == 0:
            citeste[student.poz] = 1

def alg():
    pass

if __name__ == "__main__":
    studenti=[]
    citeste=[0,0,0,0]
    ziare=[0,0,0,0]
    populare(studenti)
    minut=0
    for student in studenti:
        for timp in student.timp:
            timp.afisare()
        print()
    while True:
        pot_citi(studenti,citeste,minut)
        if 1 in citeste:
            alg()
        for student in studenti:
            if citeste[student.poz] == 2:
                if minut-student.timp[ziare.index(student.poz)].start == student.timp[ziare.index(student.poz)].timpZiar:
                    student.timp[ziare.index(student.poz)].citire=2
        minut+=1
