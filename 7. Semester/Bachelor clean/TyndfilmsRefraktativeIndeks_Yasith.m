clear all
close all

function TyndfilmsRefrakativIndeks(sample) 
    % Function that for every section will have a plot if wanted.
    % Comment it if unwanted

    %% Hardcoded type parameters:
    PARAMETERS = containers.Map;
    %   Type                d_ref[µm]  d_sam[µm]   d_thinfilm
    PARAMETERS('16_21') = {   523.92,     518.9,     1.1e-6}; 
    PARAMETERS('16_22') = {   523.92,     519.6,       2e-6};
    PARAMETERS('16_23') = {   523.92,     495.8,       6e-6}; 
    PARAMETERS('16_24') = {   523.92,     510.4,       9e-6};
    PARAMETERS('16_25') = {   523.92,     496.8,       7e-6}; 
    PARAMETERS('16_26') = {   523.92,     501.2,     5.5e-6}; 
   
    
    %% Data setup
    data_dir = "Data/Yasith/"
    % PurgeAir1 = importfileT2(data_dir + 'ref9.pulse.csv');
    PurgeRef = importfileT2(data_dir + 'reff2.pulse.csv');
    PurgeAir = importfileT2(data_dir + 'ref9.pulse.csv');
    filename = sample; 
    PurgeSam = importfileT2(data_dir + filename + '.pulse.csv'); 
    
    % Unload parameters
    type = PARAMETERS(sample)
    
    d1   =    type{1}; %    [µm] thickness of the reference substrate 
    d2   =    type{2}; %    [µm] thickness of the SAMPLE substrate
    d    =    type{3}; %    Thin-film thickness in meters (10 nm example)

    function plotSignaler()
        figure 
        hold on
        plot(PurgeRef(:,1),PurgeRef(:,2))
        plot(PurgeRef(:,1),PurgeAir(:,2))
        plot(PurgeSam(:,1),PurgeSam(:,2))
        xlabel('Time [ps]')
        ylabel('E [arb. units]')
        legend('Air','Reference', 'black Si')
        title('Signals ( ' + sample + " )", 'Interpreter','none')   % Keeps the text as is, without formatting 
        hold off
        box on
    end 

    % plotSignaler()
    
   
    %%  Vindue 
    s1=485;
    p1=675;
    PurgeAir = PurgeAir (s1:p1,:);
    
    s2=485;
    p2=675;
    PurgeRef = PurgeRef (s2:p2,:);
    PurgeSam = PurgeSam (s2:p2,:);
    
    function plotWindowedSignal()
        figure 
        hold on
        plot(PurgeRef(:,1),PurgeAir(:,2) , 'k','LineWidth',2)
        plot(PurgeRef(:,1),PurgeRef(:,2) , 'r','LineWidth',2)
        plot(PurgeSam(:,1),PurgeSam(:,2), 'b','LineWidth',2)
        plot(PurgeSam(:,1),PurgeAir(:,2), 'g','LineWidth',2)
        xlabel('Time [ps]')
        ylabel('E [arb. units]')
        legend('Air','Reference', 'black Si','Air1')
        x_limit = [0.05, 2];
        title('Windowed signals ( ' + sample + " )", 'Interpreter','none')
        hold off
        box on
    end 
    
    plotWindowedSignal()
    
    
    
    %% Frequency response
    N = 40000;
    step_size=PurgeRef(3,1)-PurgeRef(2,1); %ps
    df = 1/(N*step_size);
    freq = (linspace(0,N-1,N).*df)';
    data_fft = conj(fft(PurgeSam(:,2),N));
    ref_fft = conj(fft(PurgeRef(:,2),N));
    air_fft = conj(fft(PurgeAir(:,2),N));

    % Phase response
    data_phase = unwrap(angle(data_fft));
    air_phase = unwrap(angle(air_fft))
    ref_phase = unwrap(angle(ref_fft));
    phi=unwrap(ref_phase-air_phase);
    phi1=unwrap(data_phase-air_phase);
    
    function plotPhaseResponse()
        figure;
        hold on;
        plot(freq, phi , 'r','LineWidth',2)
        plot(freq, phi1 , 'b','LineWidth',2)
        title('Unwrapped Phase of Data ( ' + sample + " )", 'Interpreter','none');
        xlabel('Frequency [THz]');
        ylabel('Phase [radians]');
        xlim(x_limit); box on;
        legend('Sample', 'Reference');
        hold off;
    end

    % plotPhaseResponse()
    
    
    %% Uniform refraktive indices
    c=300; %  [µm/ps]
    n  = 1+(phi.*c)./(2*pi.*freq.*d1);
    n1  = 1+(phi1.*c)./(2*pi.*freq.*d2);

    function plotUniformRefaktiveIndex()
        figure
        hold on 
        plot(freq,n1 , 'r','LineWidth',2)
        plot(freq,n , 'b','LineWidth',2)
        xlabel('Frequency [THz]')
        ylabel('Refractive index')
        title('Refraktive equation for uniform materials ( ' + sample + " )", 'Interpreter','none');
        xlim(x_limit); box on;
        legend('Sample', 'Reference');
        hold off 
        box on
    end 
    
    % plotUniformRefaktiveIndex()

    %% Thinfilm refraktive indices
    freq = freq * 1e12;             % Convert from THz to Hz
    omega = 2 * pi * freq;          % Angular frequency
    freq = freq / 1e12;
    c = 2.99e8;                     % Speed of light in m/s
    p_sam = d2*1e-6;                % Sample substrate thickness in meters (530 µm example)
    p_ref = d1*1e-6;                % Reference substrate thickness in meters (525 µm example)
    T_data = data_fft ./ ref_fft;   % Compute complex transmission function T
    
    delta_2 = omega .* n .* (p_sam - p_ref) ./ c; % Assuming p_sam = p2 and p_ref = p1
    T_factor_5_6 = (T_data .* (1 + n - n .* 1i .* omega .* d ./ c)) - (n + 1) .* exp(1i .* delta_2);
    T_denominator_5_6 = T_data .* (1i .* omega .* d ./ c);
    n_f_eq_5_6 = sqrt(T_factor_5_6 ./ T_denominator_5_6);
    
    
    x_limit = [0.8, 1.15];
    function plotThinFilmRefraktiveIndex()
        figure;
        hold on
        plot(freq, n , 'k','LineWidth',2)
        plot(freq, real(n_f_eq_5_6) , 'r','LineWidth',2)
        hold off
        title('Refraktive Index ( ' + sample + " )", 'Interpreter','none');
        xlabel('Frequency [THz]');
        ylabel('Refractive Index');
        xlim(x_limit); box on;
        legend('Reference', 'Srface Layer')
    end 

    plotThinFilmRefraktiveIndex()
    
    %% Volume fraction
    eps_Si = (n).^2;
    eps_CM = (real(n_f_eq_5_6)).^2;
    zeta = ((eps_CM - 1) .* 13.68) ./ (10.68.* (2 + eps_CM));

    function plotVolumeFraction()
        figure;
        hold on
        plot(freq, zeta , 'k','LineWidth',4)
        hold off
        title('Vol Fraction');
        xlabel('Frequency [THz]');
        ylabel('Vol Fraction');
        xlim(x_limit); box on;
    end 
    
    % plotVolumeFraction()
end 

TyndfilmsRefrakativIndeks("16_21")
TyndfilmsRefrakativIndeks("16_22")
TyndfilmsRefrakativIndeks("16_23")
TyndfilmsRefrakativIndeks("16_24")
TyndfilmsRefrakativIndeks("16_25")
TyndfilmsRefrakativIndeks("16_26")
