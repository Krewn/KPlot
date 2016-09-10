InvestmentReturns=[0.0,0.0,0.0,;-0.01,0.0,0.01,;-0.02,0.0,0.02,;-0.03,0.0,0.03,;-0.04,0.0,0.04,;-0.05,0.0,0.05,;-0.06,0.0,0.06,;-0.07,0.0,0.07,;-0.08,0.0,0.08,;-0.09,0.0,0.09,;];
xName=[99,100,101,];
yName=[0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,];
surf(xName,yName,InvestmentReturns);
view(0,90); shading interp;colorbar;
xlabel("% Return");ylabel("Investment");
title("Gross");
axis("tight");
