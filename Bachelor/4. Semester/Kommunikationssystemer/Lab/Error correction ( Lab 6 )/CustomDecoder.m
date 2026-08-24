classdef CustomDecoder 
    properties
    end 
    methods
        function bits = customDecode(obj, Y) 
            threshold = 0.8;
            
            for i = 1: length(Y)
                if Y(i) > threshold 
                    bits(i) = 1;
                else 
                    bits(i) = 0;
                end 
            end 
        end
    end 
end