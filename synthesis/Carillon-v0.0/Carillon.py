import OSC

client = OSC.OSCClient()
client.connect(("127.0.0.1", 10000))

############################################### Base function ###############################################


def m(address,internal_address,contenuto):
    """address = string; internal_address = string; contenuto = int, float, list, string"""
    message = OSC.OSCMessage(address)

    message.append(internal_address)

    if contenuto is list:
        i = 0
        for item in contenuto:
            message.append(contenuto[i])
            i = i + 1
    else:
        message.append(contenuto)

    client.send(message)


#################################### Controlling abstractions for data flow ################################


class Clockz(object):

    def __init__(self,object_n):
        self.object_n = object_n
    
    def metro(self,x=None,y=None):
        object_n = self.object_n

        if x is not None:
            m("/clock" + str(object_n),"metro_x",x)
        else:
            pass

        if y is not None:
            m("/clock" + str(object_n),"metro_y",y)
        else:
            pass

    def delta(self,deltavalue):
        object_n= self.object_n
        m("/clock" + str(object_n),"delta",deltavalue)


class PixdataMIDI(object):

    def __init__(self,object_n):
        self.object_n = object_n
    
    def greylimiter(self,greyvalue):
        object_n = self.object_n
        m("/pixm" + str(object_n),"greylimiter",greyvalue)

    def steps(self,step_n):
        object_n = self.object_n
        m("/pixm" + str(object_n),"steps",step_n)


################################# Controlling abstractions for audio flow ###################################


class Organo(object):

    def __init__(self,object_n):
        self.object_n = object_n
        
    def armonics(self,arm_list):
        object_n = self.object_n
        i = 0
        j = 1
        for item in arm_list:
            m("/organo"+str(object_n),"armonics",[str(j),arm_list[i]])
            i = i + 1
            j = j + 1
    
    def amplifier(self,level=None,resonance=None):
        object_n = self.object_n
        if level is not None:
            if level == "mute":
                level = 0
            elif level == "unumte":
                level = 1
            else:
                pass
            m("/organo"+str(object_n),"amplifier",["level",level])
        else:
            pass
        
        if resonance is not None:
            m("/organo"+str(object_n),"amplifier",["resonance",resonance])
        else:
            pass
     
    def attenuatori(self,value):
        object_n = self.object_n
        m("/organo"+str(object_n),"attenuatori",value)


class SawOrgano(object):

    def __init__(self,object_n):
        self.object_n = object_n

    def armonics(self,arm_list):
        object_n = self.object_n
        i = 0
        j = 1
        for item in arm_list:
            m("/saw"+str(object_n),"armonics",[str(j),arm_list[i]])
            i = i + 1
            j = j + 1

    def amplifier(self,level=None,resonance=None):
        object_n = self.object_n
        if level is not None:
            if level == "mute":
                level = 0
            elif level == "unumte":
                level = 1
            else:
                pass
            m("/saw"+str(object_n),"amplifier",["level",level])
        else:
            pass
        
        if resonance is not None:
            m("/saw"+str(object_n),"amplifier",["resonance",resonance])
        else:
            pass

    def phaseCaos(self,general_onoff=None,armonics_onoff=None,freq=None,deltavalue=None):
        object_n = self.object_n
        if general_onoff is not None:
            m("/saw"+str(object_n),"phaseCaos",["general_onoff",general_onoff])
        else:
            pass

        if armonics_onoff is not None:
            m("/saw"+str(object_n),"phaseCaos",["armonics_onoff",armonics_onoff])
        else:
            pass

        if freq is not None:
            m("/saw"+str(object_n),"phaseCaos",["freq",freq])
        else:
            pass

        if deltavalue is not None:
            m("/saw"+str(object_n),"phaseCaos",["delta",deltavalue])
        else:
            pass

    def attenuatori(self,value):
        object_n = self.object_n
        m("/saw"+str(object_n),"attenuatori",value)
    

class Mixer(object): #non sono previsti multipli dell'oggetto Mixer,quindi nessuna variabile object_n all'interno della classe

    def group(self,groupname,level):
        m("/mixer","groups",["group"+groupname,level])

    def reverb(self,dry=None,wet=None,roomsize=None,damping=None,width=None,outgain=None,onoff=None):
        if dry is not None:
            m("/mixer","reverb",["dry",dry])
        else:
            pass

        if wet is not None:
            m("/mixer","reverb",["wet",wet])
        else:
            pass

        if roomsize is not None:
            m("/mixer","reverb",["roomsize",roomsize])
        else:
            pass

        if damping is not None:
            m("/mixer","reverb",["damping",damping])
        else:
            pass

        if width is not None:
            m("/mixer","reverb",["width",width])
        else:
            pass

        if outgain is not None:
            m("/mixer","reverb",["outgain",outgain])
        else:
            pass
        
        if onoff == "on":
            m("/mixer","reverb",["onoff",1])
        elif onoff == "off":
            m("/mixer","reverb",["onoff",0])
        else:
            pass

    def output(self,level):
        
        if level == "mute":
            m("/mixer","mastermute",1)
        elif level == "unmute":
            m("/mixer","mastermute",0)
        else:
            pass
        m("/mixer","masterlevel",level)
        
