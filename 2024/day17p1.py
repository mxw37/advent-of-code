input_file = [i.strip() for i in open("day17input.txt","r").readlines()]

registers = {"A":0,"B":0,"C":0}

registers["A"] = int(input_file[0].split(": ")[1])
registers["B"] = int(input_file[1].split(": ")[1])
registers["C"] = int(input_file[2].split(": ")[1])

instructions = [int(i) for i in input_file[4].split(": ")[1].split(",")]

def get_co(co):
    if 0 <= co <= 3:
        return co
    elif co == 4:
        return registers["A"]
    elif co == 5:
        return registers["B"]
    elif co == 6:
        return registers["C"]

ip = 0

output = []

while ip < len(instructions):
    opcode = instructions[ip]
    operand = instructions[ip+1]
    if opcode == 0:
        registers["A"] = int(registers["A"]/(2**(get_co(operand))))
    elif opcode == 1:
        registers["B"] ^= operand
    elif opcode == 2:
        registers["B"] = (get_co(operand) % 8)
    elif opcode == 3:
        if registers["A"] != 0:
            ip = operand
    elif opcode == 4:
        registers["B"] ^= registers["C"]
    elif opcode == 5:
        output.append(str(get_co(operand)%8))
    elif opcode == 6:
        registers["B"] = int(registers["A"]/(2**(get_co(operand))))
    elif opcode == 7:
        registers["C"] = int(registers["A"]/(2**(get_co(operand))))
    if opcode != 3 or registers["A"] == 0:
        ip += 2

print(",".join(output))
