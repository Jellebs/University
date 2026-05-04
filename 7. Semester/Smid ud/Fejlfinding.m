function findFejl(filNavn)
    filename = filNavn;   % <-- change
    
    % read all lines (R2019b+)
    lines = readlines(filename, 'EmptyLineRule','preserve');
    nlines = numel(lines);
    
    % pattern that accepts decimal, exponential, NaN, Inf
    numPattern = '^\s*([+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?|NaN|nan|Inf|inf)\s*$';
    numcols_expected = 3;
    
    isnum = false(nlines,1);
    for i = 1:nlines
        toks = strsplit(strtrim(lines(i)), ',');
        if numel(toks)~=numcols_expected
            continue
        end
        ok = true;
        for j = 1:numcols_expected
            s = strtrim(toks{j});
            if isempty(s)
                % treat empty as allowed (will be NaN)
                continue
            end
            if isempty(regexp(s,numPattern,'once'))
                ok = false; break
            end
        end
        isnum(i) = ok;
    end
    
    % find all consecutive numeric runs and print them
    runs = [];
    i = 1;
    while i <= nlines
        if isnum(i)
            j = i;
            while j <= nlines && isnum(j), j = j+1; end
            runs(end+1,:) = [i, j-1]; %#ok<SAGROW>
            i = j;
        else
            i = i+1;
        end
    end
    
    disp('Numeric runs (start .. end) and lengths:');
    for k = 1:size(runs,1)
        fprintf('%d .. %d   (len = %d)\n', runs(k,1), runs(k,2), runs(k,2)-runs(k,1)+1);
    end
    
    % show a preview around the first run (if any)
    if ~isempty(runs)
        s = max(1, runs(1,1)-5);
        e = min(nlines, runs(1,2)+5);
        fprintf('\nPreview lines %d..%d:\n', s, e);
        for L = s:e
            fprintf('%4d: %s\n', L, lines(L));
        end
    end
end 