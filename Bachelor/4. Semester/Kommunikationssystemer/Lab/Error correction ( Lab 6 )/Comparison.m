classdef Comparison 
    properties 
    end 
    methods
        % Function for comparing errors from SNR 0... 10 
        function [bErrorsRep, bErrorsHamming] = bitErrorComparison(obj, bits)
            bErrorsRep = []
            bErrorsHamming = []
            channelEncoder = ChannelEncoder()
            channelDecoder = ChannelDecoder()
            customEncoder = CustomEncoder()
            customDecoder = CustomDecoder()
            for snr = 0: 10 % Change in SNR 

                %% Repetitioncode
                % Channel encoder
                n = 7; 
                bitsrep = repetitionBits(channelEncoder, bits, n) % repetition code 
                
                % Modulator 
                [I, Q] = customEncode(customEncoder, bitsrep) 
                
                IQ = sqrt(I.^2 + Q.^2); % r = √(a^2 + b^2) for a complex signal.
                Y = awgn(IQ, snr);
                
                % Demodulator
                bitsDemodulated = customDecode(customDecoder, Y);
                
                % ChannelDemodulator
                bitsRep = channelDecode(ChannelDecoder, bitsDemodulated, n)
    
    
                %% Hamming code
                n = 31; 
                k = 26; 
                
                % Channel encoder / modulator
                encData = encode(bits, n, k, 'hamming/binary');
                
                Y = awgn(encData, snr);
                
                % Channel decoder / demodulator 
                decData = decode(bits, n, k); 
                
                [number, ratio] = biterr(bits, bitsRep) % Number of bits differing and ratio of errors / bits
                bErrorsRep = [bErrorsRep, ratio]

                [number, ratio] = biterr(bits, decData)
                bErrorHamming = [bErrorsHamming, ratio]
            end 
            
        end 

    end 
end
