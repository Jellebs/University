%deBlur Motion
%HKa feb. 2022

%Get ready
clear ,close all

%Load image and preprocess image
I=imread('Futtog.png');
dI=double(I);
dI=dI/max(dI(:));
figure, imshow(dI), title('Original image');

%Blurr image, -- blur from motion in x-direction --
%First create filter h
M=9;%M odd
h=ones(1,M);
h=h./sum(h(:));

%Now filter
for r=1:size(dI,1)
    dJ(r,:)=filter(h,1,dI(r,:));
end;

%Show blured image
figure, imshow(dJ), title('Blurred image');

%Let's deBlur
%First create invers filter to h
L=M*64;%just make it long engoug sinces it IIR, 64 copies will do
for s=1:L
    if (mod(s-1,M)==0) ih(s)=+1; end;
    if (mod(s-2,M)==0) ih(s)=-1; end;
end;
ih(L)=0;

%Now apply invers filter to deBlur
for r=1:size(dJ,1)
    dK(r,:)=filter(ih,1,dJ(r,:));
end;

%Show deBlured iamge
figure, imshow(dK/max(dK(:))), title('deBlurred image')