# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <complex.h>
# include <math.h>

void main(){
        //coefficients of numerator and denominator of time domain impulse response
	double a[] = { 1, -2.5194645,2.56083711,-1.20623537,0.22012927};
        double b[] = {0.00345416,0.01381663,0.02072494,0.01381663,0.00345416};
	int n = (1<<20);
	double* h = (double*)malloc(n * sizeof(double)); 
	
        h[0] = (b[0]/a[0]);
	h[1] = (1/a[0])*(b[1] - a[1]*h[0]);
	h[2] = (1/a[0])*(b[2]- a[2]*h[0]-a[1]*h[1]);
	h[3] = (1/a[0])*(b[3] -a[2]*h[1] -a[3]*h[0] -a[1]*h[2]);
	h[4] = (1/a[0])*(b[4] - a[2]*h[2]-a[1]*h[3]-a[3]*h[1]-a[4]*h[0]);
    for(int i=5;i<n;i++){
		h[i] = (1/a[0])*(0 - a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-a[4]*h[i-4]);
	}
    FILE *fout;
    fout  = fopen("../data/h.dat", "w");
    int i = 0;
    while(i < n){
        fprintf(fout, "%lf \n", h[i]);
        i++;
    }
    fclose(fout);
}
