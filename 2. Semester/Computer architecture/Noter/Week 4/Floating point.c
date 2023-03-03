
/* 
Floating point bit representation: 
    single precision ( 32 bits ): 
        s = 1 bit 
        exp = 8 bits 
        frac = 23 bits 
    double precision ( 64 bits ): 
        s = 1 bit 
        exp = 11 bits 
        frac = 52 bits.  

Normalized encoding example 
    Value = (-1)^s * M * 2**E 
    E = exp - bias
    bias = 2**(k-1)
    k = number of exponent bits

Example 
float f = 15213.0; 
15213_10 = 11101101101101_2 

M = 1.1101101101101_2 
Frac = 1101101101101

E = 13, mængden af bits vi har shiftet til højre. 
Bias = 2**(8-1) -1, ved single precision.
Exp = 127 + 13


*/