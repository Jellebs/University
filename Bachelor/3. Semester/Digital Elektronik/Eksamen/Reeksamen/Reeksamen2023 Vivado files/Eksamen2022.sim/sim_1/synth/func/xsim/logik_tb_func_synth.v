// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// Copyright 2022-2023 Advanced Micro Devices, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2023.2 (lin64) Build 4029153 Fri Oct 13 20:13:54 MDT 2023
// Date        : Wed May 29 12:37:32 2024
// Host        : 4f9052e670bb running 64-bit Ubuntu 22.04.3 LTS
// Command     : write_verilog -mode funcsim -nolib -force -file
//               /home/user/Projects/Eksamen/Eksamen2022/Eksamen2022.sim/sim_1/synth/func/xsim/logik_tb_func_synth.v
// Design      : logik
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7z010clg400-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* NotValidForBitStream *)
module logik
   (i,
    a,
    en);
  input [2:0]i;
  output [1:0]a;
  input en;

  wire [1:0]a;
  wire [1:0]a_OBUF;
  wire \a_TRI[0] ;
  wire en;
  wire en_IBUF;
  wire [2:0]i;
  wire [1:0]i_IBUF;

  OBUFT \a_OBUFT[0]_inst 
       (.I(a_OBUF[0]),
        .O(a[0]),
        .T(\a_TRI[0] ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT2 #(
    .INIT(4'h2)) 
    \a_OBUFT[0]_inst_i_1 
       (.I0(i_IBUF[1]),
        .I1(i_IBUF[0]),
        .O(a_OBUF[0]));
  OBUFT \a_OBUFT[1]_inst 
       (.I(a_OBUF[1]),
        .O(a[1]),
        .T(\a_TRI[0] ));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT2 #(
    .INIT(4'h1)) 
    \a_OBUFT[1]_inst_i_1 
       (.I0(i_IBUF[1]),
        .I1(i_IBUF[0]),
        .O(a_OBUF[1]));
  LUT1 #(
    .INIT(2'h1)) 
    \a_OBUFT[1]_inst_i_2 
       (.I0(en_IBUF),
        .O(\a_TRI[0] ));
  IBUF en_IBUF_inst
       (.I(en),
        .O(en_IBUF));
  IBUF \i_IBUF[0]_inst 
       (.I(i[0]),
        .O(i_IBUF[0]));
  IBUF \i_IBUF[1]_inst 
       (.I(i[1]),
        .O(i_IBUF[1]));
endmodule
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;
    parameter GRES_WIDTH = 10000;
    parameter GRES_START = 10000;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
    wire GRESTORE;
    tri1 p_up_tmp;
    tri (weak1, strong0) PLL_LOCKG = p_up_tmp;

    wire PROGB_GLBL;
    wire CCLKO_GLBL;
    wire FCSBO_GLBL;
    wire [3:0] DO_GLBL;
    wire [3:0] DI_GLBL;
   
    reg GSR_int;
    reg GTS_int;
    reg PRLD_int;
    reg GRESTORE_int;

//--------   JTAG Globals --------------
    wire JTAG_TDO_GLBL;
    wire JTAG_TCK_GLBL;
    wire JTAG_TDI_GLBL;
    wire JTAG_TMS_GLBL;
    wire JTAG_TRST_GLBL;

    reg JTAG_CAPTURE_GLBL;
    reg JTAG_RESET_GLBL;
    reg JTAG_SHIFT_GLBL;
    reg JTAG_UPDATE_GLBL;
    reg JTAG_RUNTEST_GLBL;

    reg JTAG_SEL1_GLBL = 0;
    reg JTAG_SEL2_GLBL = 0 ;
    reg JTAG_SEL3_GLBL = 0;
    reg JTAG_SEL4_GLBL = 0;

    reg JTAG_USER_TDO1_GLBL = 1'bz;
    reg JTAG_USER_TDO2_GLBL = 1'bz;
    reg JTAG_USER_TDO3_GLBL = 1'bz;
    reg JTAG_USER_TDO4_GLBL = 1'bz;

    assign (strong1, weak0) GSR = GSR_int;
    assign (strong1, weak0) GTS = GTS_int;
    assign (weak1, weak0) PRLD = PRLD_int;
    assign (strong1, weak0) GRESTORE = GRESTORE_int;

    initial begin
	GSR_int = 1'b1;
	PRLD_int = 1'b1;
	#(ROC_WIDTH)
	GSR_int = 1'b0;
	PRLD_int = 1'b0;
    end

    initial begin
	GTS_int = 1'b1;
	#(TOC_WIDTH)
	GTS_int = 1'b0;
    end

    initial begin 
	GRESTORE_int = 1'b0;
	#(GRES_START);
	GRESTORE_int = 1'b1;
	#(GRES_WIDTH);
	GRESTORE_int = 1'b0;
    end

endmodule
`endif
