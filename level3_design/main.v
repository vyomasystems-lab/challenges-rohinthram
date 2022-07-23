`timescale 1ns / 1ps

module main(
    input clk, shift,
    input [4:0] in,
    output [4:0] out
    );
    
    wire [1:0] temp;
   
    piso_5bit piso1(in, clk, shift, temp[0]);
    gray_bin_5bit_fsm fsm1(clk, temp[0], temp[1]);
    sipo_5bit sipo1(temp[1], clk, out); 
    
endmodule
