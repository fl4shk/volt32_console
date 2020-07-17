#!/usr/bin/env python3

from misc_util import *

from enum import Enum, auto

class Op(Enum):
	#--------
	# 0 .. 3

	# add rA, rB, rC
	Add = 0

	# sub rA, rB, rC
	Sub = auto()

	# addsi rA, rB, simm16
	Addsi = auto()

	# sltu rA, rB, rC
	Sltu = auto()
	#--------

	#--------
	# 4 .. 7

	# slts rA, rB, rC
	Slts = auto()

	# mulu rA, rB, rC, rD
	# multiply, unsigned full product, high in `rA`, low in `rB`
	Mulu = auto()

	# divu rA, rB, rC, rD
	# divmod unsigned, quotient in `rA`, remainder in `rB`
	Divu = auto()

	# and rA, rB, rC
	And = auto()
	#--------

	#--------
	# 8 .. 11

	# or rA, rB, rC
	Or = auto()

	# xor rA, rB, rC
	Xor = auto()

	# lsl rA, rB, rC
	Lsl = auto()

	# lsr rA, rB, rC
	Lsr = auto()
	#--------

	#--------
	# 12 .. 15
	# asr rA, rB, rC
	Asr = auto()

	# pre simm24
	Pre = auto()

	# addsi rA, pc, simm20
	AddsiPc = auto()

	# jl rA, simm20
	# Jump and link, jumping to location `rA + to_s32(simm20)`
	Jl = auto()
	#--------

	#--------
	# 16 .. 19

	# jmp rA, simm20
	# Jump to location `rA + to_s32(simm20)`
	Jmp = auto()

	# bz rA, simm20
	Bz = auto()

	# bnz rA, simm20
	Bnz = auto()

	# ld rA, [rB, simm16]
	Ld = auto()
	#--------

	#--------
	# 20 .. 23

	# st rA, [rB, simm16]
	St = auto()

	# ldh rA, [rB, simm16]
	Ldh = auto()

	# ldsh rA, [rB, simm16]
	Ldsh = auto()

	# sth rA, [rB, simm16]
	Sth = auto()
	#--------

	#--------
	# 24 .. 27

	# ldb rA, [rB, simm16]
	Ldb = auto()

	# ldsb rA, [rB, simm16]
	Ldsb = auto()

	# stb rA, [rB, simm16]
	Stb = auto()

	# zeh rA, rB
	Zeh = auto()
	#--------

	#--------
	# 28 .. 31

	# zeb rA, rB
	Zeb = auto()

	# seh rA, rB
	Seh = auto()

	# seb rA, rB
	Seb = auto()

	# ei
	Ei = auto()
	#--------

	#--------
	# 32 .. 35

	# di
	Di = auto()

	# reti
	Reti = auto()
	#--------

# Registers
#--------
Zero = 0
A0 = 1
A1 = 2
A2 = 3
#--------

#--------
A3 = 4
R0 = 5
R1 = 6
U0 = 7
#--------

#--------
U1 = 8
U2 = 9
U3 = 10
U4 = 11
#--------

#--------
Ira = 12
Lr = 13
Fp = 14
Sp = 15
#--------

#--------
NumRegs = 16
#--------
