from enum import Enum

class opcode(Enum):
	_OP_END = 1
	_OP_NOP = 2
	_OP_INT = 3
	_OP_MOV = 4
	_OP_PUSH = 5
	_OP_POP = 6
	_OP_PUSHF = 7
	_OP_POPF = 8
	_OP_INC = 9
	_OP_DEC = 10
	_OP_ADD = 11
	_OP_SUB = 12
	_OP_MUL = 13
	_OP_DIV= 14
	_OP_MOD = 15
	_OP_REM = 16
	_OP_NOT = 17
	_OP_XOR = 18
	_OP_OR = 19
	_OP_AND = 20
	_OP_SHL = 21
	_OP_SHR = 22
	_OP_CMP = 23
	_OP_CALL = 24
	_OP_JMP = 25
	_OP_RET = 26
	_OP_JE = 27
	_OP_JNE = 28
	_OP_JG = 29
	_OP_JGE = 30
	_OP_JL = 31
	_OP_JLE = 32
	_OP_PRN = 33

class register(Enum):
	_RG_EAX = 0
	_RG_EBX = 1
	_RG_ECX = 2
	_RG_EDX = 3
	_RG_ESI = 4
	_RG_EDI = 5
	_RG_ESP = 6
	_RG_EBP = 7
	_RG_EIP = 8
	_RG_R08 = 9
	_RG_R09 = 10
	_RG_R10 = 11
	_RG_R11 = 12
	_RG_R12 = 13
	_RG_R13 = 14
	_RG_R14 = 15
	_RG_R15 = 16

regsMap = {
	"eax": register._RG_EAX,
	"ebx": register._RG_EBX,
	"ecx": register._RG_ECX,
	"edx": register._RG_EDX,
	"esi": register._RG_ESI,
	"edi": register._RG_EDI,
	"esp": register._RG_ESP,
	"ebp": register._RG_EBP,
	"eip": register._RG_EIP,
	"r08": register._RG_R08,
	"r09": register._RG_R09,
	"r10": register._RG_R10,
	"r11": register._RG_R11,
	"r12": register._RG_R12,
	"r13": register._RG_R13,
	"r14": register._RG_R14,
	"r15": register._RG_R15,
}

regset = set(regsMap.keys())

opsRev = {
    	opcode._OP_NOP:   "nop",
		opcode._OP_INT:   "int",
		opcode._OP_MOV:   "mov",
		opcode._OP_PUSH:  "push",
		opcode._OP_POP:   "pop",
		opcode._OP_PUSHF: "pushf",
		opcode._OP_POPF:  "popf",
		opcode._OP_INC:   "inc",
		opcode._OP_DEC:   "dec",
		opcode._OP_ADD:   "add",
		opcode._OP_SUB:   "sub",
		opcode._OP_MUL:   "mul",
		opcode._OP_DIV:   "div",
		opcode._OP_MOD:   "mod",
		opcode._OP_REM:   "rem",
		opcode._OP_NOT:   "not",
		opcode._OP_XOR:   "xor",
		opcode._OP_OR:    "or",
		opcode._OP_AND:   "and",
		opcode._OP_SHL:   "shl",
		opcode._OP_SHR:   "shr",
		opcode._OP_CMP:   "cmp",
		opcode._OP_CALL:  "call",
		opcode._OP_JMP:   "jmp",
		opcode._OP_RET:   "ret",
		opcode._OP_JE:    "je",
		opcode._OP_JNE:   "jne",
		opcode._OP_JG:    "jg",
		opcode._OP_JGE:   "jge",
		opcode._OP_JL:    "jl",
		opcode._OP_JLE:   "jle",
		opcode._OP_PRN:   "prn",
}

opsMap = {
    	"nop":   opcode._OP_NOP,
		"int":   opcode._OP_INT,
		"mov":   opcode._OP_MOV,
		"push":  opcode._OP_PUSH,
		"pop":   opcode._OP_POP,
		"pushf": opcode._OP_PUSHF,
		"popf":  opcode._OP_POPF,
		"inc":   opcode._OP_INC,
		"dec":   opcode._OP_DEC,
		"add":   opcode._OP_ADD,
		"sub":   opcode._OP_SUB,
		"mul":   opcode._OP_MUL,
		"div":   opcode._OP_DIV,
		"mod":   opcode._OP_MOD,
		"rem":   opcode._OP_REM,
		"not":   opcode._OP_NOT,
		"xor":   opcode._OP_XOR,
		"or":    opcode._OP_OR,
		"and":   opcode._OP_AND,
		"shl":   opcode._OP_SHL,
		"shr":   opcode._OP_SHR,
		"cmp":   opcode._OP_CMP,
		"call":  opcode._OP_CALL,
		"jmp":   opcode._OP_JMP,
		"ret":   opcode._OP_RET,
		"je":    opcode._OP_JE,
		"jne":   opcode._OP_JNE,
		"jg":    opcode._OP_JG,
		"jge":   opcode._OP_JGE,
		"jl":    opcode._OP_JL,
		"jle":   opcode._OP_JLE,
		"prn":   opcode._OP_PRN,
}

opset = set(opsMap.keys())



