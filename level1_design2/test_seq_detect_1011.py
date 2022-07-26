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
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    inp = [1,0,1,0,1,1,1,0,1,1,0]
    out = [0,0,0,0,0,1,0,0,0,1,0]
    for i in range(len(inp)):
        dut.inp_bit.value = inp[i]
        await FallingEdge(dut.clk)
        
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.seq_seen.value}')
        #assert dut.seq_seen == out[i], f"Incorrect Operation\nExpected : {out[i]} \t Got: {dut.seq_seen.value}"


@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    inp = [1,0,1,1]
    out = [0,0,0,1]
    for i in range(len(inp)):
        dut.inp_bit.value = inp[i]
        await FallingEdge(dut.clk)
        dut._log.info(f'Correct : {out[i]} \t From DUT: {dut.seq_seen.value}')
        #assert dut.seq_seen == out[i], f"Incorrect Operation\nExpected : {out[i]} \t Got: {dut.seq_seen.value}"