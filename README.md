# lighting-python


## 1 在遍历过程中修改list的方法

> If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy. Iterating over a sequence does not implicitly make a copy. The slice notation makes this especially convenient:

```
ls = [1, 2, 3, 4]
for e in ls[:]:
    if e == 2:
        ls.remove(e)
print ls ---> [1, 3, 4]
```
