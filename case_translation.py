import numpy as np

x = np.array([1,1,1,1])
y = np.array([1,2.414,2.414,1])
z = np.array([1,1,2,2])


def trans_translate(x, y, z, tx, ty, tz):
    T = [[1, 0, 0, tx],
         [0, 1, 0, ty],
         [0, 0, 1, tz],
         [0, 0, 0, 1]]
    T = np.array(T)
    P = np.array([x, y, z, [1] * x.size])
    return np.dot(T, P)

T_ = [[-1, -1, -1],
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

tx, ty, tz = T_[0]
x_, y_, z_, _ = trans_translate(x, y, z, tx, ty, tz)

print(x_)
print(y_)
print(z_)
