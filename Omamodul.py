from fcntl import I_LIST


def Sugu(ik):
    """Esimise tahe järgi määrame sugu
    :param list ik_list:järjend isikukoodi numbridest
    :rtype: str
    """
    if int(I_LIST[0])%2==0:
        sugu="naine"
    else:
        sugu="mees"
    return sugu

def Sunnikoht(a:int)->str:
    """
    """
    if 1<=a<=10:
             haigla="kuresaare Haigla"
    elif 11<=a<=19:
             haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<=a<=220:
             haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271<=a<=370:
             haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<=a<=420:
             haigla="Narva Haigla"
    elif 421<=a<=470:
             haigla="Pärnu Haigla "
    elif 471<=a<=480:
             haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491<=a<=520:
             haigla="Järvamaa Haigla (Paide)"
    elif 521<=a<=570:
             haigla="Rakvere, Tapa haigla"
    elif 571<=a<=600:
             haigla="Valga Haigla "
    elif 601<=a<=650:
             haigla="Viljandi Haigla"
    elif 651<=a<=700:
             haigla=" Lõuna-Eesti Haigla (Võru), Põlva Haigla "
    else:
        haigla=" ---"
    return haigla

def sunnipaev(ik_list:list)->str:
    """
    """
    s1=int(ik_list[0])
    y=(ik_list[1]+ik_list[2])      #aasta
    m=(ik_list[3]+ik_list[4])   #kuu
    d=int(ik_list[5]+ik_list[6])   #päev
    if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
        spaev="viga"
        #arvud.append
    else:
         if s1==1 or s1==2:
                    yy="18"
         elif s1==3 or s1==4:
                    yy="19"
         else:
                    yy="20"
         spaev=str(d)+"."+str(m)+"."+yy+(y) #ei ole 18..,19..,20..
         return spaev

def naised_mehed(ikoodid:list):
    """
    :rtype: list
    """
    naised=[]
    mehed=[]
    for kood in ikoodid:
        ik_list=list(kood)
        sugu=Sugu(ik_list)
        if sugu=="naine":
            naised.append(kood)
        else:
             mehed.append(kood)
    ikoodid.clear()
    ikoodid.extend(naised)
    ikoodid.extend(mehed)
    return ikoodid