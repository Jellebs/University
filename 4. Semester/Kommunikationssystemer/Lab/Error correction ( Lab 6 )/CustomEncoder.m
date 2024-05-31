classdef CustomEncoder
    properties
    end
    methods
        % 1 => r = √(I^2 +Q^2) > 0.8, else r < 0.8
        function [I, Q] = customEncode(obj, bits)
            for bit = 1: length(bits)
                if bits(bit) == 1 
                    % c = √(a^2 + b^2) s
                    len = 0.8 + (1 - 0.8)*abs(rand(1))
                    I(bit) = len*abs(rand(1));
                    % b = √(c^2 - a^2) 
                    Q(bit) = sqrt(len^2 - I(bit)^2);
                else
                    len = 0.8*abs(rand(1))
                    I(bit) = len*abs(rand(1));
                    Q(bit) = sqrt(len^2 - I(bit)^2);
                end 
            end 
        end 
    end
end 

