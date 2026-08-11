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
    %% Function effiency ( Time spent calculating ) 
    t1 = datetime('now'); 
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
    K = 10;              % Amount of changes made in each size. 
    
    %% Matrix setup
    % Depends on every size, to every scan, for every type
    % nf = zeros(K, K, K, M, L);      % [(var(d's), scans, types]
    % volFrac = zeros(K, K, K, M, L); % [(var(d's), scans, types]
    
    % Ny strategi, nan misinformere ikke, hvis dataen ikke er blevet sat. 
    nf = nan(K, K, K, M, L);      % [(var(d's), scans, types]
    volFrac = nan(K, K, K, M, L); % [(var(d's), scans, types]

    for l = 1:L                                     % For every type
        sample = "16_2" + string(l);
        type = PARAMETERS(sample);
        dref = type{1};     dsam = type{2};     d = type{3};

        % Array of parameters 
        d = (d + linspace(-0.5, 0.5, K))*1e-6;      % +- 0.5um
        dsam = (dsam + linspace(-20, 20, K))*1e-6;  % +- 20um
        dref = (dref + linspace(-20, 20, K))*1e-6;  % +- 20um

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
                        n_tyndfilm = mean(n_tyndfilm);
                        nf(k, i, j, m, l) = real(n_tyndfilm);                 % Re{avg{nf_kij}
                        volFrac(k, i, j, m, l) = volumeFraction(n_tyndfilm);  % volFrac(avg{n_f})
                    end 
                end 
            end 
            disp('Done with scan' + string(m));
            t2 = datetime('now'); 
            dt = t2-t1;
            fprintf('Elapsed time: %.3f s\n', seconds(dt));
        end 
        disp('Done with type' + string(l)); 
        t2 = datetime('now'); 
        dt = t2-t1;
        fprintf('Elapsed time: %.3f s\n', seconds(dt));
    end 
    save('Resultat n_f.mat', "nf"); 
    save('Resultat Volume Fraction.mat', "volFrac"); 
    
    t2 = datetime('now'); 
    dt = t2-t1;
    fprintf('Elapsed time: %.3f s\n', seconds(dt));
    % K = 10 took around 3 hours to calculate. 
end 
% doCalculations()                            % If calculations hasn't occured yet. 


%% Process data
function results = process(nf, volFrac)
    results = nan(6, 6)
    for l = 1: 6                                                            % For every type
        nfType = nf(:, :, :, :, l);
        nfType = nfType(~isnan(nfType));                                    % Array setup, includes nans
        % nfType = nfType(nfType >= 1 & nfType <= 3.43);                      % Boundary constraint, 1 <= nFilm <= nSi
        volFracType = volFrac(:, :, :, :, l)
        volFracType = volFracType(~isnan(nfType))
        results(l, 1) = round(max(nfType(:), [], 'all', 'omitnan')     , 3);
        results(l, 2) = round(mean(nfType(:), 'all', 'omitnan')        , 3);
        results(l, 3) = round(min(nfType(:), [], 'all', 'omitnan')     , 3);% Skal ændres. Da jeg ikke sætter nogle værdier for type 3 scan 5, så er de 0 og skal ikke regnes med. 
        results(l, 4) = round(max(volFracType(:), [], 'all', 'omitnan'), 3);
        results(l, 5) = round(mean(volFracType(:), 'all', 'omitnan')   , 3);
        results(l, 6) = round(min(volFracType(:), [], 'all', 'omitnan'), 3);
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
end 


load('Resultat Volume Fraction.mat')        % Otherwise load data
load('Resultat n_f.mat')

results = process(nf, volFrac)


%% Visualize data
function plotResults(results)
    L = 6; 
    errnfUpper = results(:, 1) - results(:, 2)          % Max - Mu 
    errnfLower = results(:, 2) - results(:, 3)          % Mu - Min
    errvolFracUpper = results(:, 4) - results(:, 5)     % Max - Mu 
    errvolFracLower = results(:, 5) - results(:, 6)     % Mu - Min
    % nf plot
    figure; 
    hold on 
    title("Min, max and avg. distriubtion of the varied depths")
    set(gcf,'Position',[0 1920 800 600])
    for type = 1:L                              % Iterating to make them change color
        errorbar(type, results(type, 2), errnfLower(type), errnfUpper(type), 'o', 'LineWidth', 2.5);
    end 
    grid on
    xlabel('Types');
    ylabel('Refractive index');
    xline(0, 'LineWidth', 1);
    yline(0, 'LineWidth', 1);
    %ylim([-0.1, 4.1])
    ax = gca; 
    ax.FontSize = 15; 
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

function plotGaussianDistribution(nf)
    figure;
    hold on
    set(gcf,'Position',[0 1920 800 600]); 
    L = 6 % Types 
    mus = NaN(L, 1)
    sigmas = NaN(L, 1)
    plot3([-1, 10], [0, 0], [-1, -1], 'Color', 'black', 'LineWidth', 2)
    % sigmas(3) = 0; mus(3) = 0;
    for l = 1: L 
        data = nf(:, :, :, :, l);
        data = data(~isnan(data));                      % Remove nans 
        data = data(data >= 1 & data <= 3.43);
        [mu, sigma] = normfit(data(:));
        mus(l) = mu; 
        sigmas(l) = sigma; 
    end 

    % Visualize the 95% confidence interval from the gaussian distribution 
    K = 50;                                     % Arbitrary amount of steps for every gaussian distribution. 
    uppers = mus + 2 * sigmas;
    lowers = mus - 2 * sigmas;
    
    colors = get(gca, 'ColorOrder');

    % Adds bars to my graph. 
    function bars(barlengths, bary, z)
        barx = [l - barlengths, l + barlengths]; 
        barx = [barx; barx]; 
        surf(barx, bary, z, ...
            'EdgeColor','none', ...
            'FaceColor',colors(l + 1, :), ...
            'FaceAlpha', 'interp', ...
            'AlphaData',z, ...
            'AlphaDataMapping','none')
    end
    for l=1:L    
        linewidth = 0.05; 
        barlengths = 0.3; 
        y = linspace(lowers(l), uppers(l), K);
        x = l * ones(K, 1);
        x = [x.'-linewidth/2; x.'+linewidth/2].'; 
        y = [y-linewidth/2; y+linewidth/2].'
        px = 0.025 + (0.975/(sigmas(l) * sqrt(2*pi)) ) ...
             * exp( - ( (y - mus(l)).^2 )/( 2*sigmas(l)^2 ) );      % The normal probability distribution function
        px = px./max(px);                                            % Normalized for the color gradient to go from 0:1
        z = px; 
        % z = [z; z]; 

        surf(x, y, z, ...
            'EdgeColor','none', ...
            'FaceColor', colors(l + 1, :), ... % [3/252, 252/252, 177/252], ...
            'FaceAlpha', 'interp', ...
            'AlphaData', z, ...
            'AlphaDataMapping','none')
        
         

        barheight = 2 * linewidth; 
        % Top bars
        topbary = [uppers(l)+barheight, uppers(l)+barheight]; 
        topbary = [topbary; uppers(l)- barheight, uppers(l) - barheight];
        
        % Bottom bars
        bottombary = [lowers(l)+barheight, lowers(l)+barheight]; 
        bottombary = [bottombary; lowers(l)- barheight, lowers(l) - barheight];

        z2 = z(1:2, 1:2); 
        bars(0.15, topbary, z2)
        bars(0.15, bottombary, z2)
        % surf(barx, bary, z(1:2, 1:2), ...
        %     'EdgeColor','none', ...
        %     'FaceColor', colors(l + 1, :), ... % [3/252, 252/252, 177/252], ...
        %     'FaceAlpha', 1, ...
        %     'AlphaData', z(1:2, 1:2), ...
        %     'AlphaDataMapping','none')
        % 
    end 
    view(2);
    
    hold off 
    title("Gaussian distribution of the varied depths")
    xlabel("types", 'interpreter', 'latex')
    ylabel("Refractive Index $n_f$", 'Interpreter','latex')
    ylim([-0.1, 4.1])
    ax = gca; 
    grid on
    
    ax.FontSize = 15; 
    
    % title('Refraktive Index ( ' + sample + " )", 'Interpreter','none');
    % xlabel('Frequency [THz]');
    % ylabel('Refractive Index');
    % % xlim(x_limit); box on;
    % % ylim([0, 3.5]); 
    % legend({'Reference', ...
    % '95\% interval: $\hat{x}\pm2\hat{\sigma}$'}, ...
    % 'Interpreter','latex');
    % 

end 



plotGaussianDistribution(nf)
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





























