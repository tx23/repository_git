#include <stdio.h>

int g(int x) {
    return x+3;
}

int f(int y) {
    return g(1);
}

int main(void) {
    return f(8) + 1;
}
