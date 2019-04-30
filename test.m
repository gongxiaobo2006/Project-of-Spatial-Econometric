%空间相关性检验（示例）
W=normw(W);
info.lflag=0;
y=data(:,4);
x=[ones(33,1) data(:,7)];
ydev=y-mean(y);
morani=moran(ydev,x,W);
lmerr=lmerror_panel(ydev,x,W);
rlmerr=lmerror_robust_panel(ydev,x,W);
lmlag=lmlag_panel(ydev,x,W);
rlmlag=lmlag_robust_panel(ydev,x,W);
%空间计量模型检验（示例）
W=normw(W2_6);
info.lflag=0;
y=data(:,4);
x=[ones(33,1) data(:,7)];
ydev=y-mean(y);
vnames=strvcat('y','constant','prp');
sarres=sar(ydev,x,W,info);
semres=sem(ydev,x,W,info);
betastd=sarres.bstd;
rhostd=sarres.pstd;
lr=lratios(ydev,x,W);
prt(sarres,vnames);
prt(semres,vnames);