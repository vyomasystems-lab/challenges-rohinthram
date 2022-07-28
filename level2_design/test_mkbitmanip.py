# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x000125ae
    mav_putvalue_src2 = 0x00000e47
    mav_putvalue_src3 = 0x00000000

    rs1 = '000'
    rs2 = '0000000'
    rd = '00000'

    opcode = '0110011'
    func7 = ['0100000', '0100000', '0100000', '0010000', '0010000', '0110000', '0110000'
, '0010000'
, '0010000'
, '0010000'
, '0100100'
, '0010100'
, '0110100'
, '0100100'
, '0010100'
, '0110100'
]
    func3 = ['111', '110', '100'
, '001'
, '101'
, '001'
, '101'
, '010'
, '100'
, '110'
, '001'
, '001'
, '001'
, '101'
, '101'
, '101'
]
    ins_str = [func7[i] + rs2 + rs1 + func3[i] + rd + opcode for i in range(len(func7))]
    
    opcode = '0110011'
    func7 = ['0000101'
, '0000101'
, '0000101'
, '0000101'
, '0000101'
, '0000101'
, '0000101'
, '0100100'
, '0000100'
, '0000100'
, '0100100'
, '0000100'
]
    func3 = ['001', '011'
, '010'
, '100'
, '101'
, '110'
, '111'
, '110'
, '110'
, '100'
, '100'
, '111'
]

    ins_str += [func7[i] + rs2 + rs1 + func3[i] + rd + opcode for i in range(len(func7))]
    
    opcode = '0010011'
    
    func7 = ['0110000'
, '0110000'
, '0110000'
, '0110000'
, '0110000'
, '0110000'
, '0110000'
, '0110000'
, '0110000'
, '0110000'
, '0110000'
]

    imm = ['00000'
, '00001'
, '00010'
, '00100'
, '00101'
, '10000'
, '10001'
, '10010'
, '11000'
, '11001'
, '11010'
]

    func3 = ['001'
, '001'
, '001'
, '001'
, '001'
, '001'
, '001'
, '001'
, '001'
, '001'
, '001'
]

    ins_str += [func7[i] + imm[i] + '00000' + func3[i] + rd + opcode for i in range(len(func7))]
    
    opcode = '0110011' 
    
    ins_str += ['0000011'+rs2+rs1+'001'+rd+opcode, '0000011'+rs2+rs1+'101'+rd+opcode,
    '0000010'+rs2+rs1+'001'+rd+opcode, '0000010'+rs2+rs1+'101'+rd+opcode]
    
    opcode = '0010011'

    ins_str += ['000010'+'0'+rs2+rs1+'001'+rd+opcode, '000010'+'0'+rs2+rs1+'101'+rd+opcode, 
    '00101'+'00'+rs2+rs1+'101'+rd+opcode, '01101'+'00'+rs2+rs1+'101'+rd+opcode,
    '00000'+'1'+'0'+rs2+rs1+'101'+rd+opcode]
    
    opcode = '0110011'
    ins_str += ['0100100'+rs2+rs1+'111'+rd+opcode]
    
    
    
    #print(len(ins_str[1]))
    
    insts = [int(i, base=2) for i in ins_str]
    #for mav_putvalue_instr in [0x101010B3]:
    cnt = 0
    total = 0
    for mav_putvalue_instr in insts:
        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
    
        yield Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        #assert dut_output == expected_mav_putvalue, error_message
        if dut_output != expected_mav_putvalue:
        	cnt += 1
        total += 1
       
    assert not cnt, f'Number of Errors : {cnt} for {total}'
        
