% Spectrogram of linear FM signal

clear; close all;


set(0,'DefaultAxesFontName','Times','DefaultAxesFontUnits','points',...
   'DefaultAxesFontSize',8,'DefaultTextFontName','Times',...
   'DefaultTextFontUnits',...
   'points','DefaultTextFontSize',8);

f1=figure;
set(f1,'PaperPosition',[1 1 5 5]);

Fs=1000; % Hz
T=1/Fs;

T1=10; %  sec
F1=Fs/2;
t=(0:T:T1)';

%x0=chirp(t,0,F1,T1);
b=F1/T1; Ft=b*t; %x=cos(pi*(Ft.*t));
xc=sin(pi*b*t.*t); 
%xc=cos(pi*b*t.*t);


subplot(3,1,1)

S1=spectrogram0(xc,50,256,50,Fs);
xlabel('\it t \rm (sec)');
ylabel('\it F \rm(Hz)');
axis([0 10 0 500])
title('(a)')

subplot(3,1,2)

%S=spectrogram(xc,200,100,256,1000);
%imagesc(log(flipud(abs(S)))); colorbar


%specgram(xc,256,1000,hanning(200),100);

S2=spectrogram0(xc,200,256,50,Fs);
xlabel('\it t \rm (sec)');
ylabel('\it F \rm(Hz)');
axis([0 10 0 500])
title('(b)')
%colorbar

T1=10; %  sec
F1=Fs;
t=(0:T:T1)';

%x0=chirp(t,0,F1,T1);
b=F1/T1; Ft=b*t; %x=cos(pi*(Ft.*t));
xc2=sin(pi*b*t.*t); 
%xc2=cos(pi*b*t.*t);

subplot(3,1,3)
S3=spectrogram0(xc2,200,256,50,Fs);
xlabel('\it t \rm (sec)');
ylabel('\it F \rm(Hz)');
axis([0 10 0 500])
title('(c)')
%colorbar

f2=figure;
set(f2,'PaperPosition',[1 1 5 4]);

n=1:1000;
nw=(1:200)+700;
w=hanning(200);
wc=zeros(size(n)); wc(nw)=w;
wc=wc(:);

subplot(3,1,1), plot(t(n),xc(n),t(n),wc); box off
ylabel('Amplitude');
xlabel('\itt\rm( sec )');
title('(a)')

subplot(3,1,2), plot(t(n),xc(n).*wc); box off
ylabel('Amplitude');
xlabel('\itt\rm( sec )');
title('(b)')

xw=xc(nw).*w(:); 
Xw=fft(xw,1024);
F0=(1:512)'*Fs/1024;

subplot(3,1,3), plot(F0, abs(Xw(1:512))); box off
ylabel('Amplitude');
xlabel('\itF\rm( Hz )');
title('(c)');

f3=figure;
set(f3,'PaperPosition',[1 1 5 3]);

n0=1:2000;
x0=xc(n0);

Nfft=2^15;
Xc=fft(x0,Nfft);
F0=(-Nfft/2+1:Nfft/2)'*Fs/Nfft;

subplot(2,1,1), plot(t(n0),x0); box off
ylabel('Amplitude');
xlabel('\itt\rm( sec )');
title('(a)')

%subplot(2,1,2), plot(F0, abs(Xc(1:Nfft/2))); box off

subplot(2,1,2), plot(F0, abs(fftshift(Xc))); box off
ylabel('Amplitude');
xlabel('\itF\rm( Hz )');
title('(b)');




