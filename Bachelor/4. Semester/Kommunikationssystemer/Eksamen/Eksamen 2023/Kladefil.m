f1 = 800;
f2 = 1800;

% Define the parameters
fs = 2000; % Sampling frequency
t = 0:1/fs:0.01; % Time vector for 10 ms
m = 10*sin(2*pi*f1*t) + 2*cos(2*pi*f2*t); % Message signal

% Plot the message signal
figure;
plot(t, m); 
title('Message Signal');
xlabel('Time (s)');
ylabel('Amplitude');

% Quantize the signal
L = 32; % Number of levels
R = log2(L); % Number of bits
A_max = max(abs(m)); % Maximum amplitude of the signal

% Step size for quantization
delta = 2 * A_max / L;
quantized_sequence = round(m / delta) 
quantized_signal = quantized_sequence * delta;
plot(t, m); 
hold on
stairs(t, quantized_signal);
hold off
legend("Sampled function", "Quantized function");


fc = fs
tprbit = 32;
n = R * tprbit * length(quantized_sequence); % 5 bits * 4 t pr bit * 21 array med bits.
t = linspace(0, 0.01, n+5) 

bits = int2bit(int8(quantized_sequence), R); 
modulatedSignal = zeros(1, n)
k = 1
length(quantized_sequence)
for i = 1: length(quantized_sequence)
    a = tprbit; 
    for j = 1: R
        bit = bits(j, i); 
        if bit == 0 % 0 = -1,  1 = 1; 
            modulatedSignal(k:k+a) = cos(pi + 2*pi*fc*t(k:k+a));
        else 
            modulatedSignal(k:k+a) = 1*cos(2*pi*fc*t(k:k+a));
        end
        k = k + a; 
    end 
end 

% plot(t(1:n+1), modulatedSignal)


powerInput = ((10+2)^2)/2;
powerNoiseQ2 = ((0.75)^2)/12;

SNR = powerInput/powerNoiseQ2;
SNRdB = 20 * log10(SNR);

modulatedSignalwNoise = awgn(modulatedSignal, SNRdB);
%plot(t(1:n+1), modulatedSignal) 
% hold on 
plot(t(1:n+1), modulatedSignalwNoise)
hold off





% bpsk_symbols = 1 - 2 * bits; % Map 0 -> +1 and 1 -> -1
% 
% % Define carrier frequency and create carrier signal
% carrier_freq = 2000; % Carrier frequency (Hz)
% carrier = cos(2 * pi * carrier_freq * t);
% 
% % Modulate the carrier with BPSK symbols
% bpsk_signal = [];
% for i = 1:size(bpsk_symbols, 1)
%     for j = 1:R
%         if bpsk_symbols(i, j) == 1
%             bpsk_signal = [bpsk_signal, carrier(j)];
%         else
%             bpsk_signal = [bpsk_signal, -carrier(j)];
%         end
%     end
% end
% 
% 
% 
% % Plot the original and BPSK modulated signals
% figure;
% subplot(2,1,1);
% plot(t, m);
% title('Original Message Signal');
% xlabel('Time (s)');
% ylabel('Amplitude');
% 
% subplot(2,1,2);
% plot(bpsk_signal);
% title('BPSK Modulated Signal');
% xlabel('Sample Index');
% ylabel('Amplitude');
