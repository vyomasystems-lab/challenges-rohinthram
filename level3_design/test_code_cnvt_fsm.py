# See LICENSE.vyoma for details

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


def gray_to_bin(num):
    s = bin(num)[2:]
    res = [s[0]]
    for i in range(1, len(s)):
        res.append(str(int(res[i-1])^int(s[i])))
    return ''.join(res)


@cocotb.test()
async def test_code_cnvt_bug1(dut):

    clock = Clock(dut.clk, 2, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    inp = 22
    out = gray_to_bin(inp).zfill(5)[::-1]
    
    dut._log.info(f'Input given : {bin(inp)[2:].zfill(5)} \t Correct Output(LSB to MSB) : {out}')

    dut.shift.value = 0
    await RisingEdge(dut.clk)
    dut.inp.value = inp
    await RisingEdge(dut.clk)
    dut.shift.value = 1
    dut._log.info(f'From DUT: {dut.out.value}')
    await RisingEdge(dut.clk)

    for i in range(6):
        val = str(dut.out.value).replace('x', '0').replace('z', '0')
        dut._log.info(f'From DUT: {dut.out.value}')
        await RisingEdge(dut.clk)
    
    dut._log.info(f'From DUT: {dut.out.value}')
    assert out == str(dut.out.value), f"Incorrect Operation\nExpected : {out} \t Got: {dut.out.value}"
