import math


def dotproduct(vector_i, vector_j):
  return sum((a*b) for a, b in zip(vector_i, vector_j))

def length(vector):
  return math.sqrt(dotproduct(vector, vector))

def cosine_distance(vector_i, vector_j):
    return dotproduct(vector_i, vector_j) / (length(vector_i) * length(vector_j))



def hamming_distance(vector_i, vector_j):
    dist = sum(xi != yi for xi, yi in zip(vector_i, vector_j))
    return dist


