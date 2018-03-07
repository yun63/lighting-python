# -*- coding:utf-8 -*-

####################################################################################
#
# Copyright © 2017 TU. All Rights Reserved.
#
####################################################################################

"""

@File: test.py

@Description:

@Author: leiyunfei(leiyunfei@tuyoogame.com)

@Depart: 棋牌中心

@Create: 2017-10-24 14:25:55

"""

from cffi import FFI

ffi = FFI()
ffi.cdef(
"""
#define HELLO 3

typedef struct {
    double x;
    double y;
    double z;
    char   *label;
} Vec3;

Vec3 *Vec3_get(double x, double y, double z, char *label);
void Vec3_print(Vec3 *v);
void Vec3_add_scalar(Vec3 *v, double s);
void Vec3_delete(Vec3 *v);
"""
)

lib = ffi.dlopen('./libvect3.so')

v = lib.Vec3_get(1.0, 2.0, 3.0, "http://www.baidu.com")
lib.Vec3_add_scalar(v, 3.0)
lib.Vec3_print(v)

s = v.label
print(s)

if __name__ == '__main__':
    pass
