`timescale 1ns / 1ps

module d_ff(
    input d, clk,
    output reg q
    );
    
    
    initial q = 0;
    
    always @ (posedge clk)
        q <= d;
    
endmodule

