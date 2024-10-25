#21/02/'20
import OSC, random, time
from threading import Thread


client = OSC.OSCClient()
client.connect(("127.0.0.1", 10000))

fbasso1 = [233,220,233,247,294,277,330,233,247,185,165,196,185,139,147,147,147,147,147,147,147,185,220,196,233,147,139,220,233,247,156,220,165,131,124,117,147,117] #38 elementi (in Hz)
fbasso2 = [49,37,41.5,55,58.5,62,58.5,41.5,62,70,49,62,58.5,46.5,41.5,35,46.5]   #17 elementi  (in Hz)
amount_list = [130,40,500,330,800,1000,870,1300]       #fattori da 0 a 5000
level_list_c3 = [0.2,0.48,0.6,0.3,0.8,0.35,0.15,0.9]   #fattori da 0 a 1

intervalli_t = [2,3,2.5,1]      #in secondi
t1 = intervalli_t[0]
t2 = intervalli_t[1]
t3 = intervalli_t[2]
t4 = intervalli_t[3]

intervalli_t_amount = [10,8,12,5]    #in secondi
t1a = intervalli_t_amount[0]
t2a = intervalli_t_amount[1]
t3a = intervalli_t_amount[2]
t4a = intervalli_t_amount[3]  


##----------------------------------------Controlli---------------------------


class Camera1():           #esempio di sintassi:  Camera1.frequenzamod("mod3", 667)

    def frequenzaCarrier(self,valore):

        FrequenzaCarrier = OSC.OSCMessage()
        FrequenzaCarrier.setAddress("/c1f_carrier")
        FrequenzaCarrier.append(valore)
        client.send(FrequenzaCarrier)

    def masteramount(self,valore):
    
        MasterAmount = OSC.OSCMessage()
        MasterAmount.setAddress("/c1a_master")
        MasterAmount.append(valore)
        client.send(MasterAmount)


    def frequenzaMod(self,address,valore):

        FrequenzaMod = OSC.OSCMessage()
        FrequenzaMod.setAddress("/c1f_" + address)  #ovvero: "mod1", "mod2", "mod3"
        FrequenzaMod.append(valore)
        client.send(FrequenzaMod)    

    def modamount(self,address,valore):

        ModAmount = OSC.OSCMessage()
        ModAmount.setAddress("/c1a_" + address)   #ovvero: "mod1", "mod2", "mod3"
        ModAmount.append(valore)
        client.send(ModAmount)


class Camera2():                    

    def frequenzaCarrier(self,valore):

        FrequenzaCarrier = OSC.OSCMessage()
        FrequenzaCarrier.setAddress("/c2f_carrier")
        FrequenzaCarrier.append(valore)
        client.send(FrequenzaCarrier)

    def masteramount(self,valore):
    
        MasterAmount = OSC.OSCMessage()
        MasterAmount.setAddress("/c2a_master")
        MasterAmount.append(valore)
        client.send(MasterAmount)


    def frequenzaMod(self,address,valore):

        FrequenzaMod = OSC.OSCMessage()
        FrequenzaMod.setAddress("/c2f_" + address)  #ovvero: "mod1", "mod2", "mod3"
        FrequenzaMod.append(valore)
        client.send(FrequenzaMod)    

    def modamount(self,address,valore):

        ModAmount = OSC.OSCMessage()
        ModAmount.setAddress("/c2a_" + address)   #ovvero: "mod1", "mod2", "mod3"
        ModAmount.append(valore)
        client.send(ModAmount)        


class Camera3():

    def frequenza(self,address,valore):

        Freq = OSC.OSCMessage()
        Freq.setAddress("/c3f_" + address )   #ovvero "saw1" "saw2" "quad1" "quad1" "sin" "tri"; "saw2_gl" "quad1_gl" "quad2_gl"
        Freq.append(valore)
        client.send(Freq)    

    def level(self,address,valore):

        Level = OSC.OSCMessage()
        Level.setAddress("/c3a_" + address)    #ovvero "saw1" "saw2" "quad1" "quad1" "sin" "tri"
        Level.append(valore)
        client.send(Level)
        
    def masteramount(self,valore):

        MasterAmount = OSC.OSCMessage()
        MasterAmount.setAddress("/c3a_master")
        MasterAmount.append(valore)
        client.send(MasterAmount)


camera1 = Camera1()
camera2 = Camera2()
camera3 = Camera3()


##------------------------------------------------Disordine----------------------------------


class Disordine():

    def timesleep(self):
        
        for num in intervalli_t : 
         
            maxrange = num**(len(intervalli_t))
            tP = random.uniform(0, maxrange)
            nE = (random.random()*tP)/1000    #variazioni nell'ordine di millesimi di secondo, centesimi ecc...
            
            op1 = num + nE
            op2 = num - nE
            oplist = [op1,op2]
            choice = random.choice(oplist)

            round(choice,3)

            if num == intervalli_t[0]:
                intervalli_t[0] = choice

            elif num == intervalli_t[1]:
                intervalli_t[1] = choice

            elif num == intervalli_t[2]:
                intervalli_t[2] = choice

            elif num == intervali[3]:
                intervalli_t[3] = choice     

        t1 = intervalli_t[0]
        t2 = intervalli_t[1]
        t3 = intervalli_t[2]
        t4 = intervalli_t[3]
        

    def frequenza(self,lista):
        i = 0
        for num in lista: 

            maxrange = num*(len(lista))
            fP = random.uniform(0, maxrange)
            fE = (random.random()*fP)/10000  
            
            op1 = num + fE
            op2 = num - fE
            oplist = [op1,op2]
            choice = random.choice(oplist)

            round(choice,3)
            lista[i] = choice

            i = i + 1


    def modamount(self):
        i = 0
        for num in amount_list:

            maxrange = num*(len(amount_list))
            aP = random.uniform(0, maxrange)
            aE = (random.random()*aP)/100000
            
            op1 = num + aE
            op2 = num - aE
            oplist = [op1,op2]
            choice = random.choice(oplist)
            
            round(choice,3)
            amount_list[i] = choice

            i = i + 1
        

disordine = Disordine()


##----------------------------------------Materiali musicali----------------------------------                                         

                                                 
def sequenza1(camerax,tipo,ottava=None,address=None,coefficenteT=None):                  #es: seq1(camera1,Mod,"mod3") o seq1(camera1,Carrier)
                                                
    while ottava is None:
        ottava = 1
    else:
        pass
    while coefficenteT is None:
        coefficenteT = 1
    else:
        pass    

    if tipo == "Carrier":
        i = 1
        for num in fbasso1:
            camerax.frequenzaCarrier(num*ottava)                
            
            if i == 1 or 5 or 9 or 13 or 17 or 21 or 25 or 29 or 33 or 37:
                time.sleep(t1*coefficenteT)
            elif i == 2 or 6 or 10 or 14 or 18 or 22 or 26 or 30 or 34 or 38:
                time.sleep(t2*coefficenteT)
            elif i == 3 or 7 or 11 or 15 or 19 or 23 or 27 or 31 or 35:
                time.sleep(t3*coefficenteT)
            elif i == 4 or 8 or 12 or 16 or 20 or 24 or 28 or 32 or 36:
                time.sleep(t4*coefficenteT)
                disordine.timesleep()
            i = i + 1
            
    elif tipo == "Mod":
        i = 1
        for num in fbasso1:
            camerax.frequenzaMod(address, num*ottava)     #il metodo address è necessario solo in questo caso

            if i == 1 or 5 or 9 or 13 or 17 or 21 or 25 or 29 or 33 or 37:
                time.sleep(t1*coefficenteT)
            elif i == 2 or 6 or 10 or 14 or 18 or 22 or 26 or 30 or 34 or 38:
                time.sleep(t2*coefficenteT)
            elif i == 3 or 7 or 11 or 15 or 19 or 23 or 27 or 31 or 35:
                time.sleep(t3*coefficenteT)
            elif i == 4 or 8 or 12 or 16 or 20 or 24 or 28 or 32 or 36:
                time.sleep(t4*coefficenteT)
                disordine.timesleep()
            i = i + 1

    elif tipo == "Add":
        i = 1
        for num in fbasso1:
            camerax.frequenza(address, num*ottava)

            if i == 1 or 5 or 9 or 13 or 17 or 21 or 25 or 29 or 33 or 37:
                time.sleep(t1*coefficenteT)
            elif i == 2 or 6 or 10 or 14 or 18 or 22 or 26 or 30 or 34 or 38:
                time.sleep(t2*coefficenteT)
            elif i == 3 or 7 or 11 or 15 or 19 or 23 or 27 or 31 or 35:
                time.sleep(t3*coefficenteT)
            elif i == 4 or 8 or 12 or 16 or 20 or 24 or 28 or 32 or 36:
                time.sleep(t4*coefficenteT)
                disordine.timesleep()
            i = i + 1    
        
                       
    disordine.frequenza(fbasso1)
    random.shuffle(fbasso1)

def sequenza2(camerax,tipo,ottava=None,address=None,coefficenteT=None):

    while ottava is None:
        ottava = 1
    else:
        pass
    while coefficenteT is None:
        coefficenteT = 1
    else:
        pass
   
    if tipo == "Carrier":
        i = 1
        for num in fbasso2:
            camerax.frequenzaCarrier(num*ottava)
        
            if i == 1 or 5 or 9 or 13 or 17:
                time.sleep(t1*coefficenteT)
            elif i == 2 or 6 or 10 or 14:
                time.sleep(t2*coefficenteT)
            elif i == 3 or 7 or 11 or 15:
                time.sleep(t3*coefficenteT)
            elif i == 4 or 8 or 12 or 16:
                time.sleep(t4*coefficenteT)
                disordine.timesleep()    
            i = i + 1
            
    elif tipo == "Mod":
        i = 1        
        for num in fbasso2:
            camerax.frequenzaMod(address, num*ottava)      #il metodo address è necessario solo in questo caso

            if i == 1 or 5 or 9 or 13 or 17:
                time.sleep(t1*coefficenteT)
            elif i == 2 or 6 or 10 or 14:
                time.sleep(t2*coefficenteT)
            elif i == 3 or 7 or 11 or 15:
                time.sleep(t3*coefficenteT)
            elif i == 4 or 8 or 12 or 16:
                time.sleep(t4*coefficenteT)
                disordine.timesleep()  
            i = i + 1

    elif tipo == "Add":
        i = 1
        for num in fbasso2:
            camerax.frequenza(address, num*ottava)
        
            if i == 1 or 5 or 9 or 13 or 17:
                time.sleep(t1*coefficenteT)
            elif i == 2 or 6 or 10 or 14:
                time.sleep(t2*coefficenteT)
            elif i == 3 or 7 or 11 or 15:
                time.sleep(t3*coefficenteT)
            elif i == 4 or 8 or 12 or 16:
                time.sleep(t4*coefficenteT)
                disordine.timesleep()    
            i = i + 1
            
    disordine.frequenza(fbasso2)
    random.shuffle(fbasso2)      

def amountseq(camerax,address,coefficenteA=None,coefficenteT=None):

    while coefficenteA is None:
        coefficenteA = 1
    else:
        pass    
    while coefficenteT is None:
        coefficenteT = 1
    else:
        pass    

    i = 1
    for num in amount_list:
        camerax.modamount(address,num*coefficenteA)

        if i == 1 or 5:
            time.sleep(t1a*coefficenteT)
        elif i == 2 or 6:
            time.sleep(t2a*coefficenteT)
        elif i == 3 or 7:
            time.sleep(t3a*coefficenteT)
        elif i == 4 or 8:
            time.sleep(t4a*coefficenteT)
            disordine.timesleep()
        i = i + 1        

    disordine.modamount()  
    random.shuffle(amount_list)
    random.shuffle(intervalli_t_amount)

def levelseq_c3(camerax,address,coefficenteA=None,coefficenteT=None):

    while coefficenteA is None:
        coefficenteA = 1
    else:
        pass      
    while coefficenteT is None:
        coefficenteT = 1
    else:
        pass

    i = 1
    if camerax == camera3:

        for num in level_list_c3:
            camera3.level(address,num*coefficenteA)

            if i == 1 or 5:
                time.sleep(t1a*coefficenteT)
            elif i == 2 or 6:
                time.sleep(t2a*coefficenteT)
            elif i == 3 or 7:
                time.sleep(t3a*coefficenteT)
            elif i == 4 or 8:
                time.sleep(t4a*coefficenteT)
                disordine.timesleep()
            i = i + 1

    else:
        print "Errore"
        
    random.shuffle(level_list_c3)
    random.shuffle(intervalli_t_amount)    

def glissando(camerax,address,f1,f2):

    camerax.frequenza(address,f1)
    time.sleep(1.5)
    camerax.frequenza(address,f2)

##----------------------------------------------Thread--------------------------------------------


def seq1(camerax,tipo,ottava=None,address=None,coefficenteT=None):       #es: seq1(camera1,"Mod","mod3") seq1(camera1,"Carrier")
    thread_s1 = Thread(target=sequenza1, args=(camerax,tipo,ottava,address,coefficenteT,))
    thread_s1.start()
    
def seq2(camerax,tipo,ottava=None,address=None,coefficenteT=None):
    thread_s2 = Thread(target=sequenza2, args=(camerax,tipo,ottava,address,coefficenteT,))
    thread_s2.start()
         
def amseq(camerax,address,coefficenteA=None,coefficenteT=None,):
    thread_as = Thread(target=amountseq, args=(camerax,address,coefficenteA,coefficenteT,))
    thread_as.start()

def lseq(camerax,address,coefficenteA=None,coefficenteT=None):        
    thread_ls = Thread(target=levelseq_c3, args=(camerax,address,coefficenteA,coefficenteT,))
    thread_ls.start()

def gliss(camerax,address,f1,f2):
    "Usare _gl dopo address, usare solo con Camera3"
    thread_gl = Thread(target=glissando, args=(camerax,address,f1,f2,))
    thread_gl.start()

##-----------------------------------------Algoritmo-----------------------------------------








