# See LICENSE.vyoma for details

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
"""
@cocotb.test()
async def test_code_cnvt_bug1(dut):
    clock = Clock(dut.clk, 2, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.shift.value = 0
    await RisingEdge(dut.clk)


    #setting different input values
    inp = [31]*20
    out = ['00000']*20

    for i in range(len(inp)):
        dut.inp.value = inp[i]
        if i == 0:
            dut.out.value = 0
            dut.shift.value=1
        await RisingEdge(dut.clk)
        val = str(dut.out.value).replace('x', '0').replace('z', '0')
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.out.value}')
        	
        #assert val == out[i], f"Incorrect Operation\nExpected : {out[i]} \t Got: {val}"
 """   
"""
@cocotb.test()
async def test_code_cnvt_bug1(dut):
    clock = Clock(dut.clk, 2, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    dut.inp.value = 31
    dut.shift.value = 0
    await RisingEdge(dut.clk)
    dut.shift.value = 1
    await RisingEdge(dut.clk)

    out = ['00000', 'x0000', '0x000', '10x00', '010x0', '10100', '01010', '10101']

    for i in range(4):
        await RisingEdge(dut.clk)

    for i in range(len(out)):
        await RisingEdge(dut.clk)
        val = str(dut.out.value).replace('x', '0').replace('z', '0')
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.out.value}')
        	
        assert val == out[i].replace('x', '0'), f"Incorrect Operation\nExpected : {out[i]} \t Got: {val}"
"""

def gray_to_bin(num):
    s = bin(num)[2:]
    res = [s[0]]
    for i in range(1, len(s)):
        res.append(str(int(res[i-1])^int(s[i])))
    return ''.join(res)
"""
@cocotb.test()
async def test_code_cnvt_bug2(dut):
    clock = Clock(dut.clk, 2, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    # inp = 31
    nErr = 0
    for inp in range(32):
        out = gray_to_bin(inp).zfill(5)[::-1]
        
        dut._log.info(f'Input given : {bin(inp)[2:]} \t Correct Output : {out}')

        dut.shift.value = 0
        await RisingEdge(dut.clk)
        dut.inp.value = inp
        await RisingEdge(dut.clk)
        dut.shift.value = 1
        dut._log.info(f'From DUT: {dut.out.value}')
        await RisingEdge(dut.clk)



    #    for i in range(0):
    #        await RisingEdge(dut.clk)

        for i in range(6):
            val = str(dut.out.value).replace('x', '0').replace('z', '0')
            dut._log.info(f'From DUT: {dut.out.value}')
            await RisingEdge(dut.clk)
        
        dut._log.info(f'From DUT: {dut.out.value}')
        if out != str(dut.out.value):
            nErr += 1
        #assert out == str(dut.out.value), f"Incorrect Operation\nExpected : {out} \t Got: {dut.out.value}"
    
    assert not nErr, f"{nErr} errors out of 32" 
"""  

@cocotb.test()
async def test_code_cnvt_bug1(dut):

    clock = Clock(dut.clk, 2, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    inp = 27
    out = gray_to_bin(inp).zfill(5)[::-1]
    
    dut._log.info(f'Input given : {bin(inp)[2:]} \t Correct Output(LSB to MSB) : {out}')

    dut.shift.value = 0
    await RisingEdge(dut.clk)
    dut.inp.value = inp
    await RisingEdge(dut.clk)
    dut.shift.value = 1
    dut._log.info(f'From DUT: {dut.out.value}')
    await RisingEdge(dut.clk)



#    for i in range(0):
#        await RisingEdge(dut.clk)

    for i in range(6):
        val = str(dut.out.value).replace('x', '0').replace('z', '0')
        dut._log.info(f'From DUT: {dut.out.value}')
        await RisingEdge(dut.clk)
    
    dut._log.info(f'From DUT: {dut.out.value}')
    assert out == str(dut.out.value), f"Incorrect Operation\nExpected : {out} \t Got: {dut.out.value}"
  
       
