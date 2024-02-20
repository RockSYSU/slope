
import numpy as np



x = np.array([1,2,2,1])
y = np.array([1,2,2,1])
z = np.array([1,1,2,2])
#
def trans_rotate(x, y, z, px, py, pz, alpha, beta, gamma):
    alpha, beta, gamma = np.deg2rad(alpha), np.deg2rad(beta), np.deg2rad(gamma)
    Rx = [[1, 0, 0, 0],
          [0, np.cos(alpha), -np.sin(alpha), py * (1 - np.cos(alpha)) + pz * np.sin(alpha)],
          [0, np.sin(alpha), np.cos(alpha), pz * (1 - np.cos(alpha)) - py * np.sin(alpha)],
          [0, 0, 0, 1]]
    Ry = [[np.cos(beta), 0, np.sin(beta), px * (1 - np.cos(beta)) - pz * np.sin(beta)],
          [0, 1, 0, 0],
          [-np.sin(beta), 0, np.cos(beta), pz * (1 - np.cos(beta)) + px * np.sin(beta)],
          [0, 0, 0, 1]]
    Rz = [[np.cos(gamma), -np.sin(gamma), 0, px * (1 - np.cos(gamma)) + py * np.sin(gamma)],
          [np.sin(gamma), np.cos(gamma), 0, py * (1 - np.cos(gamma)) - px * np.sin(gamma)],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

    Rx = np.array(Rx);
    Ry = np.array(Ry);
    Rz = np.array(Rz)
    P = np.array([x, y, z, [1] * x.size])

    return np.dot(np.dot(np.dot(Rx, Ry), Rz), P)

R_ = [[45.0, 0, 0],
      [0, 45.0, 0],
      [0, 0, 45.0],
      [0, 0, 0]]
P_ = [[0, 0, 0],
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

alpha, beta, gamma = R_[2]
print(P_[1])
px, py, pz = P_[1]

x_, y_, z_, _ = trans_rotate(x, y, z, px, py, pz, alpha, beta, gamma)

print(x_)
print(y_)
print(z_)
