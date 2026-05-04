%% Can we truly say, that the thin film refraktive index is due to the changes made for the now etched sample? Or is it due to changes in the depth of the reference, aswell? 


function plotSignaler(Signals)
    figure 
    hold on
    M = length(Signals(1, :))
    legends = []
    for s = 2:M
        s
        plot(Signals(:, 1), Signals(:, s));
        legends = [legends, "Scan " + string(s - 1)];
    end 
    xlabel('Time [ps]');
    ylabel('E [arb. units]'); 
    legend(legends); 
    title('Scan of reference material')
    hold off
    box on
end

function plotUniformRefaktiveIndex(freq, ns)
    figure
    hold on 
    legends = []; 
    M = length(ns(1, :))
    for s = 1:M
        legends = [legends, 'Scan ' + string(s)];
        plot(freq, ns(:, s) ,'LineWidth',2); 
    end 

    xlabel('Frequency [THz]')
    ylabel('Refractive index')
    title('Refraktive index due to uniform material, True or False?');
    ylim([0, 4])
    xlim([0.8, 1.15]); box on;
    legend(legends);
    hold off 
    box on
end 


%% Setup
M = 6;                                      % Amount of scans
d1 = 523.92                                 % Ref depth [um]
relPath = "Tjekfiler/Test filer/"
PurgeAir = importfileT2(relPath + "Luft_middel500.pulse.csv");
PurgeRef = importfileT2(relPath + 'Ren_sillicium_2_scan' + 1 + '.pulse.csv'); 
for m = 2:M 
    
    path = relPath + 'Ren_sillicium_2_scan' + m + '.pulse.csv'; 
    data = importfileT2(path);
    PurgeRef = [PurgeRef, data(:, 2)];      % Time reference is the same for the rest.
end 



%% Frequency response
N = 40000;
step_size=PurgeRef(3,1)-PurgeRef(2,1); %ps
df = 1/(N*step_size);
freq = (linspace(0,N-1,N).*df)';
ref_fft = conj(fft(PurgeRef(:,2:6),N));
air_fft = conj(fft(PurgeAir(:,2),N));

% Phase response
air_phase = unwrap(angle(air_fft)); 
ref_phase = unwrap(angle(ref_fft));

phi=unwrap(ref_phase-air_phase);
%% Uniform refraktive indices
c=300; %µm/ps
n  = 1+(phi.*c)./(2*pi.*freq.*d1);



plotSignaler(PurgeRef)
plotUniformRefaktiveIndex(freq, n)
