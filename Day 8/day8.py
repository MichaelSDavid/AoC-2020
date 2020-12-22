import re

# Part 1
with open("input.txt") as f:
    program = [(op, int(arg)) for op, arg in re.findall(r"(\w+) ([+-]\d+)", f.read())]


ops = {
    "acc": (lambda arg, ip, acc: (acc + arg, ip + 1)),
    "nop": (lambda arg, ip, acc: (acc, ip + 1)),
    "jmp": (lambda arg, ip, acc: (acc, ip + arg)),
}


def exe(prog, ip=0, acc=0, hist=None):
    if hist is None:
        hist = set()
    if ip in hist or ip < 0:
        return False, acc
    if ip == len(prog):
        return True, acc
    op, arg = prog[ip]
    new_acc, new_ip = ops[op](arg, ip, acc)
    return exe(prog, new_ip, new_acc, hist | {ip})


print("A1:", exe(program)[1])

# Part 2
for i, (op, arg) in enumerate(program):
    if op != "acc":
        new_op = "nop" if op == "jmp" else "nop"
        p = program[:]
        p[i] = (new_op, arg)
        success, acc = exe(p)
        if success:
            print("A2:", acc)
            break
