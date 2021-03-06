from constant import Constant
from opcodes import *

ops = [(None, 0)] * 0xFF

# General

def nop(frame, machine):
    pass
ops[OP_NOP] = (nop, 0)

# Frame control

def ret(frame, machine):
    val = frame.pop_operand()
    machine.pop_frame()
    machine.top_frame().push_operand(val)
ops[OP_RET] = (ret, 0)

# Stack management

def ld0(frame, machine):
    frame.push_operand(0)
ops[OP_LD0] = (ld0, 0)

def ld1(frame, machine):
    frame.push_operand(1)
ops[OP_LD1] = (ld1, 0)

def ldn(frame, machine):
    frame.push_operand(None)
ops[OP_LDN] = (ldn, 0)

def ldc(frame, machine, const):
    val = machine.get_constant(Constant.VALUE, const)
    frame.push_operand(val)
ops[OP_LDC] = (ldc, 1)

def ldl(frame, machine, idx):
    val = frame.get_slot(idx)
    frame.push_operand(val)
ops[OP_LDL] = (ldl, 1)

def st0(frame, machine, idx):
    frame.set_slot(idx, 0)
ops[OP_ST0] = (st0, 1)

def st1(frame, machine, idx):
    frame.set_slot(idx, 1)
ops[OP_ST1] = (st1, 1)

def stn(frame, machine, idx):
    frame.set_slot(idx, None)
ops[OP_STN] = (stn, 1)

def stc(frame, machine, idx, const):
    val = machine.get_constant(Constant.VALUE, const)
    frame.set_slot(idx, val)
ops[OP_STC] = (stc, 2)

def stl(frame, machine, idx):
    val = frame.pop_operand()
    frame.set_slot(idx, val)
ops[OP_STL] = (stl, 1)

def pop(frame, machine):
    frame.pop_operand()
ops[OP_POP] = (pop, 0)

def dup(frame, machine):
    val = frame.pop_operand()
    frame.push_operand(val)
    frame.push_operand(val)
ops[OP_DUP] = (dup, 0)

def swp(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    frame.push_operand(a)
    frame.push_operand(b)
ops[OP_SWP] = (swp, 0)

# Arrays

def anw(frame, machine):
    size = frame.pop_operand()
    frame.push_operand([None] * size)
ops[OP_ANW] = (anw, 0)

def asz(frame, machine):
    arr = frame.pop_operand()
    frame.push_operand(len(arr))
ops[OP_ASZ] = (asz, 0)

def ald(frame, machine):
    idx = frame.pop_operand()
    arr = frame.pop_operand()
    if isinstance(arr, str):
        # Special case treat string as C-style string
        frame.push_operand(ord(arr[idx]))
    else:
        frame.push_operand(arr[idx])
ops[OP_ALD] = (ald, 0)

def ast(frame, machine):
    val = frame.pop_operand()
    idx = frame.pop_operand()
    arr = frame.pop_operand()
    arr[idx] = val
ops[OP_AST] = (ast, 0)

def aps(frame, machine):
    val = frame.pop_operand()
    arr = frame.pop_operand()
    arr.append(val)
ops[OP_APS] = (aps, 0)

def apo(frame, machine):
    arr = frame.pop_operand()
    frame.push_operand(arr.pop())
ops[OP_APO] = (apo, 0)

# Maps

def mnw(frame, machine):
    frame.push_operand(dict())
ops[OP_MNW] = (mnw, 0)

def msz(frame, machine):
    tbl = frame.pop_operand()
    frame.push_operand(len(tbl))
ops[OP_MSZ] = (msz, 0)

def mld(frame, machine):
    key = frame.pop_operand()
    tbl = frame.pop_operand()
    frame.push_operand(tbl.get(key))
ops[OP_MLD] = (mld, 0)

def mst(frame, machine):
    val = frame.pop_operand()
    key = frame.pop_operand()
    tbl = frame.pop_operand()
    tbl[key] = val
ops[OP_MST] = (mst, 0)

def mrm(frame, machine):
    key = frame.pop_operand()
    tbl = frame.pop_operand()
    del tbl[key]
ops[OP_MRM] = (mrm, 0)

def mct(frame, machine):
    key = frame.pop_operand()
    tbl = frame.pop_operand()
    frame.push_operand(1 if key in tbl else 0)
ops[OP_MCT] = (mct, 0)

def mky(frame, machine):
    tbl = frame.pop_operand()
    frame.push_operand(list(tbl.keys()))
ops[OP_MKY] = (mky, 0)

def mvl(frame, machine):
    tbl = frame.pop_operand()
    frame.push_operand(list(tbl.values()))
ops[OP_MVL] = (mvl, 0)

# Tuples

def tnw(frame, machine, size):
    args = [frame.pop_operand() for x in range(size)]
    args.reverse()
    frame.push_operand(tuple(args))
ops[OP_TNW] = (tnw, 1)

def tsz(frame, machine):
    tpl = frame.pop_operand()
    frame.push_operand(len(tpl))
ops[OP_TSZ] = (tsz, 0)

def tld(frame, machine):
    idx = frame.pop_operand()
    tpl = frame.pop_operand()
    frame.push_operand(tpl[idx])
ops[OP_TLD] = (tld, 0)

# Bitwise

def bnd(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    frame.push_operand(b & a)
ops[OP_BND] = (bnd, 0)

def bor(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    frame.push_operand(b | a)
ops[OP_BOR] = (bor, 0)

def bxr(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    frame.push_operand(b ^ a)
ops[OP_BXR] = (bxr, 0)

def bnt(frame, machine):
    val = frame.pop_operand()
    frame.push_operand(~val)
ops[OP_BNT] = (bnt, 0)

def bls(frame, machine, amount):
    val = frame.pop_operand()
    frame.push_operand(val << amount)
ops[OP_BLS] = (bls, 1)

def brs(frame, machine, amount):
    val = frame.pop_operand()
    frame.push_operand(val >> amount)
ops[OP_BRS] = (brs, 1)

# Arithmetics

def add(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    frame.push_operand(b + a)
ops[OP_ADD] = (add, 0)

def sub(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    frame.push_operand(b - a)
ops[OP_SUB] = (sub, 0)

def mul(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    frame.push_operand(b * a)
ops[OP_MUL] = (mul, 0)

def div(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    if isinstance(int, b):
        frame.push_operand(b // a)
    else:
        frame.push_operand(b / a)
ops[OP_DIV] = (div, 0)

def mod(frame, machine):
    a = frame.pop_operand()
    b = frame.pop_operand()
    frame.push_operand(b % a)
ops[OP_MOD] = (mod, 0)

def neg(frame, machine):
    val = frame.pop_operand()
    frame.push_operand(-val)
ops[OP_NEG] = (neg, 0)

def inc(frame, machine, value):
    val = frame.pop_operand()
    frame.push_operand(val + value)
ops[OP_INC] = (inc, 1)

def dec(frame, machine, value):
    val = frame.pop_operand()
    frame.push_operand(val - value)
ops[OP_DEC] = (dec, 1)

# Jumps

def jmp(frame, machine, address):
    frame.set_next_pc(address)
ops[OP_JMP] = (jmp, 1)

def ivk(frame, machine, idx, argc):
    args = [frame.pop_operand() for x in range(argc)]
    args.reverse()
    machine.invoke(idx, args)
ops[OP_IVK] = (ivk, 2)

# Branching

def izr(frame, machine, address):
    val = frame.pop_operand()
    if val == 0:
        frame.set_next_pc(address)
ops[OP_IZR] = (izr, 1)

def inz(frame, machine, address):
    val = frame.pop_operand()
    if val != 0:
        frame.set_next_pc(address)
ops[OP_INZ] = (inz, 1)

def ieq(frame, machine, address):
    a = frame.pop_operand()
    b = frame.pop_operand()
    if b == a:
        frame.set_next_pc(address)
ops[OP_IEQ] = (ieq, 1)

def ine(frame, machine, address):
    a = frame.pop_operand()
    b = frame.pop_operand()
    if b != a:
        frame.set_next_pc(address)
ops[OP_INE] = (ine, 1)

def ilt(frame, machine, address):
    a = frame.pop_operand()
    b = frame.pop_operand()
    if b < a:
        frame.set_next_pc(address)
ops[OP_ILT] = (ilt, 1)

def ile(frame, machine, address):
    a = frame.pop_operand()
    b = frame.pop_operand()
    if b <= a:
        frame.set_next_pc(address)
ops[OP_ILE] = (ile, 1)

def igt(frame, machine, address):
    a = frame.pop_operand()
    b = frame.pop_operand()
    if b > a:
        frame.set_next_pc(address)
ops[OP_IGT] = (igt, 1)

def ige(frame, machine, address):
    a = frame.pop_operand()
    b = frame.pop_operand()
    if b >= a:
        frame.set_next_pc(address)
ops[OP_IGE] = (ige, 1)

def iin(frame, machine, address):
    val = frame.pop_operand()
    if val is None:
        frame.set_next_pc(address)
ops[OP_IIN] = (iin, 1)

def inn(frame, machine, address):
    val = frame.pop_operand()
    if val is not None:
        frame.set_next_pc(address)
ops[OP_INN] = (inn, 1)

# Debug

def _breakpoint(frame, machine, handler, args):
    print(frame)
    input('Press Enter to continue...')
    handler(frame, machine, *args)

def abk(frame, machine, is_active):
    machine.set_interceptor(_breakpoint if is_active else None)
ops[OP_ABK] = (abk, 1)

def brk(frame, machine):
    machine.set_interceptor_once(_breakpoint)
ops[OP_BRK] = (brk, 0)
