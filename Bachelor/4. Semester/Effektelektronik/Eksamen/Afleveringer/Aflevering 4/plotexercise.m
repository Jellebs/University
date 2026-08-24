%% Run and the tasks will be shown as a slideshow()
task1()
task2()
task3()



%% Plot the following functions... 
function task1()
    % Settings 
    ax = gca;
    ax.XAxisLocation = 'origin';
    ax.YAxisLocation = 'origin';
    xlabel("x")
    ylabel("y")
    grid on
    pause on % to enable pause function

    x = linspace(0.05, 10, 100)
    plot(x, 1./x, LineStyle="-.", Color="Blue")
    pause(5); 
    plot(x, sin(x).*cos(x), LineStyle= ":", Color="Red")
    pause(5); 
    plot(x, 2*(x.^2) -3*x + 1, LineStyle= ":", Color="Green")
    pause(5);
    
end 

%% Given a function s of an angle, plot s.
function task2() 
    angle = deg2rad(linspace(0, 360, 361))
    a = 1; b = 1.5; c = 0.3; 
    s = a*cos(angle) + sqrt(b^2 - (a*sin(angle)-c).^2)
    plot(angle, s)
    pause(5); 
end 

%% Plot eclipsoidal functions. 
function task3()
    % Circle of 5 
    angle = deg2rad(linspace(0, 360, 361));
    [x, y] = circle(5, angle); 
    plot(x, y)
    pause(5)

    % Function from 0 -> 360°
    [x, y] = circle(1, angle)
    x = x.*sqrt(2.*cos(2.*angle))
    y = y.*sqrt(2.*cos(2.*angle))
    plot(x, y)
    pause(5)

    % Logarithmic spiral
    [x, y] = circle(1, angle)
    scalar = exp(0.1.*angle)
    x = x.*scalar
    y = y.*scalar
    plot(x, y)


    function [x, y] = circle(r, angle)
        x = r.*cos(angle);
        y = r.*sin(angle);
    end
end 