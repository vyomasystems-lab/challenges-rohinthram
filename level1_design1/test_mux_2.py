# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux_1(dut):
    """Test for mux2"""
    #cocotb.log.info('##### CTB: Develop your test here ########')
    
    #setting different input values
    inp = [random.randint(0, 3) for i in range(31)]
    

    for i in range(len(inp)):
        exec(f'dut.inp{i}.value = {inp[i]}')

    #for a given input, changing the select line and verifying the correctness
    for i in range(len(inp)):
        
        dut.sel.value = i
        await Timer(10, units='ns')
        print(i, eval(f'dut.inp{i}.value'), dut.out.value)
        
        assert int(dut.out.value) == inp[i], "Incorrect Operation"
    
@cocotb.test()
async def test_mux_2(dut):
    dut.inp30.value = 2
    dut.sel.value = 30
    await Timer(10, units='ns')
    print(f'{dut.inp30.value}', dut.out.value)
        
    assert int(dut.out.value) == int(dut.inp30.value), "Incorrect Operation"
    
