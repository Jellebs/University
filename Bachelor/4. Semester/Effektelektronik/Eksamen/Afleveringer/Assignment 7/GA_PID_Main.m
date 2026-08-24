%% Define bounds for Kp, Ki, Kd
Kp_bounds = [0, 10]; 
Ki_bounds = [0, 1]; 
Kd_bounds = [0, 1];

%% Set GA options:
 % options = optimoptions('ga', 'PlotFcn', @gaplotbestf, ...
 %                        'MaxGenerations', 20, 'PopulationSize', 10, ...
 %                       'Display', 'iter', 'UseParallel', false);


options = optimoptions('ga', ...
    'PopulationSize', 500, ...
    'CrossoverFraction', 0.8, ... % Crossover rate
    'MutationFcn', {@mutationadaptfeasible, 0.05}, ... % Mutation function with mutation rate
    'MaxGenerations', 100, ...
    'Display', 'iter', ...
    'PlotFcn', {@gaplotbestf, @gaplotstopping});

%% Call GA:
[x, fval] = ga(@GA_PID_GAIN, 3, [], [], [], [], ...
               [Kp_bounds(1), Ki_bounds(1), Kd_bounds(1)], ...
               [Kp_bounds(2), Ki_bounds(2), Kd_bounds(2)], ...
               [], options);

%% Printing output for PID Gains:
fprintf('---------------------------------\n');
fprintf('|  Gain  |  Optimal Value       |\n');
fprintf('---------------------------------\n');
fprintf('|  Kp    |  %18.4f  |\n', x(1));
fprintf('|  Ki    |  %18.4f  |\n', x(2));
fprintf('|  Kd    |  %18.4f  |\n', x(3));
fprintf('---------------------------------\n');
