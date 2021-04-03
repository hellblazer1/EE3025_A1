#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <string.h>



void fft(double complex* x, int n){

    //allocating memory for even and odd parts of x
    double complex* odd = malloc(n/2 * sizeof(double complex));
    double complex* even = malloc(n/2 * sizeof(double complex));    
    if (n == 1)
        return;
    else{
     //splitting x into even and odd components   
    int i = 0;
    while (2 * i < n) {
        even[i] = x[2 * i];
        odd[i] = x[2 * i + 1];
        i++;
    }
    //calculating fft of even and odd component recursively
    fft(even, n/2);
    fft(odd, n/2);
    //combining the ifft calculated for even and odd parts
    double complex w;
    int j = 0; 
    while ( 2 * j < n) {
        w = CMPLX(cos(2*M_PI*j/n), sin(2*M_PI*j/n));
        x[j] = even[j] + w * odd[j];
        x[j + n/2] = even[j] - w * odd[j];
        j++;
    }
    }
    //freeing the memory allocated to even and odd
    free(even);
    free(odd);
}


void ifft(double complex* y, int n){

    //allocating memory for storing even and odd parts of y
    double complex* odd = malloc(n/2 * sizeof(double complex));
    double complex* even = malloc(n/2 * sizeof(double complex));
    if (n == 1)
        return;
    else{
    //splitting y into even and odd components
    int i =0;
    while (2 * i < n) {
        even[i] = y[2 * i];
        odd[i] = y[2 * i + 1];
        i++;
    }
    //calculating ifft of even and odd component recursively
    ifft(even, n/2);
    ifft(odd, n/2);
    
    //combining the ifft calculated for even and odd parts
    double complex w;
    int j = 0;
    while ( 2 * j < n) {
        w = CMPLX(cos(-2*M_PI*j/n), sin(-2*M_PI*j/n));
        y[j] = even[j] + w * odd[j];
        y[j + n/2] = even[j] - w * odd[j];
        j++;
    }
    }
    //freeing the memory allocated to even and odd
    free(even);
    free(odd);
}




void main()
{
    int n= (1<<20);
    double* x = (double*)malloc(n * sizeof(double));
    double* h = (double*)malloc(n * sizeof(double));
    
    double complex* X = (double complex*)malloc(n * sizeof(double complex));
    double complex* H = (double complex*)malloc(n * sizeof(double complex));
    double complex* Y = (double complex*)malloc(n * sizeof(double complex));
    double complex* ifft_Y = (double complex*)malloc(n * sizeof(double complex));
    
    FILE *fin_1,*fout_1,*fout_2,*fout_3;

    fin_1 = fopen("../data/x.dat","r");
    int index=0;
    while (!feof(fin_1) && index < n) 
    {
        fscanf(fin_1, "%lf", &(x[index]));
        X[index] = CMPLX(x[index],0);
        index++;
    }
   
    //coefficients of numerator and denominator of impulse response of filter
    double a[] = { 1, -2.5194645,2.56083711,-1.20623537,0.22012927};
    double b[] = {0.00345416,0.01381663,0.02072494,0.01381663,0.00345416};
    //computing time domain impulse response of filter
    h[0] = (b[0]/a[0]);
    h[1] = (1/a[0])*(b[1] - a[1]*h[0]);
    h[2] = (1/a[0])*(b[2]- a[1]*h[1]-a[2]*h[0]);
    h[3] = (1/a[0])*(b[3] - a[1]*h[2]-a[2]*h[1]-a[3]*h[0]);
    h[4] = (1/a[0])*(b[4] - a[1]*h[3]-a[2]*h[2]-a[3]*h[1]-a[4]*h[0]);
    
    for(int i=0; i<5;i++)
        H[i] = CMPLX(h[i],0);
    for(int i=5;i<n;i++){
        h[i] = (1/a[0])*(0 - a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-a[4]*h[i-4]);
        H[i] = CMPLX(h[i],0);
    }
    
    //fft of x(input)
    fft(X,n);
    fout_1 = fopen("../data/x_fft.dat","w");
    int i = 0;
    while(i<n)
    {
        fprintf(fout_1,"%lf+%lfi \n",creal(X[i]),cimag(X[i]));
        i++;
    }
    
    //fft of h(time domain impulse response)
    fft(H,n);
    fout_2 = fopen("../data/h_fft.dat","w");
    i =0;
    while(i<n)
    {
        fprintf(fout_2,"%lf+%lfi \n",creal(H[i]),cimag(H[i]));
        i++;
    }
    //computing Y from H and X
    i = 0;
    while(i<n)
    {
        Y[i] = H[i]*X[i];
        ifft_Y[i] = Y[i];
        i++;
    }
    //ifft of Y(frequency domain representation of y)
    ifft(ifft_Y,n);
    fout_3 = fopen("../data/y_ifft.dat","w");
    i=0;
    while(i<n)
    {
        fprintf(fout_3,"%lf \n",creal(ifft_Y[i]/n));
        i++;
    }

    fclose(fin_1);
    fclose(fout_1);
    fclose(fout_2);
    fclose(fout_3);   
}
