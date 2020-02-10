from copy import deepcopy as dc
from random import randint as random
from random import shuffle as shuffle
from math import inf 

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

def alg(solutie):
    sol = []
    solu = []
    piece = 99999999
    for element in solutie:
        for elm in element:
            sol.append(elm)
    while piece > 0.5*len(solutie):
        piece=random(4,len(solutie))
    poz=random(0,len(solutie)-piece)
    pozf=poz+piece
    genes=sol[poz:pozf]
    genes.shuffle()
    counter=0
    for i in range(poz,pozf):
        sol[i]=genes[counter]
        counter+=1
    counter = 0
    c = 0
    for i in sol:
        solu[c].append(i)
        counter+=1
        if counter == 5:
            c+=1
            counter=0
    return solu

def test(studenti,solutie):
    for student in studenti:
        student.solutie=solutie.pop(0)
    timp = 0
    ziare=[0,0,0,0]
    cs=0
    while cs != 4:
        cs=0
        for student in studenti:
            if len(student.solutie) == 0:
                cs+=1
            else:
                if timp >= student.start:
                    if ziare[student.solutie[0]] == 0:
                        ziare[student.solutie[0]]=student.poz
                        student.timp[student.solutie[0]].start = timp
                    if student.timp[student.solutie[0]].timpZiar == (timp - student.timp[student.solutie[0]].start) and ziare[student.solutie[0]] == student.poz:
                        ziare[student.solutie[0]]=0
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
    solutie=[[],[],[],[]]
    solutie_t=alg(solutie)
    counter = 0
    timp = test(studenti,solutie)
    while counter < 50000:
        timp_t=test(studenti,solutie_t)
        if timp_t<timp:
            timp = timp_t
    print (timp)