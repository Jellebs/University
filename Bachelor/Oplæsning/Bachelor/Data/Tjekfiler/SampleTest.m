% Fordi jeg skulle teste, om mine samples var taget i rigtige rækkefølge,
% nedefra op, 1-5.
sample = "16_26"
% PurgeSam = importfileT2("proeve" + sample + '_scan' + 1 + '.pulse.csv'); 
function PurgeSam = makeArray(sample, N)
    % N amounts of samples 
    PurgeSam = importfileT2("Test Filer/" + "proeve" + sample + '_scan' + 1 + '.pulse.csv'); 
    PurgeSam = PurgeSam(117:307, :)

    for i = 2: N
        % if i == 3 
        %     continue 
        % end 
        % 
        path = "Test Filer/" + "proeve" + sample + '_scan' + string(i) + '.pulse.csv';   % "Data/Profiler/proeve16_26_scan1.pulse.csv", ...    
        data = importfileT2(path);
        data = data(117:307, :)
        PurgeSam = [PurgeSam, data(:, 2)];          % Time reference is the same for the rest.
    end
end 
PurgeSam = makeArray(sample, 3)

function plotSignaler(PurgeSam, sample, N)
    figure 
    hold on
    legends = []
    for s = 2:N + 1
        plot(PurgeSam(:,1),PurgeSam(:,s)); 
        legends = [legends, "Sample " + string(s)];
    end 
    xlabel('Time [ps]');
    ylabel('E [arb. units]'); 
    legend(legends); 
    title('Signals ( ' + sample + " )", 'Interpreter','none');  % Keeps the text as is, without formatting 
    hold off
    box on
end 

plotSignaler(PurgeSam, sample, 3)

