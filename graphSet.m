function graphSet(X,Y)
clf
scatter(X,Y,'b');
refline([0 0]);
hold on
xlabel('AFINN');
ylabel('Z-SCORE');
yL = get(gca,'YLim');
line([0 0],yL,'Color','b');
hold on
end