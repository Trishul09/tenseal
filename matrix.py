import numpy as np
import tenseal as ts

# Setup TenSEAL context
context = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=8192,
            coeff_mod_bit_sizes=[60, 40, 40, 60])
context.generate_galois_keys()
context.global_scale = 2**40

matrix=np.array([[2,2,3],[3,8,7]])
mat=np.array([[1,8,6],[7,7,5]])


result=matrix.flatten()
print(result)

res=mat.flatten()
print(res)
print()

print(result+res)
print()
print(result*res)
print()

enc_v1 = ts.ckks_tensor(context ,matrix)
enc_v2 = ts.ckks_tensor(context, mat)



#m=[[0,0,0]]
m=enc_v2+enc_v1
print(m.decrypt().tolist())

mul=enc_v2*enc_v1
print(mul.decrypt().tolist())
