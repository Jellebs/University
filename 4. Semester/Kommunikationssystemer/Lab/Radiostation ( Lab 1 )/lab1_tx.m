center_frequency            = 434.0e6;
stop_time                   = 16;
USRP_frame_length           = 4000;
USRP_front_end_sample_rate  = 48e3;
USRP_time_frame             = USRP_frame_length / USRP_front_end_sample_rate;

audiofilereader = dsp.AudioFileReader('guitartune.wav', ...
    'SamplesPerFrame', 4410);

fprintf("Initialising radio...\n")
radio = comm.SDRuTransmitter( ...
    'Platform',         'N200/N210/USRP2', ...
    'IPAddress',        '192.168.10.2', ...
    'CenterFrequency',  center_frequency, ...
    'Gain',             30);  % dB

fprintf("Initialising modulator...\n")
fmBroadcastMod = comm.FMBroadcastModulator( ...
    'SampleRate', 200e3, ...
    'FrequencyDeviation', 50e3, ...  % EU standard
    'FilterTimeConstant', 50e-5, ...  % EU standard
    'AudioSampleRate', 48e3, ...
    'Stereo', false);

fprintf("Transmitting...\n")

current_time = 0;
while current_time < stop_time
    fprintf("Sending transmission. Time: %.3f s\n", current_time)
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
