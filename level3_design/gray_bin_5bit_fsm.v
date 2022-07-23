`timescale 1ns / 1ps

module gray_bin_5bit_fsm(
    input clk, in,
    output reg out
    );
    
    parameter s0=0, s1=1, s2=2, s3=3, s4=4, s5=5, s6=6, s7=7, s8=8;
    
    reg [4:0] state;
    
    always @ (posedge clk) begin
    
        case(state)
            s0: state <= in ? s2 : s1;
            s1: state <= in ? s4 : s3;
            s2: state <= in ? s3 : s4;
            s3: state <= in ? s6 : s5;
            s4: state <= in ? s5 : s6;
            s5: state <= in ? s8 : s7;
            s6: state <= in ? s7 : s8;
            s7: state <= s0;
            s8: state <= s0;
            default: state <= s0;
        endcase
        
        case(state)
            s0: out <= in ? 1 : 0;
            s1: out <= in ? 1 : 0;
            s2: out <= in ? 0 : 1;
            s3: out <= in ? 1 : 0;
            s4: out <= in ? 0 : 1;
            s5: out <= in ? 1 : 0;
            s6: out <= in ? 0 : 1;
            s7: out <= in ? 1 : 0;
            s8: out <= in ? 0 : 1;
            default: out <= 0;         
        endcase  
       // $monitor(state, out); 
    end
    
endmodule
