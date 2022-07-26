# See LICENSE.vyoma for details

import cocotb
from cocotb.Clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_mux(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await RisingEdge(dut.clk)  
    dut.reset.value = 0
    await RisingEdge(dut.clk)

    #setting different input values
    inp = [1,1,1,1,1,1]
    out = [0,0,0,0,1,0,1,0,1]


    for i in range(len(inp)):
        dut.inp_bit.value = inp[i]
        await RisingEdge(dut.clk)
        
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.seq_seen.value}')
        #assert dut.seq_seen == out[i], f"Incorrect Operation\nExpected : {out[i]} \t Got: {dut.seq_seen.value}"
    
    
