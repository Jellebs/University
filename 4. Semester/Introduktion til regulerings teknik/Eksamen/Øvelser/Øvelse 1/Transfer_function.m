close all; clc

%%
s=tf('s'); %%% s bliver Laplace operator
%% Øvelse nr. 1: Modellering af BlackBox


% 1. Stepresponse

K = 1;

y2_peak = 2.5;
y2_min = -2.5;

x1_start = 232;
x1_slut = 160;
t_rise_1 = x1_start - x1_slut;

x2_start = 290;
x2_slut = 364;
t_rise_2 = x2_slut - x2_start;

% t_c => hvor man har 0.368*V_A
t_c = 310e-03 - 290e-03;
V_A = 2.5-(-2.5);

% G(s)
G_s = K*(1/t_c)/(s+(1/t_c));
bode(G_s);margin(G_s);
grid on