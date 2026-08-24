function [cost, simOut] = GA_PID_GAIN(pidGains)
    % pidGains is a vector [Kp Ki Kd]
    
    % Assign the PID gains to the base workspace variables 
    % that the Simulink model will use
    assignin('base', 'Kp', pidGains(1));
    assignin('base', 'Ki', pidGains(2));
    assignin('base', 'Kd', pidGains(3));
    
    % Set the simulation time
    simTime = 10; 
    
    % Run the SIMULINK 
    simOut  = sim('GA_PID_2nd.slx', 'StopTime', num2str(simTime));
    logsout = simOut.logsout;
    vehicleSpeed = logsout.getElement('speed').Values.Data;
    timeData = logsout.getElement('speed').Values.Time;

    % Define performance metric:
    refSpeed = 28; % speed in m/s
    error = (refSpeed - vehicleSpeed).^2; %minimize the integral of the squared error (ISE)
    cost = trapz(timeData, error);
end
