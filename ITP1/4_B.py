import math

r_str = input()
r = float(r_str)

m = r**2 * math.pi
s = r * 2 * math.pi

print(f"{m:.6f} {s:.6f}")