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
        self.cycles = 0

    def loadProgram(self, code):
        self.memory = list(code)  

    def fetch(self):
        #fetch instruction
        print(f"------------------memory[{self.PC}]-------------------------")
        self.MAR = self.PC
        self.cycles += 1
        self.MDR = self.memory[self.MAR]
        self.PC += 1
        self.cycles += 1       
         #wait memory
        self.cycles += 4
        self.IR = self.MDR
        self.cycles += 1  
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
            self.cycles += 1
            self.MDR =  self.memory[self.MAR]
            self.cycles += 1       
            #wait memory
            self.cycles += 4
            self.ACC =  self.MDR
            self.cycles += 1       
            print(f"executing LDA {self.MAR}    => ACC({self.ACC}) ← memory[{self.MAR}]")
           
        elif(opcode == 0x1):
            #STA
            self.MAR = address
            self.cycles += 1       
            self.MDR = self.ACC 
            self.cycles += 1
            self.memory[self.MAR] = self.MDR 
            self.cycles += 1       
            #wait memory
            self.cycles += 4
            print(f"executing STA {self.MAR}    => memory[{self.MAR}] ← ACC({self.ACC})")
        elif(opcode == 0x2):
            #ADD
            self.MAR = address
            self.cycles += 1  
            self.MAR = self.memory[self.MAR]
            self.cycles += 1       
            #wait memory
            self.cycles += 4
            print(f"executing ADD {self.MAR}    => ACC({self.ACC + self.MDR}) ← ACC({self.ACC}) + MDR({self.MDR})")
            self.ACC = self.ACC + self.MDR 
            self.cycles += 1            
        elif(opcode == 0x3):
            #HLT
            self.HLT = True
            self.cycles += 1
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
    print(f"Program-Cycles: {cpu.cycles}")
    print("RI: ?")
    print("CPI: ?")
    print("Time CPU: ?")
    print(" -------------------------------------------")

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except:
        print("-------------------------------------------")
        print("|Usage: python cpu.py  <asm filename>      |")
        print("|Example win: python cpu.py code.asm       |")
        print("|Example linux: python3 cpu.py code.asm    |")
        print(" ------------------------------------------\n")
        exit()
    main(filename)