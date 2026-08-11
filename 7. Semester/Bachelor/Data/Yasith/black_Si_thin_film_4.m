clear all
close all


PurgeAir1 = importfileT2('ref9.pulse.csv');
PurgeRef = importfileT2('reff2.pulse.csv');
PurgeAir = importfileT2('ref9.pulse.csv');
filename = '16_23'; % Define the base filename (without extensions)
PurgeSam = importfileT2([filename '.pulse.csv']); % Use the variable for importing
% PurgeSam1 = importfileT2('black2.pulse.csv');
% PurgeSam2 = importfileT2('black2_1.pulse.csv');

d1=523.92; %µm,     thickness of the reference substrate 
d2= 501.2; % ; %µm,     thickness of the SAMPLE substrate
d =5.5e-6;% 5.5e-6; % Thin-film thickness in meters (10 nm example)
%Ref = importfileT2('ref.pulse.csv');

d2 = 495.8;
d = 6e-6;

figure 
hold on
plot(PurgeRef(:,1),PurgeRef(:,2))
plot(PurgeRef(:,1),PurgeAir(:,2))
plot(PurgeSam(:,1),PurgeSam(:,2))
% plot(PurgeSam(:,1),PurgeSam1(:,2))
% plot(PurgeSam(:,1),PurgeSam2(:,2))
xlabel('Time [ps]')
ylabel('E [arb. units]')
legend('Air','Reference', 'black Si')

hold off
box on
plot(PurgeRef(:,2))

s1=485;
p1=675;
 % p2=1830;
PurgeAir = PurgeAir (s1:p1,:);%-[PurgeRef(s1,1).*ones(s1-p1+1,1),zeros(s1-p1+1,1)];

PurgeAir1 = PurgeAir1 (s1:p1,:);%-[PurgeRef(s1,1).*ones(s1-p1+1,1),zeros(s1-p1+1,1)];

s2=485;
p2=675;
PurgeRef = PurgeRef (s2:p2,:);%-[PurgeRef(s1,1).*ones(s1-p1+1,1),zeros(s1-p1+1,1)];
PurgeSam = PurgeSam (s2:p2,:);%-[PurgeSam(s1,1).*ones(s1-p1+1,1),zeros(s1-p1+1,1)];
% PurgeSam1 = PurgeSam1 (s2:p2,:);%-[PurgeSam(s1,1).*ones(s1-p1+1,1),zeros(s1-p1+1,1)];
% PurgeSam2 = PurgeSam2 (s2:p2,:);%-[PurgeSam(s1,1).*ones(s1-p1+1,1),zeros(s1-p1+1,1)];
%Ref = Ref(p:s,:)-[Ref(p,1).*ones(s-p+1,1),zeros(s-p+1,1)];
 
figure
hold all
plot(PurgeRef(:,1),PurgeAir(:,2) , 'k','LineWidth',2)
plot(PurgeRef(:,1),PurgeRef(:,2) , 'r','LineWidth',2)
plot(PurgeSam(:,1),PurgeSam(:,2), 'b','LineWidth',2)
plot(PurgeSam(:,1),PurgeAir1(:,2), 'g','LineWidth',2)
% plot(PurgeSam(:,1),PurgeSam1(:,2), 'r','LineWidth',2)
% plot(PurgeSam(:,1),PurgeSam2(:,2), 'r','LineWidth',2)
xlabel('Time [ps]')
ylabel('E [arb. units]')
legend('Air','Reference', 'black Si','Air1')
x_limit = [0.05, 2];
% box on
% data
figure 
hold on
plot(PurgeRef(:,2))
plot(PurgeAir(:,2))
plot(PurgeSam(:,2))
plot(PurgeAir1(:,2))
% plot(PurgeSam(:,1),PurgeSam1(:,2))
% plot(PurgeSam(:,1),PurgeSam2(:,2))
xlabel('Time [ps]')
ylabel('E [arb. units]')
legend('Air','Reference', 'black Si')
%%
N = 40000;
step_size=PurgeRef(3,1)-PurgeRef(2,1); %ps
df = 1/(N*step_size);
freq = (linspace(0,N-1,N).*df)';
% 
% figure
% semilogy(freq,abs(conj(fft(PurgeAir(:,2),N))) , 'k','LineWidth',2)
% hold on
% semilogy(freq,abs(conj(fft(PurgeRef(:,2),N))) , 'r','LineWidth',2)
% semilogy(freq,abs(conj(fft(PurgeSam(:,2),N))) , 'b','LineWidth',2)
% semilogy(freq,abs(conj(fft(PurgeAir1(:,2),N))) , 'b','LineWidth',2)
% % semilogy(freq,abs(conj(fft(PurgeSam1(:,2),N))))
% % semilogy(freq,abs(conj(fft(PurgeSam2(:,2),N))))
% ylabel('|E|')
% xlabel('Frequency [THz]')
% xlim([0,6])
% box on
% legend('Air','Reference', 'black Si')
%%
% Compute FFT
data_fft = conj(fft(PurgeSam(:,2),N));
ref_fft = conj(fft(PurgeRef(:,2),N));
air_fft = conj(fft(PurgeAir(:,2),N));
air_fft1 = conj(fft(PurgeAir1(:,2),N));
% Plot spectrum
% figure;
% hold on;
% semilogy(freq, abs(data_fft) , 'r','LineWidth',2)
% semilogy(freq, abs(ref_fft) , 'b','LineWidth',2)
% semilogy(freq, abs(air_fft) , 'k','LineWidth',2)
% title('Spectrum of Data');
% xlabel('Frequency [THz]');
% ylabel('|E|');
% xlim(x_limit); box on;
% legend('Sample', 'Reference');
% hold off;

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
%%

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
plot(freq, sqrt(eps_CM) , 'r','LineWidth',2)
% plot(freq, real(n_f_eq_5_6) , 'g','LineWidth',2)
hold off
title('Refractive Index ');
xlabel('Frequency [THz]');
ylabel('Refractive Index');
xlim(x_limit); box on;
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
