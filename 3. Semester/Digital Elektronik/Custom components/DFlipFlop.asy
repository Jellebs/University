Version 4
SymbolType CELL
LINE Normal -32 -32 32 -32 2
LINE Normal 32 -32 32 32 2
LINE Normal 32 32 -32 32 2
LINE Normal -32 32 -32 -32 2
LINE Normal 32 0 64 0 2
LINE Normal -64 0 -32 0 2
LINE Normal -16 -64 -16 -32 2
LINE Normal 16 -32 16 -64 2
LINE Normal 16 64 16 32 2
LINE Normal -16 64 -16 32 2
TEXT 0 0 VCenter 1 FlipFlop
PIN -16 -64 RIGHT 8
PINATTR PinName CLK
PINATTR SpiceOrder 1
PIN -64 0 BOTTOM 8
PINATTR PinName D
PINATTR SpiceOrder 2
PIN 16 -64 LEFT 8
PINATTR PinName Reset
PINATTR SpiceOrder 3
PIN 64 0 BOTTOM 8
PINATTR PinName QInv
PINATTR SpiceOrder 4
PIN -16 64 RIGHT 8
PINATTR PinName vpo
PINATTR SpiceOrder 5
PIN 16 64 LEFT 8
PINATTR PinName vneg
PINATTR SpiceOrder 6
