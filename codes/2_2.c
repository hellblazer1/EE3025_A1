# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <complex.h>
# include <math.h>


void main(){
	int n = (1<<20);
	//coefficients of numerator and denominator of time domain impulse response of filter
        double a[] = { 1, -2.5194645,2.56083711,-1.20623537,0.22012927};
        double b[] = {0.00345416,0.01381663,0.02072494,0.01381663,0.00345416};
	double* x = (double*)malloc(n * sizeof(double));
	double* y = (double*)malloc(n * sizeof(double));
	
	FILE *fin, *fout;
	fin = fopen("../data/x.dat","r");
  
	int index = 0;
	while (!feof(fin) && index < n) 
    {
        fscanf(fin, "%lf", &(x[index++]));
    }
    //computing y from difference equation
        y[0] = (b[0]/a[0])*x[0];
	y[1] = (1/a[0])*(b[0]*x[1]+b[1]*x[0] - a[1]*y[0]);
	y[2] = (1/a[0])*(b[0]*x[2]+b[1]*x[1]+b[2]*x[0]- a[1]*y[1]-a[2]*y[0]);
	y[3] = (1/a[0])*(b[0]*x[3]+b[1]*x[2]+b[2]*x[1]+b[3]*x[0]);
	y[3] = y[3] - (1/a[0])*(a[1]*y[2]-a[2]*y[1]-a[3]*y[0]);
	y[4] = (1/a[0])*(b[0]*x[4]+b[1]*x[3]+b[2]*x[2]+b[3]*x[1]+b[4]*x[0]); 
	y[4] = y[4] - (1/a[0])* (a[1]*y[3]-a[2]*y[2]-a[3]*y[1]-a[4]*y[0]);
    for(int i=5;i<n;i++){
		y[i] = (1/a[0])*(b[0]*x[i]+b[1]*x[i-1]+b[2]*x[i-2]+
		        b[3]*x[i-3]+b[4]*x[i-4] - a[1]*y[i-1]-a[2]*y[i-2]-
		        a[3]*y[i-3]-a[4]*y[i-4]);
	}
    //exporting into a .dat file
    fout  = fopen("../data/y.dat", "w");
    int i = 0;
    while(i < n){
        fprintf(fout, "%lf \n", y[i]);
        i++;
    }
    fclose(fin);
    fclose(fout);
}
