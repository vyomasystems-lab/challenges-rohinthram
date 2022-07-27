# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    inp = [1,1,0,1,1]
    out = [0,0,0,0,1]
    for i in range(len(inp)):
        dut.inp_bit.value = inp[i]
        await FallingEdge(dut.clk)
        
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.seq_seen.value}')
        assert dut.seq_seen == out[i], f"Incorrect Operation\nExpected : {out[i]} \t Got: {dut.seq_seen.value}"


@cocotb.test()
async def test_seq_bug2(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    inp = [1,0,1,1,1,0,1,1]
    out = [0,0,0,1,0,0,0,1]
    for i in range(len(inp)):
        dut.inp_bit.value = inp[i]
        await FallingEdge(dut.clk)
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.seq_seen.value}')
        assert dut.seq_seen == out[i], f"Incorrect Operation\nExpected : {out[i]} \t Got: {dut.seq_seen.value}"

@cocotb.test()
async def test_seq_bug3(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    inp = [1,0,1,0,1,1]
    out = [0,0,0,0,0,1]
    for i in range(len(inp)):
        dut.inp_bit.value = inp[i]
        await FallingEdge(dut.clk)
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.seq_seen.value}')
        assert dut.seq_seen == out[i], f"Incorrect Operation\nExpected : {out[i]} \t Got: {dut.seq_seen.value}"


@cocotb.test()
async def test_seq_bug3(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    for i in range(256):
        #reset
        dut.reset.value = 1
        await FallingEdge(dut.clk)
        dut.reset.value = 0
        await FallingEdge(dut.clk)
        a=format(i, '08b')
        dut._log.info(f"Sequence : {a} ")

        #a='10111011'
        inp=list(a)
        l=a.find('1011')
        m=a.rfind('1011')
        out = [0]*8
        if l == m :
            if (l != -1) :
                out[l+3]=1
        elif l+3 == m :
            out[l+3]=1
        else:
            out[l+3]=1
            out[m+3]=1

        for j in range(8):

            dut.inp_bit.value = int(inp[j])
            await FallingEdge(dut.clk)
            dut._log.info(f'DUT input = > {dut.inp_bit.value} \n Expected Output => {out[j]} \n Output => {dut.seq_seen.value}')
            assert out[j] == dut.seq_seen.value, f"Incorrect => Expected : {out[j]} Got : {dut.seq_seen.value}"
        