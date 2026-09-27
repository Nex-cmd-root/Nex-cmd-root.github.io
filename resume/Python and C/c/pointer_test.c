#include <stdio.h>

void add_money (int *ptr);

int main() {

   int wallet = 50;
   add_money(&wallet);
   printf("%d", wallet);

return 0;
}

void add_money (int *ptr) {
   *ptr += 100;
}