from operator import itemgetter
import numpy as np

# definitions of logic functions
def logic_AND(in_list):
    ans = bool(int(in_list[0]))
    for i in range(len(in_list)):
        ans = ans and bool(int(in_list[i]))
    return ans

def logic_OR(in_list):
    ans = bool(int(in_list[0]))
    for i in range(len(in_list)):
        ans = ans or bool(int(in_list[i]))
    return ans

def logic_NOT(in_list):
    ans = not bool(int(in_list[0]))
    if (ans==1):
        return 1
    else:
        return 0

def logic_NAND(in_list):
    ans = bool(int(in_list[0]))
    for i in range(len(in_list)):
        ans = ans and bool(int(in_list[i]))
    if(ans==1):
        return 0
    else:
        return 1
def logic_NOR(in_list):
    ans = bool(int(in_list[0]))
    for i in range(len(in_list)):
        ans = ans or bool(int(in_list[i]))
    if (ans==1):
        return 0
    else:
        return 1


def logic_XOR(in_list):
    ans = bool(int(in_list[0]))
    for i in range(1, len(in_list)):
        ans = np.logical_xor(ans, bool(int(in_list[i])))
    if (ans == 1):
        return 1
    else:
        return 0

def logic_XNOR(in_list):
    ans = bool(int(in_list[0]))
    for i in range(1, len(in_list)):
        ans = np.logical_xor(ans, bool(int(in_list[i])))
    if (len(in_list)==2 | len(input_list) % 2 == 0):
        if (ans == 1):
            return 1
        else:
            return 0
    else:
        if (ans == 1):
            return 0
        else:
            return 1

#read netlist from a text file
file_netlist = open("netlist.txt", "r")
data = file_netlist.readlines()
file_netlist.close()
print(data)
#split netlist lines to a list
line = []
for i in range(len(data)):
    line.append(data[i].split())

#levelize the circuit
for index in range(len(line)):
    line[index].append([])

line = sorted(line, key=itemgetter(0))

#solve the combinational circuit step by step
output_global_list = []
output_global_val = []
for X in line:
    input_list = []
    no_of_inputs = int(X[2])
    no_of_outputs = int(X[3])
    for i in range(no_of_inputs):
        input_list.append(X[4 + i])

    for i in range(no_of_outputs):
        output_global_list.append(X[4 + i + no_of_inputs])

    if(int(X[0])>1):
        for i in range(no_of_inputs):
            if input_list[i] != 0 or input_list[i] != 1 :
                for j in range(len(output_global_list)):
                    if (input_list[i]) == output_global_list[j]:
                        input_list[i] = output_global_val[j]

    if X[1] == 'AND':
        X[-1] = logic_AND(input_list)
        output_global_val.append(X[-1])
    elif X[1] == 'OR':
        X[-1] = logic_OR(input_list)
        output_global_val.append(X[-1])
    elif X[1] == 'NOT':
        X[-1] = logic_NOT(input_list)
        output_global_val.append(X[-1])
    elif X[1] == 'NAND':
        X[-1] = logic_NAND(input_list)
        output_global_val.append(X[-1])
    elif X[1] == 'NOR':
        X[-1] = logic_NOR(input_list)
        output_global_val.append(X[-1])
    elif X[1] == 'XOR':
        X[-1] = logic_XOR(input_list)
        output_global_val.append(X[-1])
    elif X[1] == 'XNOR':
        X[-1] = logic_XNOR(input_list)
        output_global_val.append(X[-1])
    print("internal state=", X)
print("Final Output= ", bool(output_global_val[-1]))