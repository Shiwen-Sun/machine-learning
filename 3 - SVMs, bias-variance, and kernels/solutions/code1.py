### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

w = np.array([0.7, -1])
norme = np.linalg.norm(w)
w = w/norme
w0 = 0.4/norme
M = y*(np.dot(X,w) + w0)
print("margin =", np.min(M))
