classdef ChannelEncoder
    properties
    end
    methods
        function repBits = repetitionBits(obj, bits, n) % Repetition code 
            repBits = size(bits * n)
            j = 1; 
            for bit = 1: length(bits)
                for i = 1: n
                    repBits(j) = bits(bit) %  = [repBits, bits(bits)]; 
                    j = j + 1
                end 
            end
        
        end 
    end 
end

