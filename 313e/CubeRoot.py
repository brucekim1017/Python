import sys

def cube_root (n):
  tol = 1.0e-6
  m = abs(n)
  if (m < 1):
    lo = m
    hi = 1.0
  else:
    lo = 1.0
    hi = m

  mid_new = (lo + hi) / 2.0
  mid_old = mid_new + 10 * tol
  while (abs(mid_new - mid_old) >= tol):
    cube = mid_new ** 3
    if (cube < m):
      lo = mid_new
    else:
      hi = mid_new
    mid_old = mid_new
    mid_new = (lo + hi) / 2.0

  # check sign of n
  if (n < 0):
    mid_new = (-1) * mid_new

  return mid_new

def main():
  # read n
  line = sys.stdin.readline()
  line = line.strip()
  n = float(line)

  # obtain the cube root and print
  print (cube_root(n))

if __name__ == "__main__":
  main()