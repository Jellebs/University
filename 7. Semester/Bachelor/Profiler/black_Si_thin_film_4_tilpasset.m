clear all
close all



luftFilSti = "luft_500middel.pulse.csv"
refFilSti = "ren_silicium525_2_scan1.pulse.csv"

filename = '16_23';
samFilSti = "proeve" + filename + "_scan5.pulse.csv"
PurgeAir1 = importfileT2(luftFilSti); 
PurgeRef = importfileT2(refFilSti); 
PurgeAir = importfileT2(luftFilSti); 
PurgeSam = importfileT2(samFilSti); 

d1=523.92; %µm,     thickness of the reference substrate 
d2= 495.8; %µm,     thickness of the SAMPLE substrate
d = 6e-6; % Thin-film thickness in meters (10 nm example)



%% Data
figure 
hold on
plot(PurgeRef(:,1),PurgeRef(:,2))
plot(PurgeRef(:,1),PurgeAir(:,2))
plot(PurgeSam(:,1),PurgeSam(:,2))
xlabel('Time [ps]')
ylabel('E [arb. units]')
legend('Air','Reference', 'black Si')
hold off
box on

plot(PurgeRef(:,2))
%% Vindue
s1=117;
p1=307;

PurgeAir = PurgeAir (s1:p1,:);
PurgeAir1 = PurgeAir1 (s1:p1,:);

s2=117;
p2=307;
PurgeRef = PurgeRef (s2:p2,:);
PurgeSam = PurgeSam (s2:p2,:);
 
figure
hold all
plot(PurgeRef(:,1),PurgeAir(:,2) , 'k','LineWidth',2)
plot(PurgeRef(:,1),PurgeRef(:,2) , 'r','LineWidth',2)
plot(PurgeSam(:,1),PurgeSam(:,2), 'b','LineWidth',2)
plot(PurgeSam(:,1),PurgeAir1(:,2), 'g','LineWidth',2)
xlabel('Time [ps]')
ylabel('E [arb. units]')
legend('Air','Reference', 'black Si','Air1')
x_limit = [0.05, 2];
% box on
% data
figure 
hold on
% Er allerede blevet plottet for, bare uden tidsaksen, men i samples 
% plot(PurgeRef(:,2))
% plot(PurgeAir(:,2))
% plot(PurgeSam(:,2))
% plot(PurgeAir1(:,2))
% xlabel('Time [ps]')
% ylabel('E [arb. units]')
% legend('Air','Reference', 'black Si')
%% Frekvens spektrum
N = 40000;
step_size=PurgeRef(3,1)-PurgeRef(2,1); %ps
df = 1/(N*step_size);
freq = (linspace(0,N-1,N).*df)';

% Compute FFT
data_fft = conj(fft(PurgeSam(:,2),N));
ref_fft = conj(fft(PurgeRef(:,2),N));
air_fft = conj(fft(PurgeAir(:,2),N));
air_fft1 = conj(fft(PurgeAir1(:,2),N));

% Unwrap phase
data_phase = unwrap(angle(data_fft));
ref_phase = unwrap(angle(ref_fft));
% air_phase = unwrap(angle(air_fft));

c=300; %µm/ps

PhaseConja=unwrap(angle(conj(fft(PurgeAir(:,2),N))));
PhaseConj1=unwrap(angle(conj(fft(PurgeRef(:,2),N))));
PhaseConj2=unwrap(angle(conj(fft(PurgeSam(:,2),N))));
PhaseConja1=unwrap(angle(conj(fft(PurgeAir1(:,2),N))));
phi=unwrap((PhaseConj1-PhaseConja1));
phi1=unwrap((PhaseConj2-PhaseConja));
n  = 1+(phi.*c)./(2*pi.*freq.*d1);
n1  = 1+(phi1.*c)./(2*pi.*freq.*d2);
figure
hold all
plot(freq,n1 , 'r','LineWidth',2)
plot(freq,n , 'b','LineWidth',2)
xlabel('Frequency [THz]')
ylabel('Refractive index')
xlim(x_limit); box on;
legend('Sample', 'Reference');

%% Plot phase
figure;
hold on;
plot(freq, phi , 'r','LineWidth',2)
plot(freq, phi1 , 'b','LineWidth',2)
title('Unwrapped Phase of Data');
xlabel('Frequency [THz]');
ylabel('Phase [radians]');
xlim(x_limit); box on;
legend('Sample', 'Reference');
hold off;
%% thin film validity
f=freq(150:end)* 1e12;
c1 = 2.99e8;
lambda = c1 ./ (f); % THz wavelengths
% figure;
% plot(f, lambda / (d), 'LineWidth', 2);
% title('Thin Film Approximation Validity');
% xlabel('Frequency [THz]');
% ylabel('λ/d');
%% Compute complex transmission function, T
% T_data = data_fft ./ ref_fft;
% 
% % Plot amplitude of T
% figure;
% hold on;
% plot(freq, abs(T_data));
% title('Amplitude of T for Data' , 'r','LineWidth',2)
% xlabel('Frequency [THz]');
% ylabel('Amplitude');
% xlim(x_limit); box on;
% ylim([0, 2]);
% hold off;
% 
% % Plot phase of T
% T_data_phase = data_phase - ref_phase;
% figure;
% hold on;
% plot(freq, T_data_phase , 'r','LineWidth',2)
% title('Phase of T for Data');
% xlabel('Frequency [THz]');
% ylabel('Phase');
% xlim(x_limit); box on;
% hold off;

freq = freq * 1e12; % Convert from THz to Hz
omega = 2 * pi * freq; % Angular frequency
freq = freq / 1e12;
%% Thin film refractive index 

% Constants
% d2=529;
c = 2.99e8; % Speed of light in m/s

p_sam = d2*1e-6; % Sample substrate thickness in meters (530 µm example)
p_ref = d1*1e-6; % Reference substrate thickness in meters (525 µm example)

% Compute complex transmission function T
T_data = data_fft ./ ref_fft;

% 
T_factor = (T_data .* (1 + n - n .* 1i .* omega .* d ./ c)) - (n - 1);
T_denominator = T_data .* (1i .* omega .* d ./ c);
n_f_eq_5_3 = sqrt(T_factor ./ T_denominator);

% 
% delta=1e-6;
delta_2 = omega .* n .* (p_sam - p_ref) ./ c; % Assuming p_sam = p2 and p_ref = p1
T_factor_5_6 = (T_data .* (1 + n - n .* 1i .* omega .* d ./ c)) - (n + 1) .* exp(1i .* delta_2);
T_denominator_5_6 = T_data .* (1i .* omega .* d ./ c);
n_f_eq_5_6 = sqrt(T_factor_5_6 ./ T_denominator_5_6);

x_limit = [0.8, 1.15];

eps_Si = (n).^2;
eps_CM = (real(n_f_eq_5_6)).^2;
figure;
hold on
plot(freq, n , 'k','LineWidth',2)
plot(freq, n1 , 'b','LineWidth',2)
% plot(freq, sqrt(eps_CM) , 'r','LineWidth',2)

plot(freq, real(n_f_eq_5_6) , 'r','LineWidth',2)
hold off
title('Refractive Index ');
xlabel('Frequency [THz]');
ylabel('Refractive Index');
xlim(x_limit); box on;
ylim([1, 3.5])
legend('Reference','Whole', 'Srface Layer')



% Compute the parameter zeta
zeta = ((eps_CM - 1) .* 13.68) ./ (10.68.* (2 + eps_CM));
figure;
hold on
plot(freq, zeta , 'k','LineWidth',4)

hold off
title('Vol Fraction');
xlabel('Frequency [THz]');
ylabel('Vol Fraction');
xlim(x_limit); box on;
% legend('Reference')
 save(['new1' filename '.mat'], 'freq', 'n', 'n1', 'n_f_eq_5_6', 'zeta')
