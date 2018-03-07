/***************************************************************************
 *
 * Copyright © 2016 LT. All Rights Reserved.
 *
 ***************************************************************************/

/**
 *
 * @file: vect3.c
 *
 * @breaf: 
 *
 * @author: Lei Yunfei(towardstheway@gmail.com)
 *
 * @create: 2017/10/24 14时03分09秒
 *
 **/


#include <stdio.h>
#include <stdlib.h>

#include "vect3.h"


Vec3 *Vec3_get(double x, double y, double z, char *label) {
    Vec3 *v = (Vec3 *)malloc(sizeof(Vec3));
    v->x = x;
    v->y = y;
    v->z = z;
    v->label = label;
    return v;
}

void Vec3_delete(Vec3 *v) {
    if (v == NULL)
        return;
    free(v);
    v = NULL;
}

void Vec3_print(Vec3 *v) {
    if (v == NULL)
        return;
    printf("x = %.4f, y = %.4f, z = %.4f, label = %s\n", v->x, v->y, v->z, v->label);
}

void Vec3_add_scalar(Vec3 *v, double s) {
    if (v == NULL)
        return;
    v->x += s;
    v->y += s;
    v->z += s;
}
