import cv2
import numpy as np

# 读取需要处理的图像
img = cv2.imread("figure3.png")
# 高斯滤波
dst1 = cv2.GaussianBlur(img,(3,5),0)
# 颜色空间转换函数
dst2 = cv2.cvtColor(dst1, cv2.COLOR_BGR2HSV)
# 地层1 185 212 0 (0 212 185)地层2 220 221 221(221 221 220)
# 去除背景得到 范围内变成白色 所有地层20-100 地层2 20-50 地层1 滑动面0-100
dst3 = cv2.inRange(dst2, np.array([20, 0, 0]), np.array([200,255,255]))
contours, hierarchy = cv2.findContours(dst3,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
dst5 = cv2.drawContours(img,contours,-1,(0,0,255),2)

# 显示绘制结果
cv2.imshow("dst5",dst5)
cv2.imshow("layer2",dst3)
dst4 = cv2.bitwise_and(img, img, mask= dst3)
cv2.imshow("Ori",dst4)
# 按下任意键后触发后续功能
cv2.waitKey()
# 释放所有窗体
cv2.destroyAllWindows()