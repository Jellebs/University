clear
customDecoder = CustomDecoder();
customEncoder = CustomEncoder();
channelEncoder = ChannelEncoder();
channelDecoder = ChannelDecoder();

% Task 1-5: 

% Source 
bits = [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]; 

% Channel encoder
n = 7; 
bits = repetitionBits(channelEncoder, bits, n) % repetition code 

% Modulator 
[I, Q] = customEncode(customEncoder, bits) 

% Adding white gaussian noise
% I am using IQ modulation just with the coefficient. 
% Normally the signal here would be Icos(2πf) + jQsin(2πf) 
% I just take the length of the two. 
IQ = sqrt(I.^2 + Q.^2) % r = √(a^2 + b^2) for a complex signal.
snr = 3
Y = awgn(IQ, snr)

% Demodulator
bits = customDecode(customDecoder, Y)

% ChannelDemodulator
bitsRep = channelDecode(ChannelDecoder, bits, n)




% Task 8 - 10: 
bits = [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]; 

% Bit error comparison. 
% In our comparison code we have implemented hamming codes with n = 15,
% k = 11
compare = Comparison()

[bErrorRep, bErrorHamming] = bitErrorComparison(compare, bits)
SNR = 0: 10
figure; 
plot(SNR, bErrorRep,'DisplayName','Bit error repetitioncode')
hold on 
plot(SNR, bErrorHamming, 'DisplayName', 'Bit error Hamming code')
hold off
legend

















