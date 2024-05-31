classdef ChannelDecoder
    properties
    end
    methods
        function bits = channelDecode(obj, repBits, n)
            i = 1; 
            lenZeros = 0; 
            lenOnes = 0;
            bits = []
            
            for j = 1: length(repBits)
                if repBits(j) == 1
                    lenOnes = lenOnes + 1;
                else 
                    lenZeros = lenZeros +1; 
                end 
                i = i + 1; 
                
                % Majority vote
                if i == n + 1;  
                    if lenOnes > lenZeros 
                        bits = [bits, 1];
                    else 
                        bits = [bits, 0];
                    end 
                    lenOnes = 0; 
                    lenZeros = 0; 
                    i = 1; 
                end 
            end 
        end 
    end 
end 