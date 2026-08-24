    %% ETACS, Advanced Control Systems. Aarhus University 
% Martin Ansbjerg Kjær
%
% Parameter file for simulation of Lego Car.
% Version 7.1, 26/1 2021
%
%
Rad2DegFactor = 360/2/pi;
A_Half = 0.5;
One=1;
GravitinationalAcceleration = 9.82;

% Car model parameters
CM_EnableActuatorQuantizer =1;          % Enabeling quantization af actuator. ON = 1; OFF=0.
CM_EnableBlockWheel = 1;                % Enabeling blocking of wheel. ON = 1; OFF=0.
CM_EnableWheelSpin =1;                  %   Enabeling whhel spin. ON = 1; OFF=0.
CM_CarWaight = 2  ;                     % Car waight in kg
CM_WheelRadius = 0.03 ;                 % Wheel radius in meters
CM_RelativeTorqueConstant = 0.0023;     % Relative torque constant in Nm/Voltageunit
CM_ViscousFriction= 0.018;              % Viscous Friction in Nm s/rad                % Coulomb Friction in Nm
CM_WheelSpinInputThresholdStandStill=70;%Threshold for wheel spunning when standing still, relative to avtuator signal         
CM_WheelSpinInputSlope =84.5;           %Threshold adjustmen for wheel spunning when moving. Designed to avoid wheel spin at high speed.0 slope gives speed-independent friction
CM_WheelInertia = 0.000009 ;            % Inertia of wheel and axel (during wheel spin)
CM_PWM_Type    = 1   ;                  % PWM type selector. 1= normal PWM (constant period). 2 = Modulates the on-period but keeps off-period fixed. on period
CM_PWM_FixedOff_offset   =  25 ;        %Fixt-On-PWM offsewt parameter. Tells which input gived 50% duty scycle.
CM_Actuator_NonlinarityType    = 0                  % Actuator non-linarity type. 0: linaer, 1: speed-dependent parabolic nonlinarity.
                                                    % Type 1: Gain=max(1-((abs(CarSpeed)-MaxGainSpeedOffset).^2)*(1-ZeroSpeedGain)/MaxGainSpeedOffset^2,MinGain);
CM_Actuator_SpeedDependent_MaxGainSpeedOffset =.1;  % Actuator non-linarity type 1. Parameter for speed-dependent parabolic nonlinarity.
CM_Actuator_SpeedDependent_ZeroSpeedGain=0.7 %      % Actuator non-linarity type 1. Parameter for speed-dependent parabolic nonlinarity.
CM_Actuator_SpeedDependent_MinGain = 0.5;           % Speed-dependent parabolic nonlinarity. Minimum gain 

% Ultra Sound Sensor
USS_EnableError =1  ;                % Enabeling systematic error af ultra sound sensorr. ON = 1; OFF=0.
USS_EnableSensorQuantizer=1;        % Enabeling quantization af ultra sound sensor. ON = 1; OFF=0.
USS_MinDistance = 0.2;              % Lower limit for sensor accuracy in meters
USS_UnitConversion = 1;             % Unitconversion fram meter to sensor signal
USS_LargeMaxValue =1 ;              % Upper value sensor accuracy in meters
USS_LargeErrorSlope =0.7;           %Slope for sensor in-accuracy.

% DC Motor Angle Sensor
MAS_EnableSensorQuantizer =  1;      % Enabeling quantization af angle sensor. ON = 1; OFF=0.
MAS_EnablePeriodicErrorAmplitude =1;    % Enabeling periodic error af angle sen sor. ON = 1; OFF=0.
MAS_PeriodicErrorAmplitude = 0.7*2*pi/360;    % Amplictude of periodic error in radians   

% Free Wheel Angle Sensor
FWS_EnableSensor = 0;               % Enableer for angular sensor on the free rooling axel.  0: sensor not enabled. 1: sensor enabled.The sensor enharites the propperties of the MAS.


%Enablers

%%Backwards Compabillity:
CM_CoulombFriction = 1; 
CM_EnableCoulombFriction = 0  ;         % Enabeling Coulomb Friction. ON = 1; OFF=0.

