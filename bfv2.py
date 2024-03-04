import tenseal as ts
from time import time

# Setup TenSEAL context
context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1032193)
context


context.generate_galois_keys()
context.global_scale = 2**40

v1 = [0, 1, 2, 3, 4]
v2 = [4, 3, 2, 1, 0]
print(v1)

# encrypted vectors
enc_v1 = ts.bfv_vector(context, v1)
enc_v2 = ts.bfv_vector(context, v2)


t_start = time()
result = enc_v1 + enc_v2
print(result.decrypt()) # ~ [4, 4, 4, 4, 4]
t_end = time()
print("Time taken for addition is: {} ms".format((t_end - t_start) * 1000))

result = enc_v1.dot(enc_v2)
print(result.decrypt()) # ~ [10]

result = enc_v1*enc_v2
print(result.decrypt()) # ~ [157, -90, 153]

sub = enc_v1-enc_v2
print(sub.decrypt())
