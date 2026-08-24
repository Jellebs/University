clear all
close all

%% Tidsdomæne

luftFilSti = "luft_500middel.pulse.csv"
refFilSti1 = "ren_silicium525_1_scan1.pulse.csv"
refFilSti2 = "ren_silicium525_2_scan1.pulse.csv"

PurgeAir = importfileT2(luftFilSti);
PurgeRef1 = importfileT2(refFilSti1);
PurgeRef2 = importfileT2(refFilSti2);

d3=526; %µm,     thickness of the reference substrate 
d1=538; %um      thickness of the second reference substrate.
d2= 498; %µm,     thickness of the SAMPLE substrate
d = 10e-6 % 5.5e-6; % Thin-film thickness in meters (10 nm example)

figure
hold all
plot(PurgeAir(:,1),PurgeAir(:,2) , 'green','LineWidth',2)
plot(PurgeRef1(:,1),PurgeRef1(:,2) , 'r','LineWidth',2)
plot(PurgeRef2(:,1),PurgeRef2(:,2), 'b','LineWidth',2)

refFilSti1 = "ren_silicium525_1_scan2.pulse.csv"
refFilSti2 = "ren_silicium525_2_scan2.pulse.csv"
PurgeRef1 = importfileT2(refFilSti1);
PurgeRef2 = importfileT2(refFilSti2);
plot(PurgeRef1(:,1),PurgeRef1(:,2) , 'r','LineWidth',2)
plot(PurgeRef2(:,1),PurgeRef2(:,2), 'b','LineWidth',2)

xlabel('Time [ps]')
ylabel('E [arb. units]')
legend('Air','Reference 1', 'Reference 2')



%% Frekvensdomæne
% Compute FFT
N = 40000;
step_size=PurgeRef1(3,1)-PurgeRef1(2,1); %ps
df = 1/(N*step_size);
freq = (linspace(0,N-1,N).*df)';


ref1_fft = conj(fft(PurgeRef1(:,2),N));
ref2_fft = conj(fft(PurgeRef2(:,2),N));
air_fft = conj(fft(PurgeAir(:,2),N));

% Unwrap phase
ref1_phase = unwrap(angle(ref1_fft));
ref2_phase = unwrap(angle(ref2_fft));

c=300; %µm/ps

PhaseConja=unwrap(angle(conj(fft(PurgeAir(:,2),N))));
PhaseConj1=unwrap(angle(conj(fft(PurgeRef1(:,2),N))));
PhaseConj2=unwrap(angle(conj(fft(PurgeRef2(:,2),N))));
PhaseConja1=unwrap(angle(conj(fft(PurgeAir(:,2),N))));
phi=unwrap((PhaseConj1-PhaseConja1));
phi1=unwrap((PhaseConj2-PhaseConja));
n  = 1+(phi.*c)./(2*pi.*freq.*d1);
n1  = 1+(phi1.*c)./(2*pi.*freq.*d3);
figure
hold all
plot(freq,n , 'b','LineWidth',2)
plot(freq,n1 , 'r','LineWidth',2)
xlabel('Frequency [THz]')
ylabel('Refractive index')
box on;
legend('Reference1', 'Reference2');