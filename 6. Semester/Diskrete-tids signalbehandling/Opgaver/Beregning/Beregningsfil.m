% import("../../Matlab/fold.m")
addpath("../../Matlab/")
% addpath('[../../Matlab/]');
% load ../../Matlab/fold.m 
% load ../../Matlab/shift.m

function opgave2_3()     
    n = -5: 4; % n = [5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    x = [-1, 0, 1, 2, 3, 4, 4, 4, 4, 4]
    xneg = flip(x, 2)
    xnminus3 = [0, 0, 0, x]
    xnplus2 = [x, 0, 0]
    
    [y1, ny1] = fold(x, n)
    [y2, ny2] = shift(x, n, -3)
    [y3, ny3] = shift(x, n, 2)
    
    subplot(4, 1, 1)
    hold on
    stem(n, x)
    
    subplot(4, 1, 2)
    stem(ny1, y1)
    
    subplot(4, 1, 3)
    stem(ny2, y2)
    
    subplot(4, 1, 4)
    stem(ny3, y3)
    legend("xn", "x[-n]", "x[n - 3]", "x[n + 2]")

end 

function opgave2_4()
    % Sequence 
    % repmat(A, r dimension 1, r dimension 2)
    % reshape(A, row, column) 
    sequence = reshape(repmat([1 1 1 1 0 0 0 0 0 0], 5, 1)', 1, []) % repmat gentager på rækkerne, men reshape samler på rækkerne. For at undgå 5 af de samme punkter lige efter hinanden, så transponeres matricen.
    sequence2 = reshape(repmat(cos(0.1*pi*0:9), 5, 1)', 1, []) 
    n = -19:30
    subplot(2, 1, 1)
    stem(n, sequence)
    legend("Bit liste")
    subplot(2, 1, 2)
    stem(n, sequence2)
    legend("Trigonometrisk liste")
    
end 

function opgave2_17()
    b = [0.18, 0.1, 0.3, 0.1, 0.18]
    a = [1, -1.15, 1.5, -0.7, 0.25]
    N = 100
    h = impz(b, a, N)
    n = 0:1:99
    x = (n >= 0) % Boolean operation til at lave unit step function
    y1 = filter(b, a, x)
    y2 = conv(x, h); n2 = 0:1:198
    y3 = filter(h, 1, x)
    function opga() 
        stem(n, h)
    end 
    function opgbc()
        stem(n, y1)
        hold on
        stem(n, y2)
        hold off
    end 
    function opgd()
        stem(n2, y2)
    end 
    tiledlayout(3,1)
    nexttile
    stem(n, y1)
    legend("Filter ud fra overførselsfunktion")
    ax1 = gca; 
    hold on 
    nexttile
    stem(n2, y2)
    legend("Filtreret vha. convolution")
    ax2 = gca; 
    hold on 
    nexttile
    stem(n, y3)
    legend("Filtreret vha. impulsresponse")
    ax3 = gca; 
    linkaxes([ax1, ax2, ax3], 'x');
    hold off
end 

function opgave3_1()
    b = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1/(2^10)]
    a = [1, -1/2]
    pzmap(b, a)
end 
function opgave3_19()
    b = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1/(1024)]
    a = [1, -1/2]
    pzmap(b, a)
    impz(b, a, 10)
end 

% opgave3_19()

function X = gafft(x,N,k)
    % Goertzel’s algorithm
    % X = gafft(x,N,k)
    % Computes k-th sample of an N-point DFT X[k] of x[n]
    % using Goertzel Algorithm
    L = length(x); x = [reshape(x,1,L),zeros(1,N-L+1)];
    K = length(k); X = zeros(1,K);
    for i = 1:K
        v = filter(1,[1,-2*cos(2*pi*k(i)/N),1],x);
        X(i) = v(N+1)-exp(-1j*2*pi*k(i)/N)*v(N);
    end
end

function Goertzel()
    fs = 8000;        % Sampling frequency (for context)
    N = 64;           % DFT size
    k = 3;            % Bin to test
    
    n = 0:N-1;                          % Time vector
    x = cos(2*pi*k/N * n);             % Cosine at bin k
    
    X = gafft(x, N, k);                % Apply Goertzel algorithm
end 


function Opgave_kapitel10()
    wp = 0.25*pi
    ws = 0.35*pi
    
    M = 44; L = M+1; % Impulse response length
    alpha = M/2; Q = floor(alpha); % phase delay parameters
    om = linspace(0,2*pi,1001); % Frequency array
    k = 0:M; % Frequency sample index
    psid = -alpha*2*pi/L*[(0:Q),-(L-(Q+1:M))]; % Desired Phase
    Dw = 2*pi/L; % Width between frequency samples
    % Design
    k1 = floor(wp/Dw); % Index for sample nearest to PB edge
    k2 = ceil(ws/Dw); % Index for sample nearest to SB edge
    w = ((k2-1):-1:(k1+1))*Dw; % Freq in the transition band
    A = 0.5+0.5*cos(pi*(ws-w)/(ws-wp)); % Transition band samples
    B = fliplr(A); % Transition band samples for omega >pi
    Ad = [ones(1,k1+1),A,zeros(1,L-2*k2+1),...
    B,ones(1,k1)]; % Desired Amplitude
    Hd = Ad.*exp(1j*psid); % Desired Freq Resp Samples
    hd = real(ifft(Hd)); % Desired Impulse response
    h = hd.*rectwin(L)'; % Actual Impulse response
    H = freqz(h,1,om) % Frequency response of the actual filter
    freqz(h,1,om)
    
    H_dB = 20*log10(abs(h));      % Convert to dB
    a = om/pi
    % plot(om/pi, H_dB);
    xlabel('Normalized Frequency (\times\pi rad/sample)');
    ylabel('Magnitude (dB)');
    title('Frequency Response');
    grid on;
    
    
    maxmag = max(abs(H))
    dw = 2*pi/1000;
    Asd = min(-20*log10(abs(H(ceil(ws/dw):501))/maxmag))
end 

function Opgave10_10()
    N = 26;                     % Filter order (numtaps - 1)
    Wn = 0.825;                 % Normalized cutoff (relative to Nyquist, so 0.825 * pi
    b = fir1(N, Wn, 'high', hamming(N + 1));    % High-pass filter
    [H, w] = freqz(b, 1, 1024); % High-resolution frequency response
    w = w/pi; 
    % plot(w, abs(H))
    plot(w, 20*log10(abs(H)))
    title('MATLAB fir1 High-pass Filter')
    xlabel('Frequency (\times\pi rad/sample)')
    ylabel('Magnitude (dB)')
    grid on
end 

Opgave10_10()


