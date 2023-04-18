#include <stdio.h>
#include <math.h>

float newton_raphson_32bits(float semilla){
    float iteracion = semilla - ( ((float) sin(semilla)) / ((float) cos(semilla)) );
    if(iteracion != semilla){
        iteracion = newton_raphson_32bits(iteracion);
    }
    return iteracion;
}

double newton_raphson_64bits(double semilla){
    double iteracion = semilla - ( (sin(semilla)) / (cos(semilla)) );
    if(iteracion != semilla){
        iteracion = newton_raphson_64bits(iteracion);
    }
    return iteracion;
}

float serie_leibniz_32bits(size_t n){
    float pi = 0;
    for(size_t i = 0; i < n; i++){
        if(i % 2 == 0){
            pi += ((float) 1/(2*i+1));
        } else {
            pi -= ((float) 1/(2*i+1));
        }
    } 
    return 4 * pi;
}

double serie_leibniz_64bits(size_t n){
    double pi = 0;
    for(size_t i = 0; i < n; i++){
        if(i % 2 == 0){
            pi += ((double) 1/(2*i+1));
        } else {
            pi -= ((double) 1/(2*i+1));
        }
    } 
    return 4 * pi;
}

int main(void){
    printf("La aproximación de pi con flotantes de 32 bits %.7f\n", newton_raphson_32bits(2));
    printf("La aproximación de pi con flotantes de 64 bits %.15lf\n", newton_raphson_64bits(2));
    for(size_t i = 0; i < 5; i++){
        size_t iteraciones = pow(10,i+1);
        printf("La aproximación de pi con la serie de Leibniz con flotantes de 32 bits y %ld términos es %.7f\n", iteraciones, serie_leibniz_32bits(iteraciones));
        printf("La aproximación de pi con la serie de Leibniz con flotantes de 64 bits y %ld términos es %.15lf\n", iteraciones, serie_leibniz_64bits(iteraciones));
    }
    return 0;
}