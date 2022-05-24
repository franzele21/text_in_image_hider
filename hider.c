#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "jpeglib.h"

int main() {
    char* fname = "test.jpg";

    if (access(fname, F_OK) == 0) {
        FILE* outfile = fopen(fname, "wb");
        printf("Image %s was found\n", fname);
    }
    else {
        printf("%s:%d The file %s doesn't exists\n", __FILE__, __LINE__, fname);
        exit(0);   
    }
    return 0;
}