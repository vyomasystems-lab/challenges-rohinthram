`timescale 1ns / 1ps

module piso_5bit(
    input [4:0] in,
    input clk, shift,
    output reg out
    );
    
    initial out = 0;

    wire q1,q2,q3,q4;
    wire w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12;
    
    d_ff R0(in[0],clk,q1);
    and a1(w1,shift,q1);
    and a2(w2,~shift,in[1]);
    or o1(w3,w1,w2);
    
    d_ff R1(w3,clk,q2);
    and a3(w4,shift,q2);
    and a4(w5,~shift,in[2]);
    or o2(w6,w4,w5);
    
    d_ff R2(w6,clk,q3);
    and a5(w7,shift,q3);
    and a6(w8,~shift,in[3]);
    or o3(w9,w7,w8);
    
    d_ff R3(w9,clk,q4);
    and a7(w10,shift,q4);
    and a8(w11,~shift,in[4]);
    or o4(w12,w10,w11);
    
    d_ff R4(w12,clk,out);

endmodule