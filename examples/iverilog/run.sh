#!/bin/sh

iverilog -o counter.vvp -c file_list.txt
vvp counter.vvp -fst
