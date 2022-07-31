`timescale 1ns / 1ps

module main(
    input clk, shift,
    input [4:0] inp,
    output [4:0] out
    );
    
    wire [1:0] temp;
   
    piso_5bit piso1(inp, clk, shift, temp[0]);
    gray_bin_5bit_fsm fsm1(clk, temp[0], temp[1]);
    sipo_5bit sipo1(temp[1], clk, out); 
    
endmodule

module gray_bin_5bit_fsm(
    input clk, in,
    output reg out
    );
    
    parameter s0=0, s1=1, s2=2, s3=3, s4=4, s5=5, s6=6, s7=7, s8=8;
    
    reg [4:0] state;
    
    initial begin
        state = s0;
        out = 0;
    end

    
    always @ (posedge clk) begin
    
        case(state)
            s0: state <= in ? s2 : s1;
            s1: state <= in ? s4 : s3;
            s2: state <= in ? s3 : s4;
            s3: state <= in ? s6 : s5;
            s4: state <= in ? s5 : s6;
            s5: state <= in ? s7 : s8; // s8 : s7
            s6: state <= in ? s7 : s8;
            s7: state <= s0;
            s8: state <= s0;
            default: state <= s0;
        endcase
        
        case(state)
            s0: out <= in ? 1 : 0;
            s1: out <= in ? 1 : 1; // 1 : 0
            s2: out <= in ? 0 : 1;
            s3: out <= in ? 1 : 0;
            s4: out <= in ? 0 : 1;
            s5: out <= in ? 0 : 0; // 1 : 0
            s6: out <= in ? 0 : 1;
            s7: out <= in ? 1 : 0;
            s8: out <= in ? 0 : 1;
            default: out <= 0;         
        endcase  
        // $display("Input got : %d \t State : %d \t Output : %d", in, state, out); 
    end
    
endmodule

module piso_5bit(
    input [4:0] in,
    input clk, shift,
    output reg out
    );

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

module sipo_5bit(
    input in, clk,
    output reg [4:0] out
    );

    d_ff u1(in,clk,out[4]);
    d_ff u2(out[4],clk,out[3]);
    d_ff u3(out[3],clk,out[2]);
    d_ff u4(out[2],clk,out[1]);
    d_ff u5(out[1],clk,out[0]);
    
endmodule

module d_ff(
    input d, clk,
    output reg q
    );
    
    always @ (posedge clk)
        q <= d;
    
endmodule

