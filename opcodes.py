# GYAFUN VM Op Codes

# General ops
OP_NOP = 0x00 # No-op

# Frame control
OP_RET = 0x01 # Pop the stack and return value to previous frame

# Stack management
OP_LD0 = 0x02 # Push 0 on the stack
OP_LD1 = 0x03 # Push 1 on the stack
OP_LDN = 0x04 # Push null on the stack
OP_LDC = 0x05 # Load constant from pool
OP_LDL = 0x06 # Load local from slots
OP_ST0 = 0x07 # Store 0 in local slot
OP_ST1 = 0x08 # Store 1 in local slot
OP_STN = 0x09 # Store null in local slot
OP_STC = 0x0A # Store constant from pool in local slot
OP_STL = 0x0B # Pop stack and set value in local slot
OP_POP = 0x0C # Pop and discard
OP_DUP = 0x0D # Pop stack and push the value twice

# Arrays
OP_ANW = 0x0E # Pop value and make new array of value length
OP_ASZ = 0x0F # Pop value as array and push size or array
OP_ALD = 0x10 # Pop 2 values for array and index and push value at index
OP_AST = 0x11 # Pop 3 value for array, index and value and set value at index

# Bitwise
OP_BND = 0x12 # &
OP_BOR = 0x13 # |
OP_BXR = 0x14 # ^
OP_BNT = 0x15 # ~
OP_BLS = 0x16 # Left shift
OP_BRS = 0x17 # Right shift

# Arithmetics
OP_ADD = 0x18 # Pop 2 values and push sum
OP_SUB = 0x19 # Pop 2 values and push difference
OP_MUL = 0x1A # Pop 2 values and push product
OP_DIV = 0x1B # Pop 2 values and push quotient
OP_MOD = 0x1C # Pop 2 values and push remainder
OP_NEG = 0x1D # Pop value and push negation
OP_INC = 0x1E # Pop value, increment by n and push result
OP_DEC = 0x1F # Pop value, decrement by n and push result

# Jumps
OP_JMP = 0x20 # Jump to instruction
OP_IVK = 0x21 # Pop n values and invoke subroutine setting up a new stack frame with popped values as locals

# Branching
OP_IZR = 0x22 # Pop value and if equal to 0 jump to address
OP_INZ = 0x23 # Pop value and if not equal to 0 jump to address
OP_IEQ = 0x24 # Pop 2 values and if equal jump to program address
OP_INE = 0x25 # Pop 2 values and if not equal jump to program address
OP_ILT = 0x26 # Pop 2 values and if first is less then second jump to program address
OP_IGT = 0x27 # Pop 2 values and if first is greater then second jump to program address
OP_IIN = 0x28 # Pop 1 value and if null jump to program address
OP_INN = 0x29 # pop 1 value and if not null jump to program address
