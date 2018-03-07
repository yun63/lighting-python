/***************************************************************************
 *
 * Copyright © 2016 LT. All Rights Reserved.
 *
 ***************************************************************************/

/**
 *
 * @file: vect3.h
 *
 * @breaf: 
 *
 * @author: Lei Yunfei(towardstheway@gmail.com)
 *
 * @create: 2017/10/24 12时34分14秒
 *
 **/


#ifndef  VECT3_INC
#define  VECT3_INC

#define HELLO 3

typedef struct {
    double x;
    double y;
    double z;
    char *label;
} Vec3;

Vec3 *Vec3_get(double x, double y, double z, char *label);
void Vec3_print(Vec3 *v);
void Vec3_add_scalar(Vec3 *v, double s);
void Vec3_delete(Vec3 *v);

#endif   // ----- #ifndef VECT3_INC  -----
