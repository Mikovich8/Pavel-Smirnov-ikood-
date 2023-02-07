from math import *
from random import *
from Omamodul import *
# 03/02/23
arvud=[]
while True:
    ik=input("Anna isikukood: ") #str
    if len(ik)!=11:
        print("Liiga palju või liiga vähe sümboleid. Sisesta veel kord: ")
        arvud.append(ik)
    else:
        print("Isikukoodi kontroll")
        ik_list=list(ik)
        s1=int(ik_list[0]) #"1"->1
        if s1 not in [1,2,3,4,5,6]:
            print("Esimene sümbol ei ole õige")
            arvud.append(ik)
        else:
            print("Esimene sümbol on õige")
            spaev=sunnipaev(ik_list)
            if spaev=="viga":
                arvud.append(ik)
            else:
        
             #
             print(f"Sünnipäev on {spaev}")
             print("Viimane number: {ik_list[-1]}")
             hhh=int(ik_list[8]+ik_list[9]+ik_list[10])
             #
             haigla=Sunnikoht(hhh)
             #
             if 1<=hhh<=10:
                 haigla="kuresaare Haigla"
             elif 11<=hhh<=19:
                 haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
             elif 21<=hhh<=220:
                 haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
             elif 271<=hhh<=370:
                 haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
             elif 371<=hhh<=420:
                 haigla="Narva Haigla"
             elif 421<=hhh<=470:
                 haigla="Pärnu Haigla "
             elif 471<=hhh<=480:
                 haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
             elif 491<=hhh<=520:
                 haigla="Järvamaa Haigla (Paide)"
             elif 521<=hhh<=570:
                 haigla="Rakvere, Tapa haigla"
             elif 571<=hhh<=600:
                 haigla="Valga Haigla "
             elif 601<=hhh<=650:
                 haigla="Viljandi Haigla"
             elif 651<=hhh<=700:
                 haigla=" Lõuna-Eesti Haigla (Võru), Põlva Haigla "
             else:
                 haigla=" ---"

             #
             if s1 in [1,3,5]:        
                        print("Mees")
             if s1 in [2,4,6]:        
                        print("naine")
        a1=int(ik[0])*1
        b1=int(ik[1])*2
        b2=int(ik[2])*3
        b3=int(ik[3])*4
        b4=int(ik[4])*5
        b5=int(ik[5])*6
        b6=int(ik[6])*7
        b7=int(ik[7])*8
        b8=int(ik[8])*9
        b9=int(ik[9])*1

        s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
        print(s11)
        
print(isikukoodid) #
isikukoodid=naised_mehed(isikukoodid) #sort alguses naised ja pärast mehed
print(isikukoodid)
arvud=list(map(int,arvud))
arvud.sort()
print(arvud)