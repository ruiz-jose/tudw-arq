import sys
from assembly import ASSEMBLY

class CPU:
    def __init__(self):
        
        #Registers PC, ACC, IR, MDR, MAR
        self.PC = 0
        self.ACC = 0
        self.IR = 0
        self.MDR = 0
        self.MAR = 0

        #RAM or self.memory, 6 bit address bus --> 2^6 = 64 bytes of RAM
        self.memory = [0]*64

        #Flags
        self.HLT = False

    def loadProgram(self, code):
        self.memory = list(code)  

    def fetch(self):
        #decode instruction from opcode by masking higher 6 bits
        print(f"------------------memory[{self.PC}]-------------------------")
        self.MAR = self.PC
        self.MDR = self.memory[self.MAR]
        self.PC += 1
        self.IR = self.MDR
        print (f"fetching memory[{self.PC-1}] => IR({self.IR}) ← PC({self.PC-1})")

    def execute(self):
        #decode instruction from opcode by masking higher 6 bits
        opcode = (self.IR >> 6)
        address = (self.IR & 0x3F)
        #print(f"IR (opcode|address)= {opcode}|{address}")
        
        #execute
        if(opcode == 0x0):
            #LDA
            self.MAR =  address
            self.MDR =  self.memory[self.MAR]
            self.ACC =  self.MDR
            print(f"executing LDA {address}    => ACC({self.ACC}) ← memory[{address}]")
           
        elif(opcode == 0x1):
            #STA
            self.MAR = address
            self.MDR = self.ACC 
            self.memory[self.MAR] = self.MDR 
            print(f"executing STA {address}    => memory[{address}] ← ACC({self.ACC})")
        elif(opcode == 0x2):
            #ADD
            self.MDR = self.memory[address]
            print(f"executing ADD {address}    => ACC({self.ACC + self.MDR}) ← ACC({self.ACC}) + MDR({self.MDR})")
            self.ACC = self.ACC + self.MDR           
        elif(opcode == 0x3):
            #HLT
            self.HLT = True
            print("executing HLT      => stop CPU")
        else:
            print(f"Illegal opcode {hex(opcode)}")


def main(filename):
    cpu = CPU()
    asm = ASSEMBLY()
    
    asm.assembler(filename)
    cpu.loadProgram(asm.code)

    while not cpu.HLT:
        
        try:
            #stage fetch
            cpu.fetch()
           
            #stage execution
            cpu.execute()
            
        except Exception as e:
            print("HALTING System...")
            break;
    print(" ---------------------------------------------------")
    print("Program-Cycles: ?")
    print("RI: ?")
    print("CPI: ?")
    print("Time CPU: ?")
    print(" -------------------------------------------")

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except:
        print(" -------------------------------------------")
        print("|Usage: python cpu.py  <asm filename>      |")
        print("|Example win: python cpu.py code.asm       |")
        print("|Example linux: python3 cpu.py code.asm    |")
        print(" ------------------------------------------\n")
        exit()
    main(filename)