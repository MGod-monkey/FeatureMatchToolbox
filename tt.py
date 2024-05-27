# # import cv2
# # import numpy as np

# # def compute_disparity_map(img_left, img_right, num_disparities, block_size):
# #     # 转换为灰度图
# #     img_left_gray = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
# #     img_right_gray = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

# #     # 创建 SGBM 对象
# #     sgbm = cv2.StereoSGBM_create(
# #         minDisparity=0,
# #         numDisparities=num_disparities,
# #         blockSize=block_size,
# #         P1=8 * 3 * block_size * block_size,
# #         P2=32 * 3 * block_size * block_size,
# #         disp12MaxDiff=1,
# #         uniquenessRatio=15,
# #         speckleWindowSize=0,
# #         speckleRange=2,
# #         preFilterCap=63,
# #         mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
# #     )

# #     # 计算视差图
# #     disparity_map = sgbm.compute(img_left_gray, img_right_gray)
# #     return disparity_map

# # def main():
# #     # 读取左右摄像头图像
# #     img_left = cv2.imread(r'C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\left\globalImage_left.png')
# #     img_right = cv2.imread(r'C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\right\globalImage_right.png')

# #     # 计算视差图
# #     num_disparities = 16*6
# #     block_size = 11
# #     disparity_map = compute_disparity_map(img_left, img_right, num_disparities, block_size)

# #     # 归一化视差图以进行显示
# #     disparity_map_normalized = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# #     # 显示视差图
# #     cv2.imshow('Disparity Map', disparity_map_normalized)
# #     cv2.waitKey(0)
# #     cv2.destroyAllWindows()

# # if __name__ == "__main__":
# #     main()
# import sys
# import cv2
# import numpy as np
# from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
# from PySide6.QtCore import QTimer, Qt
# from PySide6.QtGui import QImage, QPixmap

# class StereoCameraDisplay(QLabel):
#     def __init__(self, parent=None):
#         super(StereoCameraDisplay, self).__init__(parent)
#         self.measuring_point = None
#         self.measure_distance = False
#         self.left_mouse_button_pressed = False

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.left_mouse_button_pressed = True

#     def mouseMoveEvent(self, event):
#         if self.left_mouse_button_pressed:
#             position = event.position()
#             self.measuring_point = (int(position.x()), int(position.y()))
#             self.measure_distance = True

#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.left_mouse_button_pressed = False
#             self.measure_distance = False
#             self.measuring_point = None
#             self.update()

# class StereoCameraApp(QMainWindow):
#     def __init__(self, calibration_params_file, left_camera_index=1, right_camera_index=2, parent=None):
#         super().__init__()

#         self.setWindowTitle('Stereo Camera Distance Measurement')
#         self.resize(800, 600)

#         self.layout = QVBoxLayout()

#         self.image_label = QLabel()
#         self.layout.addWidget(self.image_label)

#         central_widget = QWidget()
#         central_widget.setLayout(self.layout)
#         self.setCentralWidget(central_widget)

#         self.capture_left = cv2.VideoCapture(1)
#         self.capture_right = cv2.VideoCapture(2)
#         self.calibration_params = self.load_calibration_params(calibration_params_file)
#         self.map1_left = self.calibration_params['map1_left']
#         self.map2_left = self.calibration_params['map2_left']
#         self.map1_right = self.calibration_params['map1_right']
#         self.map2_right = self.calibration_params['map2_right']
#         self.measuring_point = None
        
#         # Create the StereoCameraDisplay widget and set it as the central widget
#         self.stereo_display = StereoCameraDisplay(self)
#         self.setCentralWidget(self.stereo_display)

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)

#     def load_calibration_params(self, calibration_params_file):
#         fs = cv2.FileStorage(calibration_params_file, cv2.FILE_STORAGE_READ)

#         f_left = fs.getNode("cameraMatrix1").mat()[0, 0]
#         f_right = fs.getNode("cameraMatrix2").mat()[0, 0]
#         f = (f_left + f_right) / 2
#         T = abs(fs.getNode("T").mat()[0, 0])

#         R1 = fs.getNode("R").mat()
#         T1 = fs.getNode("T").mat()
#         cameraMatrix1 = fs.getNode("cameraMatrix1").mat()
#         cameraMatrix2 = fs.getNode("cameraMatrix2").mat()
#         distCoeffs1 = fs.getNode("distCoeffs1").mat()
#         distCoeffs2 = fs.getNode("distCoeffs2").mat()

#         imageSize = (self.capture_left.get(cv2.CAP_PROP_FRAME_WIDTH), self.capture_left.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         imageSize = tuple(map(int, imageSize))
#         R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, imageSize, R1, T1)

#         map1_left, map2_left = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, R1, P1, imageSize, cv2.CV_16SC2)
#         map1_right, map2_right = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2, P2, imageSize, cv2.CV_16SC2)

#         return {"focal_length": f, "baseline": T, "Q": Q, "map1_left": map1_left, "map2_left": map2_left, "map1_right": map1_right, "map2_right": map2_right}

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             position = event.position()
#             self.measuring_point = (int(position.x()), int(position.y()))
#             self.measure_distance = True

#     def update_frame(self):
#         img_left, img_right = self.capture_images()
#         disparity_map = self.compute_disparity_map(img_left, img_right)

#         frame1_rectified = cv2.remap(img_left, self.map1_left, self.map2_left, cv2.INTER_LINEAR)
#         frame2_rectified = cv2.remap(img_right, self.map1_right, self.map2_right, cv2.INTER_LINEAR)

#         self.disparity_map = self.compute_disparity_map(frame1_rectified, frame2_rectified)

#         # Combine the two rectified frames into one single image (for visualization purposes)
#         vis = np.hstack((frame1_rectified, frame2_rectified))

#         if self.stereo_display.measure_distance and self.stereo_display.measuring_point is not None:
#             x, y = self.stereo_display.measuring_point
#             disparity = self.disparity_map[y, x]
#             if disparity > 0:
#                 distance = self.get_distance(disparity)
#                 cv2.circle(vis, (x, y), 5, (0, 255, 0), -1)
#                 cv2.putText(vis, f'Distance: {distance:.2f}m', (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

#         self.stereo_display.setPixmap(QPixmap.fromImage(self.convert_cv_to_qt_image(vis)))

#         # qimage = QImage(img_left.data, img_left.shape[1], img_left.shape[0], QImage.Format_BGR888)
#         # pixmap = QPixmap.fromImage(qimage)
#         # self.image_label.setPixmap(pixmap)

#     def capture_images(self):
#         ret_left, img_left = self.capture_left.read()
#         ret_right, img_right = self.capture_right.read()
#         return img_left, img_right
#     def convert_cv_to_qt_image(self, cv_img):
#         height, width, channel = cv_img.shape
#         bytes_per_line = 3 * width
#         qt_image = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
#         return qt_image

#     def compute_disparity_map(self, img_left, img_right):
#         num_disparities = 16 * 6
#         block_size = 11
#         min_disparity = 0

#         img_left_gray = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
#         img_right_gray = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

#         sgbm = cv2.StereoSGBM_create(
#             minDisparity=min_disparity,
#             numDisparities=num_disparities,
#             blockSize=block_size,
#             P1=8 * 3 * block_size * block_size,
#             P2=32 * 3 * block_size * block_size,
#             disp12MaxDiff=1,
#             uniquenessRatio=15,
#             speckleWindowSize=0,
#             speckleRange=2,
#             preFilterCap=63,
#             mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
#         )

#         disparity_map = sgbm.compute(img_left_gray, img_right_gray)
#         return disparity_map

#     def calculate_distance(self, disparity_map, point):
#         x, y = point
#         Q = self.calibration_params['Q']
#         f = self.calibration_params['focal_length']
#         T = self.calibration_params['baseline']
#         disparity = disparity_map[y, x]
#         if disparity <= 0:
#             return None

#         distance = (f * T) / disparity
#         return distance

#     def draw_measurement(self, img, point, distance):
#         x, y = point
#         if distance is None:
#             text = "Invalid"
#         else:
#             text = f"{distance:.2f} m"

#         cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#         cv2.putText(img, text, (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

#         return img


# app = QApplication(sys.argv)
# calibration_params_file = r'C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\calibration_params.yml'
# window = StereoCameraApp(calibration_params_file)
# window.show()

# sys.exit(app.exec())
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# import time
# import os
# camera_left = cv2.VideoCapture(1)
# if not camera_left.isOpened():
#     camera_right = camera_left = cv2.VideoCapture(0)
# else:   
#     camera_right = cv2.VideoCapture(2)
# def biaoding(qipan_x, qipan_y, min_img_num, size):
#     try:
#         # 棋盘规格，这里是 9x6 的黑白相间的棋盘
#         CHESSBOARD_SIZE = (qipan_x, qipan_y)
#         CHESSBOARD_SQUARE_SIZE = size  # 棋盘格子的尺寸（单位为cm）
#         MIN_COUNT_IMG = min_img_num  # 最少需要多少张图像进行标定

#         # 存储所有棋盘角点的像素坐标和对应的实际坐标
#         img_points_left = []   # 左侧相机的图像坐标
#         img_points_right = []  # 右侧相机的图像坐标
#         obj_points = []        # 实际坐标

#         # 定义棋盘角点的真实坐标
#         objp = np.zeros((CHESSBOARD_SIZE[0] * CHESSBOARD_SIZE[1], 3), np.float32)
#         objp[:, :2] = np.mgrid[0:CHESSBOARD_SIZE[0], 0:CHESSBOARD_SIZE[1]].T.reshape(-1, 2)
#         objp *= CHESSBOARD_SQUARE_SIZE

#         # # 创建双目摄像头对象
#         # cap_left = cv2.VideoCapture(1, cv2.CAP_DSHOW)
#         # cap_right = cv2.VideoCapture(2, cv2.CAP_DSHOW)

#         # # 设置摄像头分辨率
#         # cap_left.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         # cap_left.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#         # cap_right.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         # cap_right.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#         # 定义摄像头参数
#         criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#         flags = (cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_FAST_CHECK)

#         # 创建窗口
#         cv2.namedWindow("Calibration", cv2.WINDOW_NORMAL)
#         cv2.resizeWindow("Calibration", 1280, 480)

#         # 检查摄像头是否正常工作
#         if not camera_left.isOpened() or not camera_right.isOpened():
#             return

#         # 开始循环捕获图像
#         while True:
#             # 读取左右两个相机的图像
#             ret_left, frame_left = camera_left.read()
#             ret_right, frame_right = camera_right.read()

#             # 调整左右摄像头的图像尺寸，使它们相同
#             frame_left = cv2.resize(frame_left, (640, 480))
#             frame_right = cv2.resize(frame_right, (640, 480))

#             # 将左右两个相机的图像合并到同一张图上
#             img = np.hstack((frame_left, frame_right))

#             # 将彩色图像转换为灰度图像
#             gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
#             gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)

#             # 在左右两个相机的图像中检测角点
#             ret_left, corners_left = cv2.findChessboardCorners(gray_left, CHESSBOARD_SIZE, None, flags=flags)
#             ret_right, corners_right = cv2.findChessboardCorners(gray_right, CHESSBOARD_SIZE, None, flags=flags)
#             # 如果左右两个相机都检测到了棋盘角点，则保存图像坐标和实际坐标
#             if ret_left == True and ret_right == True:
#                 # 在左右两个相机的图像中精确检测角点位置
#                 corners_left = cv2.cornerSubPix(gray_left, corners_left, (11, 11), (-1, -1), criteria)
#                 corners_right = cv2.cornerSubPix(gray_right, corners_right, (11, 11), (-1, -1), criteria)

#                 img_points_left.append(corners_left)
#                 img_points_right.append(corners_right)
#                 obj_points.append(objp)

#                 # 在图像中绘制检测到的角点
#                 cv2.drawChessboardCorners(frame_left, CHESSBOARD_SIZE, corners_left, ret_left)
#                 cv2.drawChessboardCorners(frame_right, CHESSBOARD_SIZE, corners_right, ret_right)

#                 # 将两个相机的图像合并到同一张图上，并显示当前标定进度
#                 img = np.hstack((frame_left, frame_right))
#                 cv2.putText(img, f"Image count: {len(img_points_left)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#                 cv2.putText(img, "Press Esc/Q to Exit", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                
#                 # 降低频率
#                 time.sleep(0.5)
#             else:
#                 # 如果只有一个相机检测到了角点，则在另一个相机的图像中绘制角点
#                 if ret_left == True:
#                     cv2.drawChessboardCorners(frame_right, CHESSBOARD_SIZE, corners_left, False)
#                 if ret_right == True:
#                     cv2.drawChessboardCorners(frame_left, CHESSBOARD_SIZE, corners_right, False)

#                 # 将两个相机的图像合并到同一张图上，并显示当前标定进度
#                 img = np.hstack((frame_left, frame_right))
#                 cv2.putText(img, f"Image count: {len(img_points_left)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#                 cv2.putText(img, "Press Esc/Q to Exit", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#             # 显示合并后的图像
#             cv2.imshow("Calibration", img)
#             # if Settings.ShowResultImageExtreWin:
#                 # cv2.imshow("Calibration", img)
#             # else:
#             #     img = QImage(img, img.shape[1], img.shape[0], QImage.Format.Format_RGB888)
#             #     # 将QImage对象设置到QLabel中
#             #     ui.cameraLabel.setPixmap(QPixmap.fromImage(img.rgbSwapped()))

#             # 如果收集到了足够多的图像，则进行标定并保存结果
#             if len(img_points_left) > MIN_COUNT_IMG:
#                 cv2.destroyAllWindows()
#                 camera_left.release()
#                 camera_right.release()
#                 print("收集到足够多的照片，开始标定...")
#                 # 标定相机
#                 ret_left, mtx_left, dist_left, rvecs_left, tvecs_left = cv2.calibrateCamera(obj_points, img_points_left, gray_left.shape[::-1], None, None)
#                 ret_right, mtx_right, dist_right, rvecs_right, tvecs_right = cv2.calibrateCamera(obj_points, img_points_right, gray_right.shape[::-1], None, None)

#                 # 双目标定
#                 flags = cv2.CALIB_FIX_INTRINSIC
#                 criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-5)
#                 ret, _, _, _, _, R, T, E, F = cv2.stereoCalibrate(obj_points, img_points_left, img_points_right, mtx_left, dist_left, mtx_right, dist_right, gray_left.shape[::-1], flags=flags, criteria=criteria)

#                 # 计算投影误差
#                 mean_error_left = 0
#                 mean_error_right = 0
#                 # 计算左侧相机的投影误差
#                 for i in range(len(obj_points)):
#                     img_points2_left, _ = cv2.projectPoints(obj_points[i], rvecs_left[i], tvecs_left[i], mtx_left, dist_left)
#                     error_left = cv2.norm(img_points_left[i], img_points2_left, cv2.NORM_L2) / len(img_points2_left)
#                     mean_error_left += error_left

#                 # 计算右侧相机的投影误差
#                 for i in range(len(obj_points)):
#                     img_points2_right, _ = cv2.projectPoints(obj_points[i], rvecs_right[i], tvecs_right[i], mtx_right, dist_right)
#                     error_right = cv2.norm(img_points_right[i], img_points2_right, cv2.NORM_L2) / len(img_points2_right)
#                     mean_error_right += error_right
#                 # 输出标定结果
#                 print("标定完成！")
#                 print("左侧相机投影误差: ", mean_error_left / len(obj_points))
#                 print("右侧相机投影误差: ", mean_error_right / len(obj_points))
#                 print("左侧相机内参矩阵: ", mtx_left)
#                 print("左侧相机畸变系数: ", dist_left)
#                 print("右侧相机内参矩阵: ", mtx_right)
#                 print("右侧相机畸变系数: ", dist_right)
#                 print("左右相机的旋转矩阵: ", R)
#                 print("左右相机的平移矩阵: ", T)

#                 # 保存标定结果到文件
#                 file_path = os.path.join("D:/", "calibration_params.yml")
#                 print(file_path)
#                 with cv2.FileStorage(file_path, cv2.FILE_STORAGE_WRITE) as fs:
#                     fs.write("dist_coeffs_left", dist_left)
#                     fs.write("camera_matrix_right", mtx_right)
#                     fs.write("dist_coeffs_right", dist_right)
#                     fs.write("R", R)
#                     fs.write("T", T)

#                 # 显示标定结果
#                 plt.imshow(cv2.cvtColor(frame_left, cv2.COLOR_BGR2RGB))
#                 plt.title("Calibration Result")
#                 plt.show()
#                 break

#             # 按下 ESC 或 Q键退出程序
#             key = cv2.waitKey(1)
#             if key == 27 or key == ord('q'):
#                 cv2.destroyAllWindows()
#                 break

#     except Exception as e:
#         print(e)
#         cv2.destroyAllWindows()
#         camera_left.release()
#         camera_right.release()
        
# biaoding(9, 6, 50, 23.3)
from modules.SuperGluePretrainedNetwork.SuperGlueApi import *

videoMatch()