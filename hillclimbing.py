from copy import deepcopy as dc
from random import sample

def populare(studenti):

    class timp():
        def __init__(self,numeZiar,timpZiar):
            self.numeZiar = numeZiar
            self.timpZiar = timpZiar
            self.start=0
        def afisare(self):
            print ("Nume ziar: {} Timp Ziar: {}".format(self.numeZiar,self.timpZiar))

    class student():
        def __init__(self,numeStudent,ora):
            self.numeStudent = numeStudent
            self.ora=ora
            self.timp = []
            self.poz = 0
            self.solutie = []
        def afisare(self):
            print ("Poz: {}  Numele studentului: {}  Ora: {}\n".format(self.poz,self.numeStudent,self.ora))
            for element in self.timp:
                print("Ziar: {}   Timp de citire: {}".format(element.numeZiar,element.timpZiar))
            print("\n")

    with open('data','r') as data:
        for lines in data.readlines():
            text=lines.split('  ')
            stud=student(text.pop(0),int(text.pop(0)))
            studenti.append(stud)
            for grup in text:
                vector=grup.split(",")
                if len(vector)>1:
                    stud.timp.append(timp(vector.pop(0).rstrip() ,int(vector.pop().rstrip())))
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

def hill(solutie):
    cp=dc(solutie)
    for i in range(len(cp)-1):
        cp[i]=sample(range(4),4)
    return cp

def test(studenti,solutie):
    solut=dc(solutie)
    for student in studenti:
        student.solutie=solut.pop(0)
    timp = 0
    ziare=[5,5,5,5]
    cs=0
    while cs != 4:
        cs=0
        for student in studenti:
            if len(student.solutie) == 0:
                cs+=1
            else:
                if timp >= student.ora:
                    if ziare[student.solutie[0]] == 5:
                        ziare[student.solutie[0]]=student.poz
                        student.timp[student.solutie[0]].start = dc(timp)
                    if (student.timp[student.solutie[0]].timpZiar == (timp - student.timp[student.solutie[0]].start)) and (ziare[student.solutie[0]] == student.poz):
                        ziare[student.solutie[0]]=5
                        student.solutie.pop(0)
        timp+=1
    return timp

if __name__ == "__main__":
    studenti=[]
    populare(studenti)
    for student in studenti:
        for timp in student.timp:
            timp.afisare()
        print()
    solutie= [
        [0, 1, 2, 3],
        [1, 0, 3, 2],
        [3, 0, 1, 2],
        [2, 1, 3, 0]
    ]
    counter = 0
    timp = test(studenti,solutie)
    while counter < 100:
        solutie_t=hill(solutie)
        timp_t=test(studenti,solutie_t)
        if timp_t<timp:
            timp = timp_t
            solutie_f=solutie_t
        counter+=1
    print ("Cel mai mic timp:{}".format(timp))
    print (solutie_f)



