def choose(n, k):
  return reduce(lambda x, y: x*y, xrange(1,n+1)) / \
    (reduce(lambda x, y: x*y, xrange(1,k+1)) * reduce(lambda x, y: x*y, xrange(1,n-k+1)))
print choose(110, 10) + choose(109, 9) - 101 - 901
