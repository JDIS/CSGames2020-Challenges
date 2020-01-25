import re

REGISTERS = {
    '$t0': 0,
    '$t1': 0,
    '$t2': 0,
    '$t3': 0,
    '$s0': 0,
    '$s1': 0,
    '$s2': 0,
    '$s3': 0,
    '$zero': 0,
    '$v0': 0,
    '$a0': 0,
    '$a1': 0,
    '$ra': 0,
    '$sp': 0,
    'pc': 0,
    'lo': 0
}


def ADD(d, s, t):
    REGISTERS[d] = REGISTERS[s] + REGISTERS[t]

def ADDI(d, s, imm):
    REGISTERS[d] = REGISTERS[s] + int(imm)

def OR(d, s, t):
    REGISTERS[d] = REGISTERS[s] | REGISTERS[t]

def ORI(d, s, imm):
    REGISTERS[d] = REGISTERS[s] | int(imm)

def SUB(d, s, t):
    REGISTERS[d] = REGISTERS[s] - REGISTERS[t]

def AND(d, s, t):
    REGISTERS[d] = REGISTERS[s] & REGISTERS[t]

def XOR(d, s, t):
    REGISTERS[d] = REGISTERS[s] ^ REGISTERS[t]

def MULT(s, t):
    REGISTERS['lo'] = REGISTERS[s] * REGISTERS[t]

def DIV(s, t):
    REGISTERS['lo'] = int(REGISTERS[s] / REGISTERS[t])

def MFLO(d):
    REGISTERS[d] = REGISTERS['lo']

def J(target):
    REGISTERS['pc'] = int(target)
    return True

def JAL(target):
    REGISTERS['ra'] = REGISTERS['pc'] + 1
    REGISTERS['pc'] = int(target)
    return True

def JR(s):
    REGISTERS['pc'] = REGISTERS['ra']
    return True

def BEQ(s, t, offset):
    if REGISTERS[s] == REGISTERS[t]:
        REGISTERS['pc'] += int(offset)
        return True

def get_address(offset_register: str):
    match = re.match(r'(.*)\((.*)\)', offset_register)
    s = match.group(2)
    return REGISTERS[s] + int(match.group(1))

def SW(t, offset_register):
    address = get_address(offset_register)
    RAM[address] = REGISTERS[t]

def LW(t, offset_register):
    address = get_address(offset_register)
    REGISTERS[t] = RAM[address]

FUNCTIONS = {
    "AJOUT": ADD,
    "AJOUTI": ADDI,
    "OU": OR,
    "OUI": ORI,
    "SOUS": SUB,
    "ET": AND,
    "XOR": XOR,
    "MULTI": MULT,
    "DIVI": DIV,
    "BOUGELO": MFLO,
    "SAUT": J,
    "SAUTAL": JAL,
    "SAUTR": JR,
    "BEQ": BEQ,
    "SAUVW": SW,
    "LOADW": LW
}

RAM = {}

data ='''30
AJOUTI $s0 $zero 4323
AJOUTI $s1 $zero 438
AJOUT $s1 $s1 $s0
AJOUTI $s2 $zero 2344
AJOUT $t0 $s0 $s2
AJOUTI $s3 $zero 670
XOR $t1 $s0 $s3
AJOUTI $t1 $t1 -4000
ET $t2 $s3 $s1
OU $t3 $t2 $s2
AJOUTI $t0 $zero 0
AJOUTI $t1 $zero 100
BEQ $t0 $t1 6
AJOUTI $s3 $s3 5
SOUS $t2 $t1 $t0
OU $s3 $s3 $t2
AJOUTI $t0 $t0 1
SAUT 12
SAUTAL 21
AJOUT $s2 $s2 $v0
SAUT 30
SAUVW $s0 0($sp)
SAUVW $s1 4($sp)
AJOUTI $s0 $zero 4323
AJOUTI $s1 $zero 438
AJOUT $s1 $s1 $s0
XOR $v0 $s1 $s0
LOADW $s1 4($sp)
LOADW $s0 0($sp)
SAUTR $ra'''


def main():
    # Input
    raw_input = data.split('\n')
    n = int(raw_input[0])
    instructions = raw_input[1:n+1]

    # Compute
    while REGISTERS['pc'] < n:
        instruction = instructions[REGISTERS['pc']].split(' ')

        jump = FUNCTIONS.get(instruction[0])(*instruction[1:])
        if not jump:
            REGISTERS['pc'] += 1

    # Result
    # print(REGISTERS['$t0'])
    # print(REGISTERS['$t1'])
    # print(REGISTERS['$t2'])
    # print(REGISTERS['$t3'])
    # print(REGISTERS['$s0'])
    # print(REGISTERS['$s1'])
    # print(REGISTERS['$s2'])
    # print(REGISTERS['$s3'])
    # print(REGISTERS['$v0'])

    print(REGISTERS['$s0'] + REGISTERS['$s1'] + REGISTERS['$s2'] + REGISTERS['$s3'])



if __name__ == '__main__':
    main()
