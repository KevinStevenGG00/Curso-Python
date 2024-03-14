class A:
    pass
class F(A):
    pass
class B(A):
    pass
class C(F):
    pass
class D(B,C):
    pass

print(D.mro())