/***************************************************************************
 *
 * Copyright © 2016 LT. All Rights Reserved.
 *
 ***************************************************************************/

/**
 *
 * @file: main.c
 *
 * @breaf: 
 *
 * @author: Lei Yunfei(towardstheway@gmail.com)
 *
 * @create: 2017/10/24 14时15分22秒
 *
 **/


#include <stdio.h>
#include "vect3.h"

int main() {
    double x, y, z;
    x = 1.0;
    y = 2.0;
    z = 3.0;
    char *label = "ssdf";
    Vec3 *v = Vec3_get(x, y, z, label);
    Vec3_print(v);
    Vec3_add_scalar(v, 3.7);
    Vec3_print(v);
    Vec3_delete(v);

    return 0;
}
