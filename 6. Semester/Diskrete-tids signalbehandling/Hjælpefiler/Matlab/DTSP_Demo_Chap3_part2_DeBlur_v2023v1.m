%deBlur Motion
%HKa feb. 2022

%Get ready
clear ,close all

%Load image and preprocess image
I=imread('redigerings-billede.tif');    % Tiff udvides til 4 værdier (x, R, G, B) og jeg ved ikke hvad x skal bruges. 
I = I(:, :, 1:3);                   
size(I);
dI=double(I);
dI=dI/max(dI(:));
figure(1), imshow(dI), ; 


%Blurr image, -- blur from motion in x-direction --
%First create filter h
M=9;%M odd
h=ones(1,M);
h=h./sum(h(:))

% h[n] = 1/9 * ( u[n] - u[n-10] )  

%Now filter                     
for r=1:size(dI,1)                  % For løkken flader billedet ud
    dJ(r,:, 1)=filter(h,1,dI(r,:));
end;

[x, y, farver] = size(dI); 
sloeretBillede = reshape(dJ, x, y, farver);
%Show blured image
figure(2),imshow(sloeretBillede), ; 

%Let's deBlur
%First create invers filter to h
L=M*64;%just make it long engoug sinces it IIR, 64 copies will do
for s=1:L
    if (mod(s-1,M)==0) ih(s)=+1; end
    if (mod(s-2,M)==0) ih(s)=-1; end
end
ih(L)=0;


%Mit forsøg: 
% h[n] = 1/9 * ( u[n] - u[n-10] ) <- 1/9 * (1/(1 - z^-1) - z^-10/(1 -
% z^-1))



dJ = sloeretBillede; 
%Now apply invers filter to deBlur
for r=1:size(dJ,1)
    dK(r,:)=filter(ih,1,dJ(r,:));
end

size(dK)
genskabBillede = reshape(dK, x, y, farver);
size(genskabBillede)
%Show deBlured iamge
figure(3),  imshow(genskabBillede/max(dK(:)))% /max(dK(:))),

legend("Original","Blurred", "deblurred")
% Der er noget galt med filteret tror jeg. Den slørede er i hvert fald
% tættere på originalen end den afslørede, så det giver ikke mening.
% Men der har været flere ting i det her dokument som ikke virkede, men som
% jeg selv måtte rette, så ja det undre mig ikke. 
