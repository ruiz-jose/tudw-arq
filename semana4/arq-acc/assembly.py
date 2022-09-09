import sys
#assembler
import re

class ASSEMBLY:
     #instruction set prueba
     
    def __init__(self):
        
        #code
        self.code = []
        #instruction set
        self.instructions = {
                    "LDA" : 0x0,
                    "STA" : 0x1,
                    "ADD" : 0x2,
                    "HLT" : 0x3
        }
   
    def assembler(self, filename):
        
        #open the asm file
        try:
            f = open(filename, "r")
        except:
            print(f"Error: {filename} file not found.")

        #copy the whole file into a buffer and close the file
        buffer = f.read()
        f.close()

        #split the buffer based on new lines, we will have a list of instructions
        tokens = buffer.split("\n")

        #output buffer
        output = []
        labels = {}
        re_label = re.compile("^\w*:$")
        re_comment = re.compile("^;.*$")
        pc = 0

        for i in range(len(tokens)):
            if re_label.match(tokens[i]):
                labels[tokens[i][:-1]] = pc
            elif re_comment.match(tokens[i]):
                continue
            else:
                pc = pc + 1
        pc = 0 #set back to zero so we can show line numbers on output.

        print("|---Code.asm---|")
        #iterate through the tokens, convert them to int
        #values based on instruction set and append it to output
        for i in range(len(tokens)):
            try:
                if re_label.match(tokens[i]) or re_comment.match(tokens[i]): #skip labels and comments altogether
                    continue
                else:
                    ins = tokens[i].split()
                    if(ins[0] in self.instructions):
                        if(len(ins)==1):
                            output.append(self.instructions[ins[0]]<<6 | 0 )
                            print(pc, ins[0])
                        else:
                            if ins[1] in labels:
                                output.append(self.instructions[ins[0]]<<6 | int(labels[ins[1]]))
                                print(pc, ins[0], labels[ins[1]])
                            else:
                                output.append(self.instructions[ins[0]]<<6 | int(ins[1]))
                                print(pc, ins[0], ins[1])
                    else:
                        if(len(ins)==1) or re_comment.match(ins[1]):
                            output.append(int(ins[0]))
                            print(pc, ins[0])
                    pc = pc + 1
            except Exception as e:
                output.append(hex(0))
        print("|---end---|")    
        print()    
        self.code = list(output)

