#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cJSON.h"

void print_c_json_version()
{
    static char version[15];
    sprintf(version, "%i.%i.%i", CJSON_VERSION_MAJOR, CJSON_VERSION_MINOR, CJSON_VERSION_PATCH);
    printf("cjson version: %s", version);
    return;
}

int main() {
    print_c_json_version();
    return 0;
}
