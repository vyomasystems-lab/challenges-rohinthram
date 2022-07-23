# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    #cocotb.log.info('##### CTB: Develop your test here ########')
    
    #setting different input values
    inp = [0]*31
    inp[1] = 2
    inp[6] = 2
    inp[17] = 1
    inp[20] = 1
    inp[30] = 3
    

    for i in range(len(inp)):
        exec(f'dut.inp{i}.value = {inp[i]}')

    #for a given input, changing the select line and verifying the correctness
    for i in range(len(inp)):
        dut.sel.value = i
        await Timer(2, units='ns')

        assert dut.out.value == inp[i], "Incorrect Operation"
    
