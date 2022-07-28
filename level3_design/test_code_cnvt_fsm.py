# See LICENSE.vyoma for details

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_code_cnvt_bug1(dut):
    clock = Clock(dut.clk, 2, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.shift.value = 0
    await RisingEdge(dut.clk)


    #setting different input values
    inp = [31]*12
    out = ['00000','00000','00000','00000','00000','10000','01000', '10100', '01010', '10101', '01010', '10101', '01010']*2


    for i in range(len(inp)):
        dut.inp.value = inp[i]
        if i == 0:
            dut.shift.value=1
        await RisingEdge(dut.clk)
        val = str(dut.out.value).replace('x', '0').replace('z', '0')
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.out.value}')
        	
        #assert val == out[i], f"Incorrect Operation\nExpected : {out[i]} \t Got: {val}"
    
    
