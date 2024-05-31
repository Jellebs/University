findsdru


LYDFIL = "Chris&Chokoladefabrikken.wav"; 
RADIO_STATION_FREQUENCY = 100e6; % Hz 
stop_time = 16; 
USRP_frame_length = 4000; 
USRP_front_end_sample_rate = 48e3;


USRP_time_frame = USRP_frame_length / USRP_front_end_sample_rate;
current_time = 0;


% Radio 
radio = comm.SDRuTransmitter(...
    "Platform", "N200/N210/USRP2", ...  
    "IPAddress", "192.168.10.2");
radio.CenterFrequency = RADIO_STATION_FREQUENCY; 
radio.Gain = 30; % dB

% Audio til digital repræsentation 
audiofilereader = dsp.AudioFileReader(LYDFIL, ...
"SamplesPerFrame", 4410);

% Frequency modulation ( FM ) 
fmBroadcastMod = comm.FMBroadcastModulator(...
    "SampleRate", 200e3, ...
    "FrequencyDeviation", 50e3, ...
    "FilterTimeConstant", 50e-5, ...
    "AudioSampleRate", 48e3, ...
    "Stereo", false)


% Afsend 
while current_time < stop_time
    fprintf("Sending transmission. Time: %.3f s\n", current_time)
    % Your task: Transmitting data ...
    audioData = audiofilereader();
    modulatedData = fmBroadcastMod(audioData);
%     transmittedSignal = TransmitterFilter(modulatedData);  % may need a Square root Raised Cosine Transmit Filter
    transmittedSignal = modulatedData;
    radio(transmittedSignal);

    current_time = current_time + USRP_time_frame;
end

release(fmBroadcastMod)
release(radio)
release(audiofilereader)

