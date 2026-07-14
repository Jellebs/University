clear all
close all

%% Equations 
function n_f = nTyndFilm(sample, scanNumber, dref, dsam, d)
    %% Data setup
    data_dir = "Data/Profiler/";
    
    PurgeRef = importfileT2(data_dir + "ren_silicium525_2_scan1.pulse.csv");
    PurgeAir = importfileT2(data_dir + "luft_500middel.pulse.csv");
    PurgeSam = importfileT2(data_dir + "proeve" + sample + '_scan' + scanNumber + '.pulse.csv'); 
    
    %%  Window 
    s1=117;
    p1=307;
    PurgeAir = PurgeAir (s1:p1,:);
    
    s2=117;
    p2=307;
    PurgeRef = PurgeRef (s2:p2,:);
    PurgeSam = PurgeSam (s2:p2,:);

    %% Frequency response
    c = 2.99e8;                     % Speed of light in m/s
    N = 40000;
    step_size=PurgeRef(3,1)-PurgeRef(2,1); %ps
    df = 1/(N*step_size);
    freq = (linspace(0,N-1,N).*df)';
    data_fft = conj(fft(PurgeSam(:,2),N));
    ref_fft = conj(fft(PurgeRef(:,2),N));
    air_fft = conj(fft(PurgeAir(:,2),N));
    
    T = data_fft ./ref_fft;

    % I need from 0.8THz to 1.15THz
    % Stepsize = 0.05ps. df = 1/(4*10^4 * 0.05) = 1/(0.2 * 10^4) = 5*10^-4
    % 0.8 = 5*10^-4*i1 
    % 1.15 = 5*10^-4*i2
    
    i1 = int16(0.8 / (5*10^-4));     % 1600 
    i2 = int16(1.15 / (5*10^-4));    % 2300
    
    % Calculate for relevant frequencies
    freq = freq(i1:i2, :);
    T = T(i1:i2, :); 
    ns = 3.43; % Approximately. 

    freq = freq * 1e12;             % Convert from THz to Hz
    omega = 2 * pi * freq;          % Angular frequency
    
    
    delta_2 = omega .* ns .* (dsam - dref) ./ c; % Assuming p_sam = p2 and p_ref = p1
    T_factor_5_6 = (T .* (1 + ns - ns .* 1i .* omega .* d ./ c)) - (ns + 1) .* exp(1i .* delta_2);
    T_denominator_5_6 = T .* (1i .* omega .* d ./ c);
    n_f = sqrt(T_factor_5_6 ./ T_denominator_5_6);          % eq 5_6
end 
function zeta = volumeFraction(nf)
    ns = 3.43; % Approximately.
    eps_Si = (ns).^2;
    eps_CM = (real(nf)).^2;
    zeta = ((eps_CM - 1) .* 13.68) ./ (10.68.* (2 + eps_CM));
end 


%% Calculation
function doCalculations()
    %% Setup
    % Hardcoded type parameters:
    PARAMETERS = containers.Map;
    %   Type                d_ref[µm]  d_sam[µm]   d_thinfilm[µm]
    PARAMETERS('16_21') = {   523.92,     518.9,     1.1}; 
    PARAMETERS('16_22') = {   523.92,     519.6,       2};
    PARAMETERS('16_23') = {   523.92,     495.8,       6}; 
    PARAMETERS('16_24') = {   523.92,     510.4,       9};
    PARAMETERS('16_25') = {   523.92,     496.8,       7}; 
    PARAMETERS('16_26') = {   523.92,     501.2,     5.5};

    L = 6;              % Amount of types to calculate for
    M = 5;              % Amount of scans for each type.
    K = 5;              % Amount of changes made in each size. 
    
    %% Matrix setup
    % Depends on every size, to every scan, for every type
    % nf = zeros(K, K, K, M, L);      % [(var(d's), scans, types]
    % volFrac = zeros(K, K, K, M, L); % [(var(d's), scans, types]
    
    % Ny strategi, nan misinformere ikke, hvis dataen ikke er blevet sat. 
    nf = nan(K, K, K, M, L);      % [(var(d's), scans, types]
    volFrac = nan(K, K, K, M, L); % [(var(d's), scans, types]

    for l = 1:L                                     % For every type
        sample = "16_2" + string(l)
        type = PARAMETERS(sample)
        dref = type{1};     dsam = type{2};     d = type{3}

        % Array of parameters 
        d = (d + linspace(-0.5, 0.5, K))*1e-6       % +- 0.5um
        dsam = (dsam + linspace(-20, 20, K))*1e-6   % +- 20um
        dref = (dref + linspace(-20, 20, K))*1e-6   % +- 20um

        for m = 1:M                                 % For every scan 

            if l == 3
                if m == 5
                    continue                        % Type 3 is missing a 1 scan. 
                end             
            end 

            for j = 1: K                            % For every change in sizes: 
                for k = 1: K
                    for i = 1: K
                        n_tyndfilm = nTyndFilm(sample, m, dref(j), dsam(k), d(i));                             
                        nf(k, i, j, m, l) = real(mean(n_tyndfilm));                 % Re{avg{nf_kij}
                        volFrac(k, i, j, m, l) = volumeFraction(mean(n_tyndfilm));  % volFrac(avg{n_f})
                    end 
                end 
            end 
        end 
    end 
    save('Resultat n_f.mat', "nf")
    save('Resultat Volume Fraction.mat', "volFrac")
end 
% doCalculations()                            % If calculations hasn't occured yet. 


%% Process data
function results = process(nf, volFrac)
    gaussianResults = nan(6, 4)                 % Results as a gaussian distribution
    results = nan(6, 6)
    for l = 1: 6                                % For every type
        nfType = nf(:, :, :, :, l)
        nfType = nfType(~isnan(nfType))
        volFracType = volFrac(:, :, :, :, l)
        volFracType = volFracType(~isnan(nfType))
        results(l, 1) = round(max(nfType(:), [], 'all', 'omitnan')     , 3);
        results(l, 2) = round(mean(nfType(:), 'all', 'omitnan')        , 3);
        results(l, 3) = round(min(nfType(:), [], 'all', 'omitnan')     , 3); % Skal ændres. Da jeg ikke sætter nogle værdier for type 3 scan 5, så er de 0 og skal ikke regnes med. 
        results(l, 4) = round(max(volFracType(:), [], 'all', 'omitnan'), 3);
        results(l, 5) = round(mean(volFracType(:), 'all', 'omitnan')   , 3);
        results(l, 6) = round(min(volFracType(:), [], 'all', 'omitnan'), 3);
        [muHat1, SigmaHat1] = normfit(nfType(:));
        [muHat2, SigmaHat2] = normfit(volFracType(:));
        gaussianResults(l, 1) = muHat1; 
        gaussianResults(l, 2) = SigmaHat1; 
        gaussianResults(l, 3) = muHat2; 
        gaussianResults(l, 4) = SigmaHat2; 
        
    end     
    T = array2table(results, ...
        'VariableNames', { ...
            'nf_max','nf_mean','nf_min', ...
            'volFrac_max','volFrac_mean','volFrac_min' ...
        });
    T.Typer = (1:6).';         
    T = movevars(T, 'Typer', 'before', 1);
    writetable(T, 'results.xlsx');
    save('Resultat n_f.mat', "nf")
    
    H = array2table(gaussianResults, ...
        'VariableNames', { ...
            'x̂_nf','σ̂_nf', ...
            'x̂_volFrac','σ̂_volFrac' ...
        });
   
    H.Typer = (1:6).';       
    H = movevars(H, 'Typer', 'before', 1);
    writetable(H, 'GaussianResults.xlsx');
    
    
end 


load('Resultat Volume Fraction.mat')        % Otherwise load data
load('Resultat n_f.mat')
results = process(nf, volFrac)


%% Visualize data
function plotResults(results)
    L = 6; 
    errnfUpper = results(:, 1) - results(:, 2)    % Max - Mu 
    errnfLower = results(:, 2) - results(:, 3)    % Mu - Min
    errvolFracUpper = results(:, 4) - results(:, 5)    % Max - Mu 
    errvolFracLower = results(:, 5) - results(:, 6)    % Mu - Min
    % nf plot
    figure; 
    hold on 
    set(gcf,'Position',[0 1920 800 600])
    for type = 1:L                              % Iterating to make them change color
        errorbar(type, results(type, 2), errnfLower(type), errnfUpper(type), 'o', 'LineWidth', 2.5);
    end 
    grid on
    xlabel('Types');
    ylabel('Refractive index');
    xline(0, 'LineWidth', 1);
    yline(0, 'LineWidth', 1);
    hold off
    
    % Volume Fraction plot
    figure; 
    hold on 
    set(gcf,'Position',[0 1920 800 600])
    for type = 1:L                              % Iterating to make them change color
        errorbar(type, results(type, 5), errvolFracLower(type), errvolFracUpper(type), 'o', 'LineWidth', 2.5);
    end 
    grid on
    xlabel('Types');
    ylabel('Volume Fraction');
    xline(0, 'LineWidth', 1);
    yline(0, 'LineWidth', 1);
    hold off
end 

plotResults(results)








%% Min max calculations
maxvaerdier = []
minvaerdier = []

function [indicesMin, indicesMax] = retrieveIndicesMinMax(fiveDArray)
    % Find the min max indices of the last of the 5 dimensions
    % array = zeros(K, K, K, M, L) : [(var(d's), scans, types]
    % last dimensions of the array = Iteration over the types, L.
    
    
    % Returns 3D matrix in R^(L, 3)
    % indicesMin = [(idxmindsam_1, idxmind_1, idxminref_1),
    %               (                ...                 ), 
    %               [(idxmindsam_L, idxmind_L, idxminref_L)] 
    % indicesMax = [(idxmaxdsam_1, idxmaxd_1, idxmaxref_1),
    %               (                ...                 ), 
    %               [(idxmaxdsam_L, idxmaxd_L, idxmaxref_L)] 
    
    L = 6; % Amount of types 

    indicesMin = nan(L, 3);
    indicesMax = nan(L, 3);
    function [idxMin, idxMax] = indicesForType(type)
        type = fiveDArray(:, :, :, :, type); 
        [~, indexMax] = max(type(:));
        [~, indexMin] = min(type(:));
        [idxmaxdsam, idxmaxd, idxmaxdref, ~] = ind2sub(size(type), indexMax);
        [idxmindsam, idxmind, idxmindref, ~] = ind2sub(size(type), indexMin);
        idxMin = [idxmindref, idxmindsam, idxmind];
        idxMax = [idxmaxdref, idxmaxdsam, idxmaxd]; 
    end 
    
    
    for l = 1:L 
        [minIdx, maxIdx] = indicesForType(l);
        indicesMin(l, :) = minIdx; 
        indicesMax(l, :) = maxIdx; 
    end 
end 

[indicesMin, indicesMax] = retrieveIndicesMinMax(nf);





























