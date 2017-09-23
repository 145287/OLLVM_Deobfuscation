# !/usr/bin/python
# coding=utf-8

# Imports from Miasm framework

from miasm2.core.bin_stream                 import bin_stream_str

from miasm2.arch.x86.disasm                 import dis_x86_32

from miasm2.arch.x86.ira                    import ir_a_x86_32

from miasm2.arch.x86.regs                   import all_regs_ids, all_regs_ids_init

from miasm2.ir.symbexec                     import symbexec

from miasm2.expression.simplifications      import expr_simp

from miasm2.expression.expression 			import ExprInt, ExprCond ,ExprInt32, ExprId

from miasm2.expression.modint 				import int32

import miasm2.expression.expression as m2_expr

offset = 0x59b

filename = "/home/hack/Android/OLLVM/OLLVM_TEST/flat_test/target_flat"

bin_file = open(filename, "rb").read() 

bin_stream = bin_stream_str(bin_file)

mdis = dis_x86_32(bin_stream)     

disasm = mdis.dis_multibloc(offset) 

ir = ir_a_x86_32(mdis.symbol_pool)

for bbl in disasm: 
	ir.add_bloc(bbl) 


symbols_init =  {}

for i, r in enumerate(all_regs_ids):

    symbols_init[r] = all_regs_ids_init[i]

symb = symbexec(ir, symbols_init)

#======================================单个地址计算
block = ir.get_bloc(offset)#

nxt_addr = symb.emulbloc(block) 

simp_addr = expr_simp(nxt_addr)  
 
if isinstance(simp_addr,ExprInt):
	print "Jump on next basic block: %s" % simp_addr 
 
elif isinstance(simp_addr, ExprCond):  # The simp_addr variable is a condition expression
	branch1 = simp_addr.src1
	branch2 = simp_addr.src2
	print("Condition: %s or %s" % (branch1,branch2))






		


	