`timescale 1ns/1ps
`default_nettype none

// Synthesis
module test;

  /* Make a reset that pulses once. */
  reg clk = 0;
  wire [7:0] value;
  reg reset = 0;
  
  initial begin
    $dumpfile("wave.vcd");
    $dumpvars(clk, reset, value);
    # 17 reset = 1;
    # 11 reset = 0;
    # 29 reset = 1;
    # 11 reset = 0;
    # 100 $finish;
  end
  
  /* Make a regular pulsing clock. */
  always #5 clk = !clk;

  counter c1 (value, clk, reset);
  
  initial
     $monitor("At time %t, value = %h (%0d)",
              $time, value, value);
endmodule // test

`resetall

