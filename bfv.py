import numpy as np
import tenseal as ts

# Setup TenSEAL context
context = ts.context(
            ts.SCHEME_TYPE.BFV,
            poly_modulus_degree=4096,
            plain_modulus=1032193)
#context.generate_galois_keys()
#context.global_scale = 2**40
v1=[2,1,2,3,5]
v2=[4,4,6,8,6]
enc_v1=ts.bfv_vector(context,v1)
enc_v2=ts.bfv_vector(context,v2)
result=enc_v1+enc_v2  
print(result.decrypt())         
            
