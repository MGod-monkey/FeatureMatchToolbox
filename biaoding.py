# import cv2
# import numpy as np
# import glob

# def main():
#     # 棋盘格参数
#     pattern_size = (9, 6)  # 棋盘格中内角点的数量，例如 (9, 6) 表示 9x6 的棋盘格
#     square_size = 2.5  # 棋盘格中每个方格的实际大小，以厘米为单位

#     # 准备棋盘格角点在世界坐标系中的坐标
#     pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
#     pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
#     pattern_points *= square_size

#     obj_points = []  # 世界坐标系中的角点坐标
#     img_points = []  # 图像坐标系中的角点坐标

#     images = glob.glob('calibration_images/*.jpg')  # 标定图片路径
#     for img_path in images:
#         img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
#         if img is None:
#             print("Failed to read image:", img_path)
#             continue

#         found, corners = cv2.findChessboardCorners(img, pattern_size)
#         if found:
#             term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
#             cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)

#             img_points.append(corners)
#             obj_points.append(pattern_points)
#         else:
#             print("Failed to find chessboard corners in:", img_path)

#     if len(img_points) < 2:
#         print("Not enough images for calibration")
#         return

#     img_size = img.shape[::-1]
#     ret, K, D, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, img_size, None, None)

#     # 保存校准参数
#     fs = cv2.FileStorage("calibration_params.yml", cv2.FILE_STORAGE_WRITE)
#     fs.write("K", K)
#     fs.write("D", D)
#     fs.release()

#     print("Calibration successful")
#     print("Camera matrix K:", K)
#     print("Distortion coefficients D:", D)

# if __name__ == '__main__':
#     main()
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 棋盘规格，这里是 10x7 的黑白相间的棋盘
CHESSBOARD_SIZE = (5, 4)
CHESSBOARD_SQUARE_SIZE = 23.2  # 棋盘格子的尺寸（单位为cm）
MIN_COUNT_IMG = 50  # 最少需要多少张图像进行标定


# 存储所有棋盘角点的像素坐标和对应的实际坐标
img_points_left = []   # 左侧相机的图像坐标
img_points_right = []  # 右侧相机的图像坐标
obj_points = []        # 实际坐标

# 定义棋盘角点的真实坐标
objp = np.zeros((CHESSBOARD_SIZE[0] * CHESSBOARD_SIZE[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHESSBOARD_SIZE[0], 0:CHESSBOARD_SIZE[1]].T.reshape(-1, 2)
objp *= CHESSBOARD_SQUARE_SIZE

# 创建双目摄像头对象
cap_left = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap_right = cv2.VideoCapture(2, cv2.CAP_DSHOW)

# 设置摄像头分辨率
cap_left.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap_left.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap_right.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap_right.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# 定义摄像头参数
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
flags = (cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_FAST_CHECK)

# 创建窗口
cv2.namedWindow("Calibration", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Calibration", 1280, 480)

# 开始循环捕获图像
while True:
    # 读取左右两个相机的图像
    ret_left, frame_left = cap_left.read()
    ret_right, frame_right = cap_right.read()

    # # 调整左右摄像头的图像尺寸，使它们相同
    # frame_left = cv2.resize(frame_left, (640, 480))
    # frame_right = cv2.resize(frame_right, (640, 480))

    # 将左右两个相机的图像合并到同一张图上
    img = np.hstack((frame_left, frame_right))

    # 将彩色图像转换为灰度图像
    gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)

    # 在左右两个相机的图像中检测角点
    ret_left, corners_left = cv2.findChessboardCorners(gray_left, CHESSBOARD_SIZE, None, flags=flags)
    ret_right, corners_right = cv2.findChessboardCorners(gray_right, CHESSBOARD_SIZE, None, flags=flags)
    # 如果左右两个相机都检测到了棋盘角点，则保存图像坐标和实际坐标
    if ret_left == True and ret_right == True:
        # 在左右两个相机的图像中精确检测角点位置
        corners_left = cv2.cornerSubPix(gray_left, corners_left, (11, 11), (-1, -1), criteria)
        corners_right = cv2.cornerSubPix(gray_right, corners_right, (11, 11), (-1, -1), criteria)

        img_points_left.append(corners_left)
        img_points_right.append(corners_right)
        obj_points.append(objp)

        # 在图像中绘制检测到的角点
        cv2.drawChessboardCorners(frame_left, CHESSBOARD_SIZE, corners_left, ret_left)
        cv2.drawChessboardCorners(frame_right, CHESSBOARD_SIZE, corners_right, ret_right)

        # 将两个相机的图像合并到同一张图上，并显示当前标定进度
        img = np.hstack((frame_left, frame_right))
        cv2.putText(img, f"Image count: {len(img_points_left)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        # 如果只有一个相机检测到了角点，则在另一个相机的图像中绘制角点
        if ret_left == True:
            cv2.drawChessboardCorners(frame_right, CHESSBOARD_SIZE, corners_left, False)
        if ret_right == True:
            cv2.drawChessboardCorners(frame_left, CHESSBOARD_SIZE, corners_right, False)

        # 将两个相机的图像合并到同一张图上，并显示当前标定进度
        img = np.hstack((frame_left, frame_right))
        cv2.putText(img, f"Image count: {len(img_points_left)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # 显示合并后的图像
    cv2.imshow("Calibration", img)

    # 如果收集到了足够多的图像，则进行标定并保存结果
    if len(img_points_left) > MIN_COUNT_IMG:
        # 标定相机
        ret_left, mtx_left, dist_left, rvecs_left, tvecs_left = cv2.calibrateCamera(obj_points, img_points_left, gray_left.shape[::-1], None, None)
        ret_right, mtx_right, dist_right, rvecs_right, tvecs_right = cv2.calibrateCamera(obj_points, img_points_right, gray_right.shape[::-1], None, None)

        # 双目标定
        flags = cv2.CALIB_FIX_INTRINSIC
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-5)
        ret, _, _, _, _, R, T, E, F = cv2.stereoCalibrate(obj_points, img_points_left, img_points_right, mtx_left, dist_left, mtx_right, dist_right, gray_left.shape[::-1], flags=flags, criteria=criteria)

        # 计算投影误差
        mean_error_left = 0
        mean_error_right = 0
        # 计算左侧相机的投影误差
        for i in range(len(obj_points)):
            img_points2_left, _ = cv2.projectPoints(obj_points[i], rvecs_left[i], tvecs_left[i], mtx_left, dist_left)
            error_left = cv2.norm(img_points_left[i], img_points2_left, cv2.NORM_L2) / len(img_points2_left)
            mean_error_left += error_left

        # 计算右侧相机的投影误差
        for i in range(len(obj_points)):
            img_points2_right, _ = cv2.projectPoints(obj_points[i], rvecs_right[i], tvecs_right[i], mtx_right, dist_right)
            error_right = cv2.norm(img_points_right[i], img_points2_right, cv2.NORM_L2) / len(img_points2_right)
            mean_error_right += error_right

        # 输出标定结果
        print("标定完成！")
        print("左侧相机投影误差: ", mean_error_left / len(obj_points))
        print("右侧相机投影误差: ", mean_error_right / len(obj_points))
        print("左侧相机内参矩阵: ", mtx_left)
        print("左侧相机畸变系数: ", dist_left)
        print("右侧相机内参矩阵: ", mtx_right)
        print("右侧相机畸变系数: ", dist_right)
        print("左右相机的旋转矩阵: ", R)
        print("左右相机的平移矩阵: ", T)

        # 保存标定结果到文件
        fs = cv2.FileStorage("calibration_params_auto.yml", cv2.FILE_STORAGE_WRITE)
        fs.write("camera_matrix_left", mtx_left)
        fs.write("dist_coeffs_left", dist_left)
        fs.write("camera_matrix_right", mtx_right)
        fs.write("dist_coeffs_right", dist_right)
        fs.write("R", R)
        fs.write("T", T)
        fs.release()

        # 显示标定结果
        plt.imshow(cv2.cvtColor(frame_left, cv2.COLOR_BGR2RGB))
        plt.title("Calibration Result")
        plt.show()

        break

    # 按下 ESC 键退出程序
    if cv2.waitKey(1) == 27:
        break

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import glob

# # 标定板参数
# board_size = (5, 4)  # 棋盘格尺寸
# square_size = 232  # 棋盘格方格边长，单位：毫米

# # 准备3D坐标
# object_points = np.zeros((board_size[0] * board_size[1], 3), np.float32)
# object_points[:, :2] = np.mgrid[0:board_size[0], 0:board_size[1]].T.reshape(-1, 2) * square_size

# # 读取左右摄像头图片
# left_images = glob.glob('left/*.jpg')
# right_images = glob.glob('right/*.jpg')

# assert len(left_images) == len(right_images), "左右摄像头图片数量不匹配"

# image_points_left = []
# image_points_right = []
# object_points_list = []

# for left_img_path, right_img_path in zip(left_images, right_images):
#     img_left = cv2.imread(left_img_path)
#     img_right = cv2.imread(right_img_path)

#     gray_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
#     gray_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

#     ret_left, corners_left = cv2.findChessboardCorners(gray_left, board_size)
#     ret_right, corners_right = cv2.findChessboardCorners(gray_right, board_size)

#     if ret_left and ret_right:
#         image_points_left.append(corners_left)
#         image_points_right.append(corners_right)
#         object_points_list.append(object_points)

# # 单目标定
# ret_left, mtx_left, dist_left, rvecs_left, tvecs_left = cv2.calibrateCamera(object_points_list, image_points_left, gray_left.shape[::-1], None, None)
# ret_right, mtx_right, dist_right, rvecs_right, tvecs_right = cv2.calibrateCamera(object_points_list, image_points_right, gray_right.shape[::-1], None, None)

# # 双目标定
# retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(object_points_list, image_points_left, image_points_right, mtx_left, dist_left, mtx_right, dist_right, gray_left.shape[::-1])

# # 保存标定参数
# calibration_params = {
#     'cameraMatrix1': cameraMatrix1.tolist(),
#     'distCoeffs1': distCoeffs1.tolist(),
#     'cameraMatrix2': cameraMatrix2.tolist(),
#     'distCoeffs2': distCoeffs2.tolist(),
#     'R': R.tolist(),
#     'T': T.tolist(),
#     'E': E.tolist(),
#     'F': F.tolist()
# }

# with open('calibration_params.yml', 'w') as f:
#     import yaml
#     yaml.dump(calibration_params, f)

# import os
# import cv2

# # 指定摄像头索引
# left_cam_index = 2
# right_cam_index = 1

# # 指定保存路径
# left_save_path = 'left'
# right_save_path = 'right'

# # 创建保存文件夹
# if not os.path.exists(left_save_path):
#     os.makedirs(left_save_path)

# if not os.path.exists(right_save_path):
#     os.makedirs(right_save_path)

# # 打开摄像头
# left_cam = cv2.VideoCapture(left_cam_index)
# right_cam = cv2.VideoCapture(right_cam_index)

# # 设置摄像头分辨率
# left_cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# left_cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# right_cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# right_cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# counter = 0

# while True:
#     ret_left, frame_left = left_cam.read()
#     ret_right, frame_right = right_cam.read()

#     cv2.imshow('Left Camera', frame_left)
#     cv2.imshow('Right Camera', frame_right)

#     key = cv2.waitKey(1) & 0xFF

#     if key == ord('s'):
#         left_filename = os.path.join(left_save_path, f'left_{counter:03d}.jpg')
#         right_filename = os.path.join(right_save_path, f'right_{counter:03d}.jpg')
#         cv2.imwrite(left_filename, frame_left)
#         cv2.imwrite(right_filename, frame_right)
#         print(f'Saved image pair {counter}')
#         counter += 1
#     elif key == ord('q'):
#         break

# # 释放资源
# left_cam.release()
# right_cam.release()
# cv2.destroyAllWindows()