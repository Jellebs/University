% conceptestcode.m


% Kode til at virke placering af poler og deres egenskab på stabiliteten. 

%%
r=1.
theta=pi/7
a=[1 -2*r*cos(theta) r^2]

figure(1)
h=zplane(1,a)

figure(2)
impz(1,a,101)
%%
r=0.98
theta=pi/13
a=[1 -2*r*cos(theta) r^2]

figure(3);
zplane(1,a);

figure(4)
impz(1,a,101)
%%
r=0.91
theta=pi/13
a=[1 -2*r*cos(theta) r^2]

f=figure(5);
zplane(1,a);

figure(6)
impz(1,a,101)