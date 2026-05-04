function numeric_data = importFil(filePathAndName)
    % Reads a CSV file with:
    %   - One header row
    %   - Comma-separated values
    %   - Possible NaN or Inf entries
    %
    % Returns: data (table), numeric_data (array), and variable names
    
    % ---- User input ----
    filename = filePathAndName;   % Change this to your file name or path
    
    % ---- Import options ----
    opts = detectImportOptions(filename, 'Delimiter', ' ');  % detect settings
    opts.VariableNamesLine = 1;                              % header row
    opts.MissingRule = 'fill';                               % handle missing values
    opts = setvaropts(opts, 'TreatAsMissing', {'NaN','Inf'});% treat 'NaN'/'Inf' as missing
    
    % ---- Read data, skipping header ----
    numeric_data = readmatrix(filename, ...
        'Delimiter', ',', ...
        'NumHeaderLines', 1);   % skip 1 header row
    
    % ---- Handle NaN/Inf automatically ----
    % readmatrix already converts 'NaN' and 'Inf' strings to numeric NaN/Inf
    
    % ---- Show quick summary ----
    disp('First few rows of numeric data:')
    disp(numeric_data(1:min(5,end), :))
    data = numeric_data
    disp(length(data))
end
