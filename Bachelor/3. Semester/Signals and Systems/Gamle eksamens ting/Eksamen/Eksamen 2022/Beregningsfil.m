clear
n = linspace(-5, 5, 100);
h = 2*(heaviside(n) - 2*heaviside(n-5))
x = heaviside(n) - heaviside(n-3)

plot(n, h)
plot(n, x)
y = conv(h, x, "same")
plot(n, y)





%h = 2 if inp = input("n vaerdi") < 5 && inp > 0; 
%hn = []
%for (i = 0; i < 5; i++) 
%    hn.append(h[n[i]])%
%end


% if n[i] > 0 && n[i] < 5 for i in range(len(n))