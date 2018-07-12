class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate): # IS-A
    #calling parent constructor(always happen first),inherite data from logicgate
    #inherite label for gates
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.PinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutPut()
    def getPinB(self):
        return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate): # IS-A

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPinA() == 1 and self.getPinB()== 1:
            return 1
        else:
            return 0
class OrGate(BinaryGate): # IS-A
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPinA() == 1 or self.getPinB() == 1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate): # IS-A
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate): # IS-A
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin() == 1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate

def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()
