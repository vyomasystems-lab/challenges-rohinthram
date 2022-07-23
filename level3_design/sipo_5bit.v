`timescale 1ns / 1ps

module sipo_5bit(
    input in, clk,
    output reg [4:0] out
    );
    
    initial out = 0;

    d_ff u1(in,clk,out[4]);
    d_ff u2(out[4],clk,out[3]);
    d_ff u3(out[3],clk,out[2]);
    d_ff u4(out[2],clk,out[1]);
    d_ff u5(out[1],clk,out[0]);
    
endmodule
