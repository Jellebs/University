clear all
close all

function TyndfilmsRefrakativIndeks(sample, args) 
    % Function that for every section will have a plot if wanted.
    % Comment it if unwanted
    %% Hardcoded type parameters:
    PARAMETERS = containers.Map;

    
    % MEASURED VALUES
    %   Type                d_ref[µm]  d_sam[µm]   d_thinfilm
    PARAMETERS('16_21') = {   523.92,     518.9,     1.1e-6}; 
    PARAMETERS('16_22') = {   523.92,     519.6,       2e-6};
    PARAMETERS('16_23') = {   523.92,     495.8,       6e-6}; 
    PARAMETERS('16_24') = {   523.92,     510.4,       9e-6};
    PARAMETERS('16_25') = {   523.92,     496.8,       7e-6}; 
    PARAMETERS('16_26') = {   523.92,     501.2,     5.5e-6}; 

    if exist('args', 'var')                                                 % If arguments has been given to the functiion
        print("hej"); 
        if args == 'Min'
            % CALCULATED MIN VALUES
            PARAMETERS('16_21') = {   513.92,     498.9,     1.6e-6};       % Min
            PARAMETERS('16_22') = {   513.92,     499.6,     2.5e-6};       % Min
            PARAMETERS('16_23') = {   503.92,     475.8,     6.5e-6};       % Min
            PARAMETERS('16_24') = {   523.92,     500.4,     9.5e-6};       % Min
            PARAMETERS('16_25') = {   513.92,     506.8,     7.5e-6};       % Min
            PARAMETERS('16_26') = {   513.92,     481.2,     6e-6};         % Min
        elseif args == 'Max'
            % CALCULATED MAX VALUES
            PARAMETERS('16_21') = {   543.92,     498.9,     0.6e-6};       % Max
            PARAMETERS('16_22') = {   543.92,     499.6,     1.5e-6};       % Max
            PARAMETERS('16_23') = {   533.92,     475.8,     5.5e-6};       % Max
            PARAMETERS('16_24') = {   543.92,     490.4,     8.5e-6};       % Max
            PARAMETERS('16_25') = {   523.92,     476.8,     6.5e-6};       % Max
            PARAMETERS('16_26') = {   543.92,     481.2,     5e-6};         % Max
        end
    end 
    
    
    
    

    
    
    
    
    % Unload parameters 
    type = PARAMETERS(sample); 
    
    d1   =    type{1}; %    [µm] thickness of the reference substrate 
    d2   =    type{2}; %    [µm] thickness of the SAMPLE substrate
    d    =    type{3}; %    Thin-film thickness in meters (10 nm example)


    %% Data setup
    data_dir = "Data/Profiler/";
    
    PurgeRef = importfileT2(data_dir + "ren_silicium525_2_scan1.pulse.csv");
    PurgeAir = importfileT2(data_dir + "luft_500middel.pulse.csv");
    PurgeSam = importfileT2(data_dir + "proeve" + sample + '_scan' + 1 + '.pulse.csv'); 
    N = size(PurgeAir, 1);
    
    for i = 2: 5                                    % 1 has already been put into the array. 
        path = data_dir + "proeve" + sample + '_scan' + string(i) + '.pulse.csv';   % "Data/Profiler/proeve16_26_scan1.pulse.csv", ...    
        data = importfileT2(path);
        PurgeSam = [PurgeSam, data(:, 2)];          % Time reference is the same for the rest.
    end  
    
    function plotSignaler()
        figure 
        hold on
        plot(PurgeRef(:,1),PurgeAir(:,2));
        plot(PurgeRef(:,1),PurgeRef(:,2));
        legends = []; 
        for s = 2:6
            legends = [legends, "Scan " + string(s - 1)]
            plot(PurgeSam(:,1),PurgeSam(:,s)); 
        end 
        xlim([1622, 1624])
        xlabel('Time [ps]');
        ylabel('E [arb. units]'); 
        legend(['Air','Reference', legends]); 
        title('Signals ( ' + sample + " )", 'Interpreter','none');  % Keeps the text as is, without formatting 
        hold off
        box on
    end 
    % plotSignaler()
   
    %%  Window  
    % Førhenværende måde
    s1 = 117
    s2 = s1; 
    p1 = 307; 
    p2 = p1; 

    PurgeAir = PurgeAir (s1:p1,:);
    PurgeRef = PurgeRef (s2:p2,:);
    PurgeSam = PurgeSam (s2:p2,:);

    % % Finding the offsets: 
    % [val, argmax] = max(PurgeSam(:, 2:end)); 
    % [val, argmax1] = max(PurgeAir(:, 2)); 
    % [val argmax2] = max(PurgeRef(:, 2));
    % 
    % [val, argmin] = min(PurgeSam(:, 2:end)); 
    % [val, argmin1] = min(PurgeAir(:, 2)); 
    % [val, argmin2] = min(PurgeRef(:, 2)); 
    % argmax = [argmax1, argmax2, argmax];
    % argmin = [argmin1, argmin2, argmin];
    % c = int16((argmax + argmin)/2);
    % [val, argminc] = min(c)
    % L = c(2) - c(1);                % Amount of points having been shifted due to the wafer.
    % M = min(400/2, c(argminc)) * 2; % Width of the window. Can only ever be twice the size of one of the centers,
    %                                 % unless its larger then 400/2 then I would want a window of length 400. 
    % O = c - M/2;                    % Offsets to give the windows.
    % O(O <= 0) = 1; 
    % % Window creation
    % H = zeros(N, size(c,2));        % R^{7 x N}
    % for i=1:size(c, 2)
    %     offset = O(i);
    %     H(offset:offset + M-1, i) = tukeywin(M, 0.5); 
    % end 
    % function plotWindows()
    %     figure 
    %     hold on
    %     legends = [];
    %     for i=1:7
    %         legends = [legends, "Window " + string(i)];
    %         plot(H(:, i));
    %     end 
    %     legend(legends)
    %     hold off
    % end 
    % % plotWindows()
    % 
    % % Applying the windows
    % PurgeAir(:, 2) = PurgeAir(:, 2) .* H(:, 1); 
    % PurgeRef(:, 2) = PurgeRef(:, 2).* H(:, 2); 
    % PurgeSam(:, 2:end) = PurgeSam(:, 2:end) .* H(:, 3:end);
    function plotWindowedSignal()
        figure 
        hold on
        plot(PurgeRef(:,1),PurgeAir(:,2) , 'k','LineWidth',2); 
        plot(PurgeRef(:,1),PurgeRef(:,2) , 'r','LineWidth',2); 
        legends = []; 
        for s = 2:6 
            plot(PurgeSam(:,1),PurgeSam(:,s), 'LineWidth',2); 
            legends = [legends, 'black Si sample ' + string(s - 1)];
        end 
        % xlim([1622, 1624])
        xlabel('Time [ps]')
        ylabel('E [arb. units]')
        legend(['Air', 'Reference', legends]) % legend(['Air', 'Reference', legends])
        title('Windowed signals ( ' + sample + " )", 'Interpreter','none')
        hold off
        box on
    end 
    % plotWindowedSignal()
    
    
    %% Frequency response
    x_limit = [0.8, 4];
    N = 40000;
    step_size=PurgeRef(3,1)-PurgeRef(2,1); %ps
    df = 1/(N*step_size);
    freq = (linspace(0,N-1,N).*df)';
    data_fft = conj(fft(PurgeSam(:,2:6),N)); % conj(fft(PurgeSam(:,2:6),N));
    ref_fft = conj(fft(PurgeRef(:,2),N)); % conj(fft(PurgeRef(:,2),N));
    air_fft = conj(fft(PurgeAir(:,2),N)); %  conj(fft(PurgeAir(:,2),N));

    % Phase response
    data_phase = unwrap(angle(data_fft));
    air_phase = unwrap(angle(air_fft)); 
    ref_phase = unwrap(angle(ref_fft));
    phi= unwrap(ref_phase-air_phase);
    phi1= unwrap(data_phase-air_phase);
    % absolute value for positive convention. 

    function plotPhaseResponse()
        figure;
        hold on;
        plot(freq, phi , 'r','LineWidth',2);
        legends = []; 
        for s = 1:length(phi1(1, :))
            legends = [legends, 'Sample ' + string(s)];
            plot(freq, phi1(:, s) ,'LineWidth',2); 
        end 
        
        title('Unwrapped Phase of Data ( ' + sample + " )", 'Interpreter','none');
        xlabel('Frequency [THz]');
        ylabel('Phase [radians]');
        xlim(x_limit); box on;
        legend(['Reference', legends])
        hold off;
    end
    % plotPhaseResponse()

    function plotTransmissionFunctions()
        figure;
        hold on;
        legends = []; 
        for s = 1:length(phi1(1, :))
            T = data_fft./ ref_fft; 
            legends = [legends, 'Sample ' + string(s)];
            plot(freq, unwrap(angle(T)),'LineWidth',2); 
        end 
        
        title('Transmissions functions ( ' + sample + " )", 'Interpreter','none');
        xlabel('Frequency [THz]');
        ylabel('Phase [radians]');
        xlim(x_limit); box on;
        legend(['Reference', legends]);
        hold off;
    end
    % plotTransmissionFunctions()
    
    %% Uniform refraktive indices
    c=300; %µm/ps
    
    n  = 1+ phi.*c./(2*pi.*freq.*d1);
    n1  = 1 + phi1.*c./(2*pi.*freq.*d2); 
    function plotUniformRefaktiveIndex()
        figure
        hold on 
        
        plot(freq,n , 'b','LineWidth',2); 

        legends = []; 
        for s = 1:length(phi1(1, :))
            legends = [legends, 'Sample ' + string(s)];
            % plot(freq, n1(:, s) ,'LineWidth',2); 
        end 

        xlabel('Frequency [THz]')
        ylabel('Refractive index')
        title('Refraktive equation for one layer uniform wafer')
        % title('Refraktive equation for uniform materials ( ' + sample + " )", 'Interpreter','none');
        xlim(x_limit); box on;
        % ylim([3.3, 3.5])
        legend("n_{si}")
        % legend(['Reference', legends]);
        hold off 
        box on
    end 
    % plotUniformRefaktiveIndex()
    nref = 1 + phi.*c./(2*pi.*freq.*d1);

    %% Thinfilm refraktive indices
    freq = freq * 1e12;             % Convert from THz to Hz
    omega = 2 * pi * freq;          % Angular frequency
    freq = freq / 1e12;
    c = 2.99e8;                     % Speed of light in m/s
    p_sam = d2*1e-6;                % Sample substrate thickness in meters (530 µm example)
    p_ref = d1*1e-6;                % Reference substrate thickness in meters (525 µm example)
    T = data_fft ./ ref_fft;        % Compute complex transmission function T
    
    
    %  = n; % = 1 + phi.*c./(2*pi.*freq.*d1);% n; 
    % P_air = exp(1i * (nref - 1) .* (omega/c) * (p_sam - p_ref)) .* exp(1i * (omega/c) * d); % .* exp(1i .* (omega/c) * (p_ref - p_sam));
    P_air = exp(1i * (nref - 1) .* (omega/c) * (p_sam - p_ref)) .* exp(1i * (omega/c) * d); % .* exp(1i .* (omega/c) * (p_ref - p_sam)); 
    f = freq * 1e12; 
    
    % n_f_eq_5_6 = sqrt((1/d) * (c./omega) .* (n + 1).*(1 +(P_air./T)) -
    % n);                                               3 - 5 - 6 - 4- 1 -2
    % n_f_eq_5_6 = sqrt(1i*(c./(omega * d)) .* (n + 1).*(1 - P_air./T) - n); 
    n_f_eq_5_6 = sqrt((c./(1i * omega * d)) .* (nref + 1) .* (1 - P_air./T) - nref); 

    
    function plotThinFilmRefraktiveIndex()
        figure;
        hold on
        set(gcf,'Position',[0 1920 500 350]); 
        plot(freq, n , 'k','LineWidth',2);
        
        legends = []; 
        for s = 1:length(n_f_eq_5_6(1, :))
            legends = [legends, 'Srface Layer ( Sample ' + string(s) + " )"];
            plot(freq, real(n_f_eq_5_6(:, s)) ,'LineWidth',2);
        end 

        
        hold off
        title('Refraktive Index ( ' + sample + " )", 'Interpreter','none');
        xlabel('Frequency [THz]');
        ylabel('Refractive Index');
        xlim(x_limit); box on;
        ylim([-0.1, 4])
        legend(['Reference', legends])
    end 
    plotThinFilmRefraktiveIndex()

    function plotMinMaxThinFilmRefraktiveIndex()
        if args == 'Min' 
            figure;
            hold on
            plot(freq, n , 'k','LineWidth',2);
        end 
        
        
  
        legends = []; 
        set(gcf,'Position',[0 1920 800 600])
        set(gca,'ColorOrderIndex',2)            % Ensures, that every color corresponds to the sample of the same scan. "Reference" takes colorindex 1, the scans comes after. 
        colororder(lines(6))                    % 6 plots before plotting for the same scans. Ensures same color for same scan.
        for s = 1:length(n_f_eq_5_6(1, :))
            legends = [legends, 'Srface Layer ( Sample ' + string(s) + " )"];
            
            plot(freq, real(n_f_eq_5_6(:, s)),'LineWidth',2);
        end 

        if args == 'Max'
            hold off
            title('Refraktive Index ( ' + sample + " )", 'Interpreter','none');
            xlabel('Frequency [THz]');
            ylabel('Refractive Index');
            xlim(x_limit); box on;
            legend(['Reference', legends])
        end 
    end 
    % plotMinMaxThinFilmRefraktiveIndex()
    
    function plotGaussianDistributedRefraktiveIndices() 
        figure;
        hold on
        set(gcf,'Position',[0 1920 800 600]); 
        plot(freq, n , 'k','LineWidth',2);
        df = 20/40000;                              % 20 THz by 40000 frequency points. 
        nfspectra = real(n_f_eq_5_6); 
        nfspectra = nfspectra(x_limit(1)/df: x_limit(2)/df, :);
        [muhat, sigmahat] = normfit(nfspectra.'); 

        % Visualize the 95% confidence interval from the gaussian distribution 
        N = int16((x_limit(2) - x_limit(1))/df);            
        K = 50;                                     % Arbitrary amount of steps for every gaussian distribution. 
        upper = muhat + 2 * sigmahat;
        lower = muhat - 2 * sigmahat;
        Ny = NaN(N, K); 
        Z = NaN(N, K); 
        for n = 1:N
            y = linspace(lower(n), upper(n), K); 
            px = ( 1/(sigmahat(n) * sqrt(2*pi)) ) ...
                 * exp( - ( (y - muhat(n)).^2 )/( 2*sigmahat(n)^2 ) );      % The normal probability distribution function
            px = px/max(px);                                                % Normalized for the color gradient to go from 0:1
            Z(n, :) = px; 
            Ny(n, :) = y;
        end 
        X = repmat(linspace(x_limit(1), x_limit(2), N), K, 1).';                            % Ensures a (N, K) grid. 
        C = ones(size(X));                                                  % The gradient of the colors should be none existing but be constant.
        
        size(X), size(Z), size(C)
        s = surf(X, Ny, Z, C);                                              % Surface plot
        
        alpha_data = Z;                                                     % Going from fully opaque towards transparent. 
        set(s,...
            'AlphaData',alpha_data,...
            'FaceColor',[3/252, 252/252, 177/252], ...
            'EdgeColor', 'none', ...
            'FaceAlpha','interp',...
            'AlphaDataMapping','none');

        view(2);
        title('Refraktive Index ( ' + sample + " )", 'Interpreter','none');
        xlabel('Frequency [THz]');
        ylabel('Refractive Index');
        xlim(x_limit); box on;
        ylim([0, 3.5]); 
        legend({'Reference', ...
        '95\% interval: $\hat{x}\pm2\hat{\sigma}$'}, ...
        'Interpreter','latex');
        
    end 
    % plotGaussianDistributedRefraktiveIndices() 

    %% Volume fraction
    eps_Si = (n).^2;
    eps_CM = (real(n_f_eq_5_6)).^2;
    zeta = ((eps_CM - 1) .* 13.68) ./ (10.68.* (2 + eps_CM));

    function plotVolumeFraction()
        figure;
        hold on
        
        legends = []; 
        for s = 1:length(zeta(1, :))
            legends = [legends, 'Sample ' + string(s)];
            plot(freq, zeta(:, s), 'LineWidth', 2);
        end 
        title('Vol Fraction sample' + sample);
        xlabel('Frequency [THz]');
        ylabel('Vol Fraction');
        legend(legends); 
        xlim(x_limit); 
        hold off
        box on;
    end 
    % plotVolumeFraction()
end 

% Testing measured sizes
TyndfilmsRefrakativIndeks("16_21")
TyndfilmsRefrakativIndeks("16_22")
% TyndfilmsRefrakativIndeks("16_23")
TyndfilmsRefrakativIndeks("16_24")
TyndfilmsRefrakativIndeks("16_25")
TyndfilmsRefrakativIndeks("16_26")

% Testing uncertainty sizes equaling the minimum and maximum values
% TyndfilmsRefrakativIndeks("16_21", 'Min')
% TyndfilmsRefrakativIndeks("16_21", 'Max')
% TyndfilmsRefrakativIndeks("16_22", 'Min')
% TyndfilmsRefrakativIndeks("16_22", 'Max')
% % TyndfilmsRefrakativIndeks("16_23", 'Min')
% % TyndfilmsRefrakativIndeks("16_23", 'Max')
% TyndfilmsRefrakativIndeks("16_24", 'Min')
% TyndfilmsRefrakativIndeks("16_24", 'Max')
% TyndfilmsRefrakativIndeks("16_25", 'Min')
% TyndfilmsRefrakativIndeks("16_25", 'Max')
% TyndfilmsRefrakativIndeks("16_26", 'Min')
% TyndfilmsRefrakativIndeks("16_26", 'Max')
