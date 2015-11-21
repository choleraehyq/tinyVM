import itertools

from memory import Memory
from program import Program
from codes import *
from exception import ParseException, NotImplementedException
from utils import Int

class Vm(object):

    def __init__(self, srcfile):
        self.src = srcfile
        self.m = Memory(17)
        self.p = Program()

    def run(self):
        self.parse()
        for i in self.p.instrs:
            self.runInstruction(i)

    def runInstruction(self, instrIndex):
        instr = self.p.instrs[instrIndex]
        a0, a1 = instrIndex*2, (instrIndex*2)+1
        if instr == opcode._OP_NOP:
            pass
        elif instr == opcode._OP_INT:
            raise NotImplementedException
        elif instr == opcode._OP_MOV:
            self.p.args[a0] = Int(int(self.p.args[a1]))
        elif instr == opcode._OP_PUSH:
            self.m.push_stack(self.p.args[a0])
        elif instr == opcode._OP_POP:
            self.p.args[a0] = Int(self.m.pop_stack())
        elif instr == opcode._OP_PUSHF:
            self.m.push_stack(self.m.FLAGS)
        elif instr == opcode._OP_POPF:
            self.m.FLAGS = self.m.pop_stack()
        elif instr == opcode._OP_INC:
            self.p.args[a0] += Int(1)
        elif instr == opcode._OP_DEC:
            self.p.args[a0] -= Int(1)
        elif instr == opcode._OP_ADD:
            self.p.args[a0] += self.p.args[a1]
        elif instr == opcode._OP_SUB:
            self.p.args[a0] -= self.p.args[a1]
        elif instr == opcode._OP_MUL:
            self.p.args[a0] *= self.p.args[a1]
        elif instr == opcode._OP_DIV:
            self.p.args[a0] /= self.p.args[a1]
        elif instr == opcode._OP_MOD:
            self.m.remainder = self.p.args[a0] % self.p.args[a1]
        elif instr == opcode._OP_REM:
            self.p.args[a0] = Int(self.m.remainder)
        elif instr == opcode._OP_AND:
            self.p.args[a0] &= self.p.args[a1]
        elif instr == opcode._OP_SHL:
            if self.p.args[a1] > Int(0):
                self.p.args[a0] <<= self.p.args[a1]
        elif instr == opcode._OP_SHR:
            if self.p.args[a1] > Int(0):
                self.p.args[a0] >>= self.p.args[a1]
        elif instr == opcode._OP_NOT:
            self.p.args[a0] = ~self.p.args[a0]
        elif instr == opcode._OP_OR:
            self.p.args[a0] |= self.p.args[a1]
        elif instr == opcode._OP_XOR:
            self.p.args[a0] ^= self.p.args[a1]
        elif instr == opcode._OP_CMP:
            if self.p.args[a0] == self.p.args[a1]:
                self.m.FLAGS = 0x1
            elif self.p.args[a0] > self.p.args[a1]:
                self.m.FLAGS = 0x2
            else:
                self.m.FLAGS = 0x0
        elif instr == opcode._OP_CALL:
            self.m.push_stack(instrIndex)
            instrIndex = int(self.p.args[a0])-1
        elif instr == opcode._OP_JMP:
            instrIndex = int(self.p.args[a0])-1
        elif instr == opcode._OP_RET:
            instrIndex =  self.m.pop_stack()
        elif instr == opcode._OP_JE:
            if self.m.FLAGS & 0x1 != 0:
                instrIndex = int(self.p.args[a0])
        elif instr == opcode._OP_JNE:
            if self.m.FLAGS & 0x1 == 0:
                instrIndex = int(self.p.args[a0])
        elif instr == opcode._OP_JG:
            if self.m.FLAGS & 0x2 != 0:
                instrIndex = int(self.p.args[a0])
        elif instr == opcode._OP_JGE:
            if self.m.FLAGS & 0x3 != 0:
                instrIndex = int(self.p.args[a0])
        elif instr == opcode._OP_JL:
            if self.m.FLAGS & 0x3 == 0:
                instrIndex = int(self.p.args[a0])
        elif instr == opcode._OP_JLE:
            if self.m.FLAGS & 0x2 == 0:
                instrIndex = int(self.p.args[a0])
        elif instr == opcode._OP_PRN:
            print(a0)

    def parse_value(self, tok, instrIndex, argIndex):
        number = toValue(tok)
        self.p.args[(instrIndex * 2) + argIndex] = number
        return True

    def parse_address(self, tok, instrIndex, argIndex):
        if tok.startswith('['):
            i = toValue(tok)
            self.p.args[(instrIndex*2)+argIndex] = self.m.heap[i]
            return True
        return False

    def parse_register(self, tok, instrIndex, argIndex):
        if tok in regset:
            reg = regsMap[tok]
            self.p.args[(instrIndex*2)+argIndex] = self.m.registers[reg]
            return True
        return False

    def parse_instr(self, tok):
        if tok in opset:
            op = opsMap[tok]
            self.p.instrs.append(op)
            return True
        return False

    def parse_label_value(self, tok, instrIndex, argIndex):
        ret = True
        try:
            label = Int(self.p.labels[tok])
            self.p.args[(instrIndex*2)+argIndex] = label
        except KeyError:
            ret = False
        return ret

    def parse_label_def(self, tok):
        if tok.endswith(':'):
            label = tok[:len(tok)-1]
            if label in regset:
                raise ParseException("register name {} cannot be used as a label".format(label))
            if label in self.p.labels.keys():
                raise ParseException("label name {} already exists".format(label))
            self.p.labels[label] = len(self.p.instrs)
            return True
        return False

    def parse(self):
        lines = []

        for line in self.src:
            toks = parse_line(line)
            lines.append(toks)
            hasInstr = False

            for tok in toks:
                if tok.startswith('#'):
                    break
                if self.parse_label_def(tok):
                    if hasInstr:
                        raise ParseException("cannot define label " + tok + " after an instruction in the same line")
                    continue
                if self.parse_instr(tok):
                    hasInstr = True
                    continue

        self.p.args = [Int(0) for i in range(len(self.p.instrs) * 2)]

        instrIndex = 0
        argIndex = 0
        for toks in lines:
            hasInstr = False
            for tok in toks:
                if tok.startswith('#'):
                    continue
                if tok.endswith(':'):
                    continue
                if tok in opset:
                    instrIndex += 1
                    hasInstr = True
                    continue
                if not hasInstr:
                    raise ParseException("found argument token " + tok + " without instruction")
                if self.parse_register(tok, instrIndex, argIndex) or \
                    self.parse_label_value(tok, instrIndex, argIndex) or \
                    self.parse_address(tok, instrIndex, argIndex):
                    argIndex += 1
                    continue
                if self.parse_value(tok, instrIndex, argIndex):
                    argIndex += 1

        self.p.instrs.append(opcode._OP_END)


def parse_line(line):
    tokens = []
    line = line.strip()
    for i in line.split(' '):
        tokens.extend(i.split(','))
    tokens = list(itertools.filterfalse(lambda x: x == "", tokens))
    tokens = [x.lower() for x in tokens]
    return tokens

def toValue(tok):
    sepIndex = tok.find('|')
    base = 0
    val = tok
    if sepIndex > 0 and sepIndex < len(tok)-1:
        val = tok[:sepIndex]
        baseFlag = tok[sepIndex+1:]
        base = {
            'h': 16,
            'd': 10,
            'o': 8,
            'b': 2,
        }[baseFlag]
    elif tok.startswith('0') and not tok[1].isdigit():
        val = tok[2:]
        baseFlag = tok[1]
        base = {
            'h': 16,
            'd': 10,
            'o': 8,
            'b': 2,
        }[baseFlag]
    i = parse_int(val, base)
    return Int(i)

def parse_int(s, base):
    if not is_valid_number(s, base):
        raise ValueError("{0} is not a valid number in base {1}".format(s, base))
    ret = 0
    for i in s:
        if i >= 'a' and i <= 'f':
            i = ord(i) - ord('a') + 10
        else:
            i = ord(i) - ord('0')
        ret = ret * base + i
    return ret

def is_valid_number(s, base):
    for i in s:
        flag = False
        if i >= '0' and i <= '9':
            i = ord(i) - ord('0')
            flag = True
        elif i >= 'a' and i <= 'f':
            i = ord(i) - ord('a') + 10
            flag = True
        if not flag:
            return False
        if i > base:
            return False
    return True




