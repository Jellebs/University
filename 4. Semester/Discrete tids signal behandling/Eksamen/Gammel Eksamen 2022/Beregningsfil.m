z = tf('z')

G = (z-2)/(z+1/2)
% zplane([1, -2], [1, 1/2])
% zplane([1,-2.70711, 1.41421, 0],[1, -0.914214, 0.292893, 0.5])


G = tf([2, 1], [1, -1/2])
margin(G)
% Gcl = feedback(G, 1)
% impulse(Gcl)