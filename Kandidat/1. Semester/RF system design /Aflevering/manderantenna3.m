%% Meander-line antenna at 1060 MHz - Hertz dipole model
clear; clc; close all;

%% Parameters
res = 30;                          % Hertz dipole resolution [segments per wavelength]
f = 1060e6;  c = 3e8;  lam = c/f;  k = 2*pi/lam;  eta = 120*pi;   % eta: impedance of free space
hs = 3.2e-2;                       % substrate thickness h = 3.2 cm, as given in the paper
eff = 4;                           % effective permittivity (given)

% Guided wavelength, paper eq. (5)
lg = lam/sqrt(eff);
w = 0.05*lg;  d = 0.16*lg;  s = 0.42*lg;  L = 0.70*lg;    % paper, eqs. (1)-(4)

fprintf('--- Design values (paper, Section III) ---\n');
fprintf('lambda   = %.2f mm\n', lam*1e3);
fprintf('eps_eff  = %.3f\n', eff);
fprintf('lambda_g = %.2f mm\n', lg*1e3);
fprintf('d = %.2f mm,  s = %.2f mm,  L = %.2f mm,  w = %.2f mm\n\n', d*1e3, s*1e3, L*1e3, w*1e3);

%% Geometry: centerline corner points (x,y), feed at the top, open end at the bottom
y1 = L/2 - (L-3*d)/2;
P = [-s/2  L/2;
     -s/2  y1;      s/2  y1;
      s/2  y1-d;   -s/2  y1-d;
     -s/2  y1-2*d;  s/2  y1-2*d;
      s/2  y1-3*d; -s/2  y1-3*d;
     -s/2 -L/2];
figure; plot(P(:,1), P(:,2), 'k', 'LineWidth', 2);
axis equal; grid on; title('Meander centerline [m]');

%% Split the wire into Hertz dipoles (each shorter than lam/res)
C = [];  U = [];  h = [];  sp = [];  s0 = 0;      % centre, direction, length, distance from feed
for n = 1:size(P,1)-1
    v   = P(n+1,:) - P(n,:);                      % one straight piece of wire
    len = norm(v);
    N   = ceil(len/(lam/res));                    % number of dipoles on this piece
    t   = ((1:N)' - 0.5)/N;                       % dipole centres as a fraction of the piece
    C   = [C;  P(n,:) + t*v];
    U   = [U;  repmat(v/len, N, 1)];
    h   = [h;  repmat(len/N, N, 1)];
    sp  = [sp; s0 + t*len];
    s0  = s0 + len;                               % s0 ends up as the total wire length
end
fprintf('Hertz dipoles: %d\n', numel(h));
fprintf('Longest dipole: %.2f mm (small-dipole limit min(s,d)/2 = %.2f mm)\n', max(h)*1e3, min(s,d)/2*1e3);
if max(h) > min(s,d)/2, warning('Dipoles longer than the limit: increase res'); end

%% Current: standing wave, zero at the open end (as for the dipole in Lecture 1)
I  = sin(k*(s0 - sp));
wt = I.*h;                                        % weight of each dipole

%% Radiation pattern
% Angle a is measured from broadside (+z). E-plane = y-z plane, H-plane = x-z plane.
a  = linspace(-pi, pi, 1441);  a(end) = [];
z  = zeros(size(a));
Ee = farfield([z; sin(a); cos(a)].', C, U, wt, k);
Eh = farfield([sin(a); z; cos(a)].', C, U, wt, k);
Emax   = max([Ee; Eh]);                       % strongest value found in either cut
Ee_rel = Ee/Emax;   Eh_rel = Eh/Emax;         % both cuts on one common scale (used for the printout below)
Ee = Ee/max(Ee);    Eh = Eh/max(Eh);          % each cut normalised to its own peak (dB plot, beamwidths)
Exy = farfield([sin(a); cos(a); z].', C, U, wt, k);     % x-y plane cut (angle from +y), for the textbook E-plane
Exy = Exy/max(Exy);

figure; plot(rad2deg(a), 20*log10(Ee), rad2deg(a), 20*log10(Eh));
hold on; plot([-180 180], [-3 -3], 'k--');
grid on; ylim([-30 3]);
xlabel('Angle from +z [deg]'); ylabel('|E| normalised to each cut''s peak [dB]');
legend('E-plane', 'H-plane', '-3 dB', 'Location', 'south');

[T, PH] = ndgrid(linspace(0,pi,91), linspace(0,2*pi,181));
[sx, sy, sz] = sph2cart(PH, pi/2 - T, 1);         % unit vectors toward the observer
S3 = [sx(:) sy(:) sz(:)];
[E3, Ev3] = farfield(S3, C, U, wt, k);
H3 = sqrt(sum(abs(cross(S3, Ev3, 2)/eta).^2, 2)); % far field: H = (s x E)/eta
E3 = reshape(E3/max(E3), size(T));   H3 = reshape(H3/max(H3), size(T));
[X, Y, Z] = sph2cart(PH, pi/2 - T, E3);           % distance from centre = |E|
figure; surf(X, Y, Z, E3, 'EdgeColor', 'none');
axis equal; grid on; colorbar;
xlabel('x'); ylabel('y'); zlabel('z'); title('Normalized |E| pattern');

%% 3 dB beamwidths (width of the lobe around the peak where |E| >= 1/sqrt(2))
cuts = {Ee, Eh, Exy};  bw = nan(1,3);
for q = 1:3
    bw(q) = lobe(cuts{q}, a);
end
D = 41253/(bw(1)*bw(2));                          % directivity from the beamwidths

%% Figure 4: 3D pattern of the normalised |H| (same construction as the |E| pattern in Figure 3)
% In the far field H = (s x E)/eta, so H is perpendicular to both s and E and |H| = |E|/eta.
[X, Y, Z] = sph2cart(PH, pi/2 - T, H3);
figure; surf(X, Y, Z, H3, 'EdgeColor', 'none');
axis equal; grid on; colorbar;
xlabel('x'); ylabel('y'); zlabel('z'); title('Normalized |H| pattern');

%% Figures 5 and 6: all three planes, for the |E| pattern and for the |H| pattern
planeDir  = {[sin(a); cos(a); z].', [z; sin(a); cos(a)].', [sin(a); z; cos(a)].'};   % x-y, y-z, x-z cuts
planeName = {'x-y plane', 'y-z plane', 'x-z plane'};
planeRole = {'textbook E-plane', 'our E-plane = textbook H-plane', 'our H-plane'};
hAxis = {'x', 'y', 'x'};   vAxis = {'y', 'z', 'z'};    % axes of each plot; the angle is measured from the vertical axis
fieldName = {'|E|', '|H|'};
Fe = cell(1,3);  maxDiff = 0;
for fld = 1:2                                          % 1: |E| pattern, 2: |H| pattern
    figure('Position', [100 100 1200 450]);            % wide figure: three plots side by side
    for p = 1:3
        [Em, Evec] = farfield(planeDir{p}, C, U, wt, k);
        if fld == 1
            F = Em;
        else
            F = sqrt(sum(abs(cross(planeDir{p}, Evec, 2)/eta).^2, 2));   % H = (s x E)/eta
        end
        F = F/max(F);                                  % each cut normalised to its own peak
        if fld == 1
            Fe{p} = F;
        else
            maxDiff = max(maxDiff, max(abs(F - Fe{p})));
        end
        [b, pk, ed] = lobe(F, a);
        subplot(1,3,p);
        plotAngle(F, a, ed, pk, b, [fieldName{fld} ', ' planeName{p}], [hAxis{p} '   (' planeRole{p} ')'], vAxis{p});
    end
end

%% Paper formulas, eqs. (12)-(15)
k0 = pi/(sqrt(eff)*L);
tE = 2*asind(sqrt(7.03/((3*L^2 + hs^2)*k0^2)));
tH = 2*asind(sqrt(1/(2 + k0*w)));
Dp = 41253/(tE*tH);

%% Results
fprintf('\n%-22s %12s %12s\n', '', 'Simulation', 'Paper eqs.');
fprintf('%-22s %9.1f deg %9.1f deg\n', 'E-plane 3 dB angle', bw(1), tE);
fprintf('%-22s %9.1f deg %9.1f deg\n', 'H-plane 3 dB angle', bw(2), tH);
fprintf('%-22s %9.2f dBi %9.2f dBi\n', 'Directivity', 10*log10(D), 10*log10(Dp));

[~, iE] = max(Ee_rel);
fprintf('\nStrongest direction: %.0f deg from +z, in the E-plane cut (y-z plane)\n', abs(rad2deg(a(iE))));
fprintf('Peak of the H-plane cut: %.1f dB below the strongest direction\n', -20*log10(max(Eh_rel)));
fprintf('\nTextbook planes: E-plane (x-y) %.1f deg, H-plane (y-z) %.1f deg, D = %.2f dBi\n', ...
        bw(3), bw(1), 10*log10(41253/(bw(3)*bw(1))));
fprintf('\nFar-field check: max difference between the normalised |E| and |H| patterns = %.1e (3D), %.1e (cuts)\n', ...
        max(abs(E3(:) - H3(:))), maxDiff);

%% Far field of the summed Hertz dipoles
function [E, Ev] = farfield(S, C, U, wt, k)
% S: M x 3 unit vectors toward the observer;  C, U: N x 2 dipole centres / directions
% wt: N x 1 (current*length).  Each dipole gives  wt*(s*(s.u) - u)*exp(j*k*s.r0)
ph = exp(1j*k*(S(:,1:2)*C.')) .* wt.';            % M x N phase term
su = S(:,1:2)*U.';                                % M x N, s.u
Ex = sum(ph.*(su.*S(:,1) - U(:,1).'), 2);
Ey = sum(ph.*(su.*S(:,2) - U(:,2).'), 2);
Ez = sum(ph.*(su.*S(:,3)), 2);
E  = sqrt(abs(Ex).^2 + abs(Ey).^2 + abs(Ez).^2);
Ev = [Ex Ey Ez];                                  % complex E-field vector (second output)
end

%% Pattern drawn "polar style" with the 3 dB lobe shaded
function plotAngle(E, a, ed, pk, bw, name, hLab, vLab)
% E: cut normalised to its peak;  a: angles [rad], measured from the vertical axis (0 = up)
% ed: lobe edges [rad];  pk: peak direction [rad];  bw: 3 dB angle [deg]
hold on;
th = a.';
for lobe = [0 pi]                                 % the pattern is symmetric: the opposite direction has the same lobe
    aa = linspace(ed(1), ed(2), 60) + lobe;       % angles inside this 3 dB lobe
    fill([0 sin(aa) 0], [0 cos(aa) 0], [0.8 0.9 1], 'EdgeColor', 'none');   % shaded 3 dB lobe
    plot([0 sin(aa(1))],   [0 cos(aa(1))],   'r');                         % the two edges of the lobe
    plot([0 sin(aa(end))], [0 cos(aa(end))], 'r');
    plot(0.707*sin(aa([1 end])), 0.707*cos(aa([1 end])), 'ro', 'MarkerFaceColor', 'r');
    text(0.4*sin(pk+lobe), 0.4*cos(pk+lobe), sprintf('%.1f deg', bw), ...
         'HorizontalAlignment', 'center', 'FontWeight', 'bold');
end
plot(E.*sin(th), E.*cos(th), 'b', 'LineWidth', 1.5);                        % the pattern
hc = plot(0.707*sin(0:0.05:2*pi), 0.707*cos(0:0.05:2*pi), 'k--');          % -3 dB level = circle of radius 0.707
legend(hc, 'circle radius 0.707 (-3 dB)', 'Location', 'southoutside');
set(gca, 'XTick', [-1 -0.707 0 0.707 1], 'YTick', [-1 -0.707 0 0.707 1]);   % ticks at the circle radius
axis equal; axis([-1.1 1.1 -1.1 1.1]); grid on;
xlabel(hLab); ylabel(vLab);
title(sprintf('%s: 3 dB angle = %.1f deg', name, bw));
end

%% 3 dB width of the lobe around the peak of a full-circle cut
function [bw, pk, ed] = lobe(E, a)
% E: cut normalised to its peak;  a: angles [rad].  Returns the 3 dB angle bw [deg],
% the peak direction pk [rad] and the two lobe edges ed [rad] (NaN if the cut never drops below -3 dB).
bw = NaN;  pk = NaN;  ed = [NaN NaN];
[~, i] = max(E);
E = circshift(E, 1-i);                            % put the peak at index 1
jr = find(E < 1/sqrt(2), 1);                      % first sample below -3 dB, going right
jl = find(E(end:-1:2) < 1/sqrt(2), 1);            % first sample below -3 dB, going left
if ~isempty(jr)
    bw = (jr + jl - 2)*360/numel(E);
    pk = a(i);
    ed = a(i) + [-(jl - 0.5), (jr - 1.5)]*2*pi/numel(E);
end
end