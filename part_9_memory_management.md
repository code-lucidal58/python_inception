# Memory Management

## Reference counting
```python
x = 10
a = x
```
`x` is pointing to an address. When `x` is assigned to `a`, `a` is also referencing the same address that `x` is. Python
Memory Manager, maintains a table as to how many references are made to a particular memory address. This is called 
**reference counting**. Once the count drops to zero, the memory location is released. Modules like `sys` and `ctype` provide
functions to access the reference count table.
```python
import ctypes
import sys

x = [1, 2, 3]
a = x
print(id(a))
print(id(x))  # same as id(a)
print(sys.getrefcount(a))  # 3
print(ctypes.c_long.from_address(id(a)).value)  # 2
```
Parameters are passed by reference in Python. That is why in `sys.getrefcount`, the count is increased by 1, as the parameter
in the function is also making a reference to the memory location. To remove this issue, the `ctype` module can be used. 
When the count is 0, the memory is released and might be being used by other programs. Hence, it is dangerous to deal directly
with memory.

## Circular Reference
```python
my_var = objectA
objectA.var1 = ObjectB
```
In the above code, if `my_var` is deleted, `objectA` and `objectB` will also be destroyed. Suppose, there is a circular
reference as follows:
```python
my_var = objectA
objectA.var1 = ObjectB
objectB.var1 = objectA
```
When `my_var`, is deleted, the reference count for `objectA` is not 0, because it is referenced by `objectB.var1`. Same
goes for `objectB`. It is also not deleted by Python Memory Manager. This will result to *memory leaks*. 
These reference care deleted by Garbage Collector

## Garbage Collector (GC)
It can be controlled programmatically using the `gc` module. By default, it is turned on. You can turn off, but beware.
Garbage Collector works on the memory, periodically. You may manually call it, as well.  
Below Python 3.4, there was a catch in GC. Objects that had `__del__` and are involved in circular reference, order of the
object destruction would be important. The GC does not know the order, hence it will leave it as it is, and are called 
*uncollectable*. This lead to memory leak.
```python
import ctypes
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "object exists"
    return "Not found"

class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: self: {hex(id(self))}, b: {hex(id(self.b))}')

class B:
    def __init__(self, a):
        self.a = a
        print(f'B: self: {hex(id(self))}, a: {hex(id(self.a))}')

gc.disable()
my_var = A()
# B: self: 0x10efc10d0, a: 0x10f03da00
# A: self: 0x10f03da00, b: 0x10efc10d0
a_id = id(my_var)
b_id = id(my_var.b)
print(ref_count(a_id))  # 2
print(ref_count(b_id))  # 1
print(object_by_id(a_id))  # object exists
print(object_by_id(b_id))  # object exists
my_var = None
print(ref_count(a_id))  # 1
print(ref_count(b_id))  # 1
print(object_by_id(a_id))  # object exists
print(object_by_id(b_id))  # object exists
gc.collect()
print(object_by_id(a_id))  # not found
print(object_by_id(b_id))  # not found
print(ref_count(a_id))  # <random number>
print(ref_count(b_id))  # <random number>
```
Once object is deleted, the address will be allotted to som other tasks, hence the last to statements of the obove code 
will print junk value.

## Shared References and Mutability
```python

```