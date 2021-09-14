# the formula of Lattice paths in a i x j grid is ==> factorial (i + j)/(factorial(i)xfactorial(j))
# https://codereview.stackexchange.com/questions/128810/calculate-the-lattice-paths-in-an-nn-lattice-project-euler-15

from math import factorial as f
i, j = map(int, input("Enter grid dimensions? ").split())
print(f(i + j) // f(i) // f(j))
