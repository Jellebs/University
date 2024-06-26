clear all; close all; clc; 

p = 0.25; 
num_bits = 1e6; 
num_of_channels = 3; 

tx_sequence = randi([0, 1], 1, num_bits); 

rx_sequence = tx_sequence;


for i = 1: num_of_channels
    error_positions = rand(1, num_bits) < p;
    
    rx_sequence = xor(rx_sequence, error_positions);

end 

error_count = sum(rx_sequence ~= tx_sequence);
error_probability = error_count / num_bits; 

X = [1 - p p;p 1-p]^num_of_channels

disp(["Crossover probability(p):", num2str(p)]);
disp(["Number of cascaded channels:", num2str(num_of_channels)]);
disp(["Simulated Error probability for 3 cascaded channnels:", num2str(error_probability)]); 
disp(["Calculated Error probability for 3 cascaded channels:", num2str(X(2))]);











