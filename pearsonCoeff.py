#Code to compute the Pearson Coefficient as described at https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
import statistics
import math
def computeCoeff():
    x = [15,12,8,8,7,7,7,6,5,3];
    y = [10,25,17,11,13,17,20,13,9,15]
    xmean = statistics.mean(x);
    ymean = statistics.mean(y);
    numerator = 0;
    xdenom = 0;
    ydenom = 0;
    for i in range(0,len(x)):
        numerator = numerator + (x[i]-xmean) * (y[i]-ymean);
        xdenom = xdenom + pow((x[i]-xmean),2) 
        ydenom = ydenom + pow((y[i]-ymean),2);
    xdenom = math.sqrt(xdenom);
    ydenom = math.sqrt(ydenom);
    coeff = numerator/(xdenom*ydenom);
    print("Coeffcient:"+str(round(coeff,3)))

computeCoeff()
