from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QSizePolicy, QMessageBox
from PySide6.QtGui import QIcon, QAction, QImage, QPixmap, QMouseEvent
from PySide6.QtCore import Qt, QTimer, Signal, Slot, QThread
from threading import Lock
import queue
from main import *
import socket
import cv2
import re
from . ui_functions import *
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
# import torch
import yaml
from imutils.video import VideoStream
import time
from . SuperGluePretrainedNetwork.models.utils import AverageTimer, VideoStreamer
from . SuperGluePretrainedNetwork.SuperGlueApi import *
# from models.matching import Matching
# from models.utils import (AverageTimer, VideoStreamer,
#                           make_matching_plot_fast, frame2tensor)

# 计时器模块

img_result = None
webcameraIP = ''
horizontal_angle = vertical_angle = distance = 0
matchPointRate = [1, 1, 1, 1, 1]
mathTimeCost = [999, 999, 999, 999, 999]
HError = [100, 100, 100, 100, 100]
VError = [1000, 100, 100, 100, 100]
DError = [100, 100, 100, 100, 100]

class FrameUpdateThread(QThread):
    frame_ready = Signal(QImage)
    camera_closed = Signal()
    
    def __init__(self, camera=None, parent=None):
        super(FrameUpdateThread, self).__init__(parent)
        self.parent = parent
        self.camera = camera
        self.running = False
        self.paused = False
        self.camera_lock = Lock()
        self.buffer = queue.Queue(maxsize=5)  # 创建一个最大容量为5的队列作为缓冲区
    
    def setCamera(self, camera):
        self.camera = camera
        
    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False

    def run(self):
        self.running = True
        while self.running:
            if not self.paused:
                if self.parent.Settings.ShowDoubleImage == 'True' or self.parent.Settings.ShowDoubleImage == True:
                    with self.camera_lock:
                        if not self.running:
                            break
                        if self.parent.camera_left.isOpened() and self.parent.camera_right.isOpened():
                            ret_left, self.frame_left = self.parent.camera_left.read()
                            ret_right, self.frame_right = self.parent.camera_right.read()
                            if ret_left and ret_right:
                                combined_frame = np.hstack((self.frame_left, self.frame_right))
                                self.frame = combined_frame

                                if self.buffer.full():
                                    self.buffer.get()
                                self.buffer.put(self.frame)

                                image = QImage(self.frame, self.frame.shape[1], self.frame.shape[0], QImage.Format.Format_RGB888)
                                self.frame_ready.emit(image.rgbSwapped())
                        else:
                            self.parent.openCamera = False
                            self.parent.webCameraConnect = False
                            self.parent.timer_autoConnect.start(5 * 1000)
                            break
                else:
                    with self.camera_lock:
                        if not self.running:
                            break
                        if self.camera.isOpened():
                            ret, self.frame = self.camera.read()
                            if ret:
                                if self.buffer.full():
                                    self.buffer.get()
                                self.buffer.put(self.frame)

                                image = QImage(self.frame, self.frame.shape[1], self.frame.shape[0], QImage.Format.Format_RGB888)
                                self.frame_ready.emit(image.rgbSwapped())
                        else:
                            self.parent.openCamera = False
                            self.parent.webCameraConnect = False
                            self.parent.timer_autoConnect.start(5 * 1000)
                            break
            else:
                self.msleep(100)
        self.camera_closed.emit()
    def status(self):
        return self.running

    def stop(self):
        self.paused = True
        self.running = False
        with self.camera_lock:
            try:
                self.parent.camera_left.release()
                self.parent.camera_right.release()
            except Exception as e:
                print(e)

class Camera(MainWindow):
    # def __init__(self, camera_label, parent=None):
    #     super().__init__(parent)
    #     self.ui.cameraLabel = camera_label
    #     self.init_camera()
    
    def init_camera(self):
        global webcameraIP
        self.webCameraConnect = False
        self.openCamera = False

        if self.Settings.WebCameraIP != '':
            webcameraIP = self.Settings.WebCameraIP
        
        # 绑定图像处理按键
        self.ui.addGloadImageBtn.clicked.connect(lambda: UIFunctions.showFileDialog(self, 0))
        self.ui.addLocalImageBtn.clicked.connect(lambda: UIFunctions.showFileDialog(self, 1))

        # 自动连接
        def autoConnect(self):
            if self.Settings.WebCameraIP != '':
                Camera.setIP(self, self.Settings.WebCameraIP)
        self.timer_autoConnect = QTimer(self)
        self.timer_autoConnect.timeout.connect(lambda: autoConnect(self))
        self.timer_autoConnect.start(5*1000)

        return Camera
    
    # 打开/关闭摄像头
    def openClosecamera(self, openTimer=True):
        if self.openCamera == False:      
            try:
                if not self.webCameraConnect:
                    self.camera_left = cv2.VideoCapture(1)
                    if not self.camera_left.isOpened():
                        self.camera_right = self.camera_left = cv2.VideoCapture(0)
                    else:   
                        self.camera_right = cv2.VideoCapture(2)
                else:
                    self.camera_left = cv2.VideoCapture(f'http://{self.Settings.WebCameraIP}:8080/video_feed/0')
                    self.camera_right = cv2.VideoCapture(f'http://{self.Settings.WebCameraIP}:8080/video_feed/2')
                self.camera = self.camera_left
            except Exception as e:
                UIFunctions.showMessageBox(self, 'ERROR', f'{e}', 1)
                return

            if openTimer:
                # 摄像头刷新
                self.frame_update_thread = FrameUpdateThread(camera=self.camera, parent=self)
                self.frame_update_thread.frame_ready.connect(self.update_frame)
                self.frame_update_thread.camera_closed.connect(self.camera_closed_slot)
                self.frame_update_thread.start()
        else:
            if hasattr(self, "frame_update_thread") and self.frame_update_thread.status():
                self.frame_update_thread.stop()
                self.frame_update_thread.wait()
                self.ui.cameraLabel.setText('请打开摄像头')
            if self.camera_left.isOpened() and self.camera_right.isOpened():
                try:
                    self.camera_left.release()
                    self.camera_right.release()
                except Exception as e:
                    print(e)
        self.openCamera = not self.openCamera
        
    # 切换摄像头
    def changeCamera(self):
        if self.openCamera == False:
            pass
        if self.camera_right == self.camera_left:
            return
        if self.camera != self.camera_right:
            self.camera = self.camera_right
        else:
            self.camera = self.camera_left
        self.frame_update_thread.setCamera(self.camera)
    
    # 改变分辨率
    def changeResolution(self, index):
        if index == 0:
            cameraWidth = 640
            cameraHeight = 480
            self.Settings.WebCameraResolution = '640x480'
        elif index == 1:
            cameraWidth = 800
            cameraHeight = 600
            self.Settings.WebCameraResolution = '800x600'
        elif index == 2:
            cameraWidth = 1280
            cameraHeight = 720
            self.Settings.WebCameraResolution = '1280x720'
        elif index == 3:
            cameraWidth = 1920
            cameraHeight = 1080
            self.Settings.WebCameraResolution = '1920x1080'
        self.camera_left.set(cv2.CAP_PROP_FRAME_WIDTH, cameraWidth)
        self.camera_left.set(cv2.CAP_PROP_FRAME_HEIGHT, cameraHeight)
        self.camera_right.set(cv2.CAP_PROP_FRAME_WIDTH, cameraWidth)
        self.camera_right.set(cv2.CAP_PROP_FRAME_HEIGHT, cameraHeight)
        UIFunctions.toggleCameraLabel(self, cameraWidth, cameraHeight)
    
    # 保存照片
    def shutter(self):
        if self.openCamera == False:
            UIFunctions.showMessageBox(self, '摄像头未打开!', 0)
            return
        elif not self.camera_left.isOpened() or not self.camera_right.isOpened():
            UIFunctions.showMessageBox(self, '摄像头未能正常运行，请检查摄像头后重试!', 1)
        else:
            saveImgIndex = int(self.Settings.ImageSaveCameraIndex)
            # 保存当前相机图像
            if saveImgIndex == 0 or saveImgIndex == 3 or saveImgIndex == 4:
                imgSavePath = UIFunctions.getResultFilePath(self, self.Settings.ImageSavePath)
            # 保存左相机图像
            elif saveImgIndex == 1:
                imgSavePath = UIFunctions.getResultFilePath(self, self.Settings.ImageSavePath) + r'\left'
            # 保存右相机图像
            elif saveImgIndex == 2:
                imgSavePath = UIFunctions.getResultFilePath(self, self.Settings.ImageSavePath) + r'\right'

            # 判断images目录是否存在，不存在则创建
            print('图像保存路径：', imgSavePath)
            if not os.path.exists(imgSavePath):
                os.makedirs(imgSavePath)
            # ret, frame = self.camera.read()
            self.frame_update_thread.pause()
            globalBtn = QPushButton("全局图片")
            localBtn = QPushButton("局部图片")
            def saveToGloal():
                try:
                    if self.Settings.ImageCover == 'True' or self.Settings.ImageCover == True:
                        if saveImgIndex == 1:
                            cv2.imwrite(f'{imgSavePath}/globalImage_left.png', self.frame_update_thread.frame_left)
                        elif saveImgIndex == 2:
                            cv2.imwrite(f'{imgSavePath}/globalImage_right.png', self.frame_update_thread.frame_right)
                        elif saveImgIndex == 3:
                            cv2.imwrite(f'{imgSavePath}/left/globalImage_left.png', self.frame_update_thread.frame_left)
                            cv2.imwrite(f'{imgSavePath}/right/globalImage_right.png', self.frame_update_thread.frame_right)
                        else:                            
                            cv2.imwrite(f'{imgSavePath}/globalImage.png', self.frame_update_thread.frame)
                    else:
                        # 保存图片名为当前时间戳后4位
                        if saveImgIndex == 1:
                            cv2.imwrite(f'{imgSavePath}/globalImage_left_{int(time.time()) % 10000}.png', self.frame_update_thread.frame_left)
                        elif saveImgIndex == 2:
                            cv2.imwrite(f'{imgSavePath}/globalImage_right_{int(time.time()) % 10000}.png', self.frame_update_thread.frame_right)
                        elif saveImgIndex == 3:
                            cv2.imwrite(f'{imgSavePath}/left/globalImage_left_{int(time.time()) % 10000}.png', self.frame_update_thread.frame_left)
                            cv2.imwrite(f'{imgSavePath}/right/globalImage_right_{int(time.time()) % 10000}.png', self.frame_update_thread.frame_right)
                        else:                            
                            cv2.imwrite(f'{imgSavePath}/globalImage_{int(time.time()) % 10000}.png', self.frame_update_thread.frame)
                    self.Settings.ImageSaveSuccess = True
                except Exception as e:
                    print(e)
                    self.Settings.ImageSaveSuccess = False
            def saveToLocal():
                try:
                    if self.Settings.ImageCover == 'True' or self.Settings.ImageCover == True:
                        if saveImgIndex == 1:
                            cv2.imwrite(f'{imgSavePath}/localImage_left.png', self.frame_update_thread.frame_left)
                        elif saveImgIndex == 2:
                            cv2.imwrite(f'{imgSavePath}/localImage_right.png', self.frame_update_thread.frame_right)
                        elif saveImgIndex == 3:
                            cv2.imwrite(f'{imgSavePath}/left/localImage_left.png', self.frame_update_thread.frame_left)
                            cv2.imwrite(f'{imgSavePath}/right/localImage_right.png', self.frame_update_thread.frame_right)
                        else:                            
                            cv2.imwrite(f'{imgSavePath}/localImage.png', self.frame_update_thread.frame)
                    else:
                        # 保存图片名为当前时间戳后4位
                        if saveImgIndex == 1:
                            cv2.imwrite(f'{imgSavePath}/localImage_left_{int(time.time()) % 10000}.png', self.frame_update_thread.frame_left)
                        elif saveImgIndex == 2:
                            cv2.imwrite(f'{imgSavePath}/localImage_right_{int(time.time()) % 10000}.png', self.frame_update_thread.frame_right)
                        elif saveImgIndex == 3:
                            cv2.imwrite(f'{imgSavePath}/left/localImage_left_{int(time.time()) % 10000}.png', self.frame_update_thread.frame_left)
                            cv2.imwrite(f'{imgSavePath}/right/localImage_right_{int(time.time()) % 10000}.png', self.frame_update_thread.frame_right)
                        else:                            
                            cv2.imwrite(f'{imgSavePath}/localImage_{int(time.time()) % 10000}.png', self.frame_update_thread.frame)
                    self.Settings.ImageSaveSuccess = True
                except Exception as e:
                    print(e)
                    self.Settings.ImageSaveSuccess = False
            
            globalBtn.clicked.connect(saveToGloal)
            localBtn.clicked.connect(saveToLocal)
            UIFunctions.showMessageBox(self, '保存图像为', 3, globalBtn, localBtn)
            self.frame_update_thread.resume()
    
    def checkIPStatus(self, ip_address):
        # 创建socket对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间为3秒
        sock.settimeout(3)
        try:
            # 尝试连接
            sock.connect((ip_address, 8080))
            # 如果连接成功，则立即关闭 socket 连接并返回 True
            sock.close()
            return True
        except:
            # 如果连接失败，则关闭 socket 连接并返回 False
            sock.close()
            return False

    # 设置IP
    def setIP(self, ip_address, is_init=False):
        global webcameraIP
        # ip, port = ip_address.split(":")
        pattern = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        # IP地址的正则表达式
        if re.match(pattern, ip_address):
            if Camera.checkIPStatus(self, ip_address):
                if self.openCamera:
                    self.camera_left.release()
                    self.camera_right.release()
                if not self.webCameraConnect:
                    UIFunctions.showMessageBox(self, '网络摄像头已自动连接！', 2)
                if self.Settings.WebCameraIP != webcameraIP:
                    UIFunctions.showMessageBox(self, '设置成功！', 2)
                    webcameraIP = self.Settings.WebCameraIP
                self.webCameraConnect = True
                self.timer_autoConnect.stop()
                # self.timer_autoConnect.start(20*1000)   #连接成功后自动连接的频率降低
                self.Settings.setConfig('WEBCAMERA', 'WebCameraIP', ip_address)
                self.ui.statusLabel.setText('WebCameraIP: ' + ip_address)
            else:
                UIFunctions.showMessageBox(self, '网络摄像头无法连接，请检查IP地址是否正确！', 1)
                self.Settings.setConfig('WEBCAMERA', 'WebCameraIP', '')
                self.webCameraConnect = False
        else:
            UIFunctions.showMessageBox(self, 'IP地址不正确，请检查！', 0)
    

    # 水平距离计算
    # # 获取深度图
    # def compute_depth_map(disp, K1, T):
    #     baseline = np.linalg.norm(T)
    #     focal_length = K1[0, 0]

    #     depth_map = (baseline * focal_length) / (disp + 1e-6)
    #     return depth_map
    # # 将图像转到世界坐标系
    # def img_to_world_coords(x, y, depth, K):
    #     fx, fy = K[0, 0], K[1, 1]
    #     cx, cy = K[0, 2], K[1, 2]

    #     Z = depth[y, x]
    #     X = (x - cx) * Z / fx
    #     Y = (y - cy) * Z / fy

    #     return np.array([X, Y, Z])
    # ##################################################
    # #               4. 水平距离计算                  ##
    # ##################################################
    # def calcHorizontalDistance(self, global_img_path=None, local_img_path=None):
    #     # 加载校准参数
    #     fs = cv2.FileStorage(UIFunctions.getResultFilePath(self, self.Settings.WebCameraCalibrationParametersPath), cv2.FILE_STORAGE_READ)
    #     K1 = fs.getNode("K1").mat()
    #     K2 = fs.getNode("K2").mat()
    #     D1 = fs.getNode("D1").mat()
    #     D2 = fs.getNode("D2").mat()
    #     R = fs.getNode("R").mat()
    #     T = fs.getNode("T").mat()
    #     fs.release()

    #     global img_result
    #     # 读取原图像和局部图像
    #     if global_img_path is not None and local_img_path is not None:
    #         img_global = cv2.imread(self.Settings.ImageChooseGloadPath)
    #         img_local = cv2.imread(self.Settings.ImageChooseLocalPath)
    #     elif self.Settings.ImageChooseGloadPath != '' and self.Settings.ImageChooseLocalPath != '':
    #         # img_global_gray = cv2.imread(self.Settings.ImageChooseGloadPath, cv2.IMREAD_GRAYSCALE)
    #         # img_local_gray = cv2.imread(self.Settings.ImageChooseLocalPath, cv2.IMREAD_GRAYSCALE)
    #         img_global = cv2.imread(self.Settings.ImageChooseGloadPath)
    #         img_local = cv2.imread(self.Settings.ImageChooseLocalPath)
    #     else:
    #         UIFunctions.showMessageBox(self, '请先选择图片！', 1)
    #         return False
    #     # 特征匹配            
    #     kp_local, kp_global, M, mask, good_matches, matchesMask, src_pts, dst_pts = Camera.match(self, img_global, img_local)

    #     # 立体矫正
    #     R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(K1, D1, K2, D2, imgL.shape[::-1], R, T)
    #     mapL1, mapL2 = cv2.initUndistortRectifyMap(K1, D1, R1, P1, imgL.shape[::-1], cv2.CV_16SC2)
    #     mapR1, mapR2 = cv2.initUndistortRectifyMap(K2, D2, R2, P2, imgR.shape[::-1], cv2.CV_16SC2)
    #     imgL_rectified = cv2.remap(imgL, mapL1, mapL2, cv2.INTER_LINEAR)
    #     imgR_rectified = cv2.remap(imgR, mapR1, mapR2, cv2.INTER_LINEAR)

    #     # 计算视差图
    #     window_size = 5
    #     min_disp = 0
    #     num_disp = 128
    #     stereo = cv2.StereoSGBM_create(
    #         minDisparity=min_disp,
    #         numDisparities=num_disp,
    #         blockSize=window_size,
    #         uniquenessRatio=10,
    #         speckleWindowSize=100,
    #         speckleRange=32,
    #         disp12MaxDiff=1,
    #         P1=8 * 3 * window_size ** 2,
    #         P2=32 * 3 * window_size ** 2,
    #     )

    #     disp_map = stereo.compute(imgL_rectified, imgR_rectified).astype(np.float32) / 16.0

    #     # 计算深度图
    #     depth_map = compute_depth_map(disp_map, K1, T)

    #     # 可视化深度图
    #     depth_map_normalized = cv2.normalize(depth_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    #     cv2.imshow("Depth Map", depth_map_normalized)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    #     # 加载局部图像与全局图像中的匹配特征点
    #     local_points = np.round(src_pts).astype(int).reshape(-1, 2) # 局部图像中的特征点坐标（单位：像素）
    #     global_points = np.round(dst_pts).astype(int).reshape(-1, 2)# 通过单应性矩阵计算得到的全局图像中的对应特征点坐标（单位：像素）

    #     # 计算匹配特征点之间的距离
    #     distances = []
    #     for local_point, global_point in zip(local_points, global_points):
    #         local_3D = img_to_world_coords(int(local_point[0]), int(local_point[1]), depth_map, K1)
    #         global_3D = img_to_world_coords(int(global_point[0]), int(global_point[1]), depth_map, K1)

    #         distance = np.linalg.norm(local_3D - global_3D)
    #         distances.append(distance)

    #     print("Distances between matched feature points (in cm):", distances)
    def calcHorizontalDistance(self, global_img_path=None, local_img_path=None):
        pass
        # global img_result, horizontal_angle, vertical_angle, distance
        # # 读取原图像和局部图像
        # if global_img_path is not None and local_img_path is not None:
        #     img_global = cv2.imread(self.Settings.ImageChooseGloadPath)
        #     img_local = cv2.imread(self.Settings.ImageChooseLocalPath)
        # elif self.Settings.ImageChooseGloadPath != '' and self.Settings.ImageChooseLocalPath != '':
        #     # img_global_gray = cv2.imread(self.Settings.ImageChooseGloadPath, cv2.IMREAD_GRAYSCALE)
        #     # img_local_gray = cv2.imread(self.Settings.ImageChooseLocalPath, cv2.IMREAD_GRAYSCALE)
        #     img_global = cv2.imread(self.Settings.ImageChooseGloadPath)
        #     img_local = cv2.imread(self.Settings.ImageChooseLocalPath)
        # else:
        #     UIFunctions.showMessageBox(self, '请先选择图片！', 1)
        #     return False
        # # 特征匹配            
        # kp_local, kp_global, M, mask, good_matches, matchesMask, src_pts, dst_pts = Camera.match(self, img_global, img_local)
        # # # 加载双目摄像头校准参数
        # # fs = cv2.FileStorage(UIFunctions.getResultFilePath(self, self.Settings.WebCameraCalibrationParametersPath), cv2.FILE_STORAGE_READ)
        # # K1 = fs.getNode("K1").mat()
        # # K2 = fs.getNode("K2").mat()
        # # D1 = fs.getNode("D1").mat()
        # # D2 = fs.getNode("D2").mat()
        # # R = fs.getNode("R").mat()
        # # T = fs.getNode("T").mat()
        # # fs.release()

        # # 加载校准参数
        # with open(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\calibration_params.yml", 'r') as f:
        #     data = f.read()
        # params = yaml.safe_load(data)
        # K1 = np.array(params['cameraMatrix1']) # 左摄像头内参矩阵
        # K2 = np.array(params['cameraMatrix2']) # 右摄像头内参矩阵
        # D1 = np.array(params['distCoeffs1']) # 左摄像头畸变系数
        # D2 = np.array(params['distCoeffs2']) # 右摄像头畸变系数
        # R = np.array(params['R']) # 旋转矩阵
        # T = np.array(params['T']) # 平移向量

        # # 三角化重投影
        # P1 = np.hstack((K1, np.zeros((3, 1))))
        # P2 = np.hstack((K2, -K2 @ T))

        # points_4d = cv2.triangulatePoints(P1, P2, src_pts.T, dst_pts.T)
        
        # # 对非零值进行归一化，避免除零错误
        # points_3d = points_4d / points_4d[3, np.newaxis]
        # points_3d = points_3d[:3].T

        # # 计算平均距离
        # distances = np.sqrt(np.sum(np.square(points_3d), axis=1))
        # avg_distance = np.mean(distances)

        # print("平均距离(cm)：", avg_distance)
    
    # 图像特征匹配步骤
    def matchStep(self, global_img_path=None, local_img_path=None, index=None, showLiucheng=False, step=None):
        global img_result, matchPointRate, mathTimeCost, HError, VError, DError, horizontal_angle, vertical_angle, distance
        img_result = None
        # 读取原图像和局部图像
        if global_img_path is not None and local_img_path is not None:
            img_global = cv2.imread(global_img_path)
            img_local = cv2.imread(local_img_path)
        elif self.Settings.ImageChooseGloadPath != '' and self.Settings.ImageChooseLocalPath != '':
            # img_global_gray = cv2.imread(self.Settings.ImageChooseGloadPath, cv2.IMREAD_GRAYSCALE)
            # img_local_gray = cv2.imread(self.Settings.ImageChooseLocalPath, cv2.IMREAD_GRAYSCALE)
            img_global = cv2.imread(self.Settings.ImageChooseGloadPath)
            img_local = cv2.imread(self.Settings.ImageChooseLocalPath)
        else:
            UIFunctions.showMessageBox(self, '请先选择图片！', 1)
            return False
        ################################
        #         1. 特征提取          #
        ###############################
        img_global_gray= cv2.cvtColor(img_global, cv2.COLOR_BGR2GRAY)
        img_local_gray= cv2.cvtColor(img_local, cv2.COLOR_BGR2GRAY)
        if index == None:
            featureAlgorithm = int(self.Settings.FeatureAlgorithm)
        else:
            featureAlgorithm = index
        # SIFT算法
        if featureAlgorithm != 4:
            timer = AverageTimer(newline=True)
            if featureAlgorithm == 0:
                # 适配OpenCV4.0
                if cv2.__version__.startswith('4.'): 
                    sift = cv2.SIFT_create()
                else:
                    sift = cv2.xfeatures2d.SIFT_create()
                # 提取特征点和特征描述符
                kp_global, des_global = sift.detectAndCompute(img_global_gray, None)
                kp_local, des_local = sift.detectAndCompute(img_local_gray, None)
                FLANN_INDEX = 1
            # SURF算法1
            elif featureAlgorithm == 1:
                # 适配OpenCV4.x
                if cv2.__version__.startswith('4.'):
                    UIFunctions.showMessageBox(self, "安装的Opencv版本不包含SURF算法，建议安装3.4.1.15版本！", 2)
                    return False
                    # surf = cv2.xfeatures2d.SURF_create(400, nOctaves=4, extended=True)
                else:
                    surf = cv2.xfeatures2d.SURF_create(400, nOctaves=4, extended=True, upright=True)
                
                # 在全景图和局部图中提取特征点和描述符
                kp_global, des_global = surf.detectAndCompute(img_global_gray, None)
                kp_local, des_local = surf.detectAndCompute(img_local_gray, None)
                # 使用FLANN匹配器进行特征点匹配
                FLANN_INDEX = 1
            # ORB算法
            elif featureAlgorithm == 2:
                orb = cv2.ORB_create()
                kp_global, des_global = orb.detectAndCompute(img_global_gray, None)
                kp_local, des_local = orb.detectAndCompute(img_local_gray, None)
                FLANN_INDEX = 6
            # AKAZE算法
            elif featureAlgorithm == 3:
                akaze = cv2.AKAZE_create()
                kp_global, des_global = akaze.detectAndCompute(img_global_gray, None)
                kp_local, des_local = akaze.detectAndCompute(img_local_gray, None)
                FLANN_INDEX = 6
            # Step1
            # 描述提取的特征点
            self.ui.btn_Setp1.setStyleSheet("border-color: rgb(239, 87, 119)")
            self.ui.line1.setStyleSheet("color: rgb(255, 241, 0)")
            img_global_keypoints = cv2.drawKeypoints(img_global, kp_global, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            img_local_keypoints = cv2.drawKeypoints(img_local, kp_local, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            if showLiucheng:
                timer.pause()
                UIFunctions.showImage(self, [img_local_keypoints, img_global_keypoints])
                timer.resume()
            ################################
            #         2. 特征匹配          #
            ###############################
            # # 使用BFMatcher对象进行特征点匹配（暴力匹配）
            # bf = cv2.BFMatcher()
            # matches = bf.knnMatch(des_global, des_local, k=2)
            # 索引算法：0/1 :基于KD树    6：基于LSH（局部敏感哈希）
            if FLANN_INDEX == 0 or FLANN_INDEX == 1:
                index_params = dict(algorithm=FLANN_INDEX, trees=5)
                search_params = dict(checks=100)
                flann = cv2.FlannBasedMatcher(index_params, search_params)
                matches = flann.knnMatch(des_local, des_global, k=2)
            elif FLANN_INDEX == 6:
                index_params = dict(algorithm=FLANN_INDEX, table_number=6, key_size=12, multi_probe_level=1)
                search_params = dict(checks=100)
                flann = cv2.FlannBasedMatcher(index_params, search_params)
                matches = flann.knnMatch(des_local, des_global, k=2)
            # # 初始化FLANN算法，自动获取最优参数
            # matcher = cv2.FlannBasedMatcher()
            # matcher_params = matcher.getEffectiveMatcherParams()
            # # 特征点匹配
            # matches = matcher.knnMatch(descriptors_local, descriptors_global, k=2)
            # # print("FLANN matcher parameters:", matcher_params)
            timer.update('match')
            # Step2
            self.ui.btn_Setp2.setStyleSheet("border-color: #575fcf")
            self.ui.line1.setStyleSheet("color: rgb(108, 252, 20)")
            self.ui.line2.setStyleSheet("color: rgb(255, 241, 0)")
            # 将匹配结果绘制到图像上
            img_result = cv2.drawMatchesKnn(img_local, kp_local, img_global, kp_global, matches, None, flags=2)
            # draw_params = dict(singlePointColor=None,
            #                 matchesMask=None,  # draw only inliers
            #                 flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            # img_result = cv2.drawMatches(img_local, kp_local, img_global, kp_global, matches, None, matchesThickness=None)
            self.ui.label_matchPoints.setText(f"匹配点数：{len(matches)}/{len(kp_global)}")
            if showLiucheng:
                timer.pause()
                UIFunctions.showImage(self, img_result)
                timer.resume()
            
            # 应用尺度空间扩展和RANSAC算法来提高匹配准确性
            good_matches = []
            MIN_MATCH_COUNT = self.Settings.MatchDeadline
            for m, n in matches:
                if m.distance < self.Settings.MatchRatio * n.distance:
                    good_matches.append(m)
            print('匹配点数：', len(good_matches))
            if len(good_matches) > MIN_MATCH_COUNT:
                # 获取关键点的坐标
                src_pts = np.float32([kp_local[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
                dst_pts = np.float32([kp_global[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
                # 第三个参数 Method used to computed a homography matrix. The following methods are possible: #0 - a regular method using all the points
                # CV_RANSAC - RANSAC-based robust method
                # CV_LMEDS - Least-Median robust method
                # 第四个参数取值范围在 1 到 10  绝一个点对的值。原图像的点经变换后点与目标图像上对应点的差 #    差就是 outlier
                # 返回值中 M 为变换矩阵，也叫单应性矩阵
                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                matchesMask = mask.ravel().tolist()
                h, w = img_local_gray.shape[:2]
                # 使用得到的变换矩 对原图像的四个角变换 获得在目标图像上对应的坐标
                pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)
                img_global = cv2.polylines(img_global, [np.int32(dst)], True, (17, 241, 21), 3, cv2.LINE_AA)
            else:
                matchesMask = None
            
            # step3
            self.ui.btn_Setp3.setStyleSheet("border-color: #4bcffa")
            self.ui.line2.setStyleSheet("color: rgb(108, 252, 20)")
            self.ui.line3.setStyleSheet("color: rgb(255, 241, 0)")
            draw_params = dict(singlePointColor=None,
                            matchesMask=matchesMask,  # draw only inliers
                            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            img_result = cv2.drawMatches(img_local, kp_local, img_global, kp_global, good_matches, None, **draw_params)

            if showLiucheng:
                timer.pause()
                UIFunctions.showImage(self, img_result)
                timer.resume()
            elif step == 3:
                UIFunctions.showImage(self, img_result)
                timer.print()
                return
            timer.update('calc')
            # 计算局部图像和全局图像之间的变换矩阵
            h, w = img_local.shape[:2]
            corners_global = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            corners_local = cv2.perspectiveTransform(corners_global, M)

            # 根据变换矩阵计算水平角、垂直角和直线距离
            dx = corners_local[0][0][0] - corners_global[0][0][0]
            dy = corners_local[0][0][1] - corners_global[0][0][1]
            horizontal_angle = np.rad2deg(np.arctan2(dy, dx))
            vertical_angle = np.rad2deg(np.arctan2(dx, dy))
            distance = np.sqrt(dx**2 + dy**2)

            print("水平偏移角: {:.2f}°".format(horizontal_angle))
            print("垂直偏移角: {:.2f}°".format(vertical_angle))
            print("直线距离: {:.2f} 像素".format(distance))
            # step4
            cv2.putText(img_result, u"Horizontal offset angle: {:.2f}".format(horizontal_angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img_result, u"Vertical offset angle: {:.2f}".format(vertical_angle), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            self.ui.btn_Setp4.setStyleSheet("border-color: #0be881")
            self.ui.line3.setStyleSheet("color: rgb(108, 252, 20)")
            self.ui.line4.setStyleSheet("color: rgb(255, 241, 0)")
            if showLiucheng:
                timer.pause()
                UIFunctions.showImage(self, img_result)
                timer.resume()
            elif step == 4:
                UIFunctions.showImage(self, img_result)
                timer.print()
                return

            # step5
            Camera.calcHorizontalDistance(self)
            self.ui.btn_Setp5.setStyleSheet("border-color: #f8a5c2")
            self.ui.line4.setStyleSheet("color: rgb(108, 252, 20)")
            cv2.putText(img_result, "distance: {:.2f} px".format(distance), (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            total_time = timer.get_total_time()
            timer.print()
        # 基于SuperPoint和SuperGlue算法
        else:
            good_matches, kp_local, horizontal_angle, vertical_angle, distance, total_time, img_result = imgMatch(self.Settings.ImageChooseLocalPath, self.Settings.ImageChooseGloadPath, 
                    keypoint_threshold=self.Settings.KeypointThreshold, match_threshold=self.Settings.MatchThreshold)
    
        UIFunctions.showImage(self, img_result)
        if step != None:
            timer.print()
            return
        ############################
        #       设置Label          #
        ############################
        label = [self.ui.label1_1_1, self.ui.label2_1_1, self.ui.label3_1_1, self.ui.label4_1_1, self.ui.label5_1_1] 
        if index != None:
            label[index].setText(f"特征匹配点：{len(good_matches)}/{len(kp_local)}")
            matchPointRate[index] = len(good_matches) / len(kp_local)
        else:
            label[featureAlgorithm].setText(f"特征匹配点：{len(good_matches)}/{len(kp_local)}")
            matchPointRate[featureAlgorithm] = len(good_matches) / len(kp_local)
            self.ui.label_matchPoints.setText(f"匹配点数：{len(good_matches)}/{len(kp_local)}")

        self.ui.label_HOffset.setText("{:.2f}".format(horizontal_angle))
        self.ui.label_VOffset.setText("{:.2f}".format(vertical_angle))
        if index != None:
            label = [self.ui.label1_H, self.ui.label2_H, self.ui.label3_H, self.ui.label4_H, self.ui.label5_H] 
            label[index].setText("{:.2f}".format(horizontal_angle))
            label = [self.ui.label1_V, self.ui.label2_V, self.ui.label3_V, self.ui.label4_V, self.ui.label5_V]
            label[index].setText("{:.2f}".format(vertical_angle))
        else:
            label = [self.ui.label1_H, self.ui.label2_H, self.ui.label3_H, self.ui.label4_H, self.ui.label5_H] 
            label[featureAlgorithm].setText("{:.2f}".format(horizontal_angle))
            label = [self.ui.label1_V, self.ui.label2_V, self.ui.label3_V, self.ui.label4_V, self.ui.label5_V]
            label[featureAlgorithm].setText("{:.2f}".format(vertical_angle))
            self.ui.label_HDistance.setText("{:.2f}".format(distance))
        if index != None:
            label = [self.ui.label1_D, self.ui.label2_D, self.ui.label3_D, self.ui.label4_D, self.ui.label5_D] 
            label[index].setText("{:.2f}".format(distance))
        else:
            label = [self.ui.label1_D, self.ui.label2_D, self.ui.label3_D, self.ui.label4_D, self.ui.label5_D] 
            label[featureAlgorithm].setText("{:.2f}".format(distance))
        ##############################
        #          统计排序          #
        ##############################
        # 计算误差
        if float(self.Settings.ResultHAngle) != 0:
            label = [self.ui.label1_HError, self.ui.label2_HError, self.ui.label3_HError, self.ui.label4_HError, self.ui.label5_HError]
            if index != None:
                Camera.calcError(self, horizontal_angle, self.Settings.ResultHAngle, self.ui.label_HError, label[index])
            else:
                Camera.calcError(self, horizontal_angle, self.Settings.ResultHAngle, self.ui.label_HError, label[featureAlgorithm])
        if float(self.Settings.ResultVAngle) != 0:
            label = [self.ui.label1_VError, self.ui.label2_VError, self.ui.label3_VError, self.ui.label4_VError, self.ui.label5_VError]
            if index != None:
                Camera.calcError(self, vertical_angle, self.Settings.ResultVAngle, self.ui.label_VError, label[index])
            else:
                Camera.calcError(self, vertical_angle, self.Settings.ResultVAngle, self.ui.label_VError, label[featureAlgorithm])
        if float(self.Settings.ResultDistance) != 0:
            label = [self.ui.label1_DError, self.ui.label2_DError, self.ui.label3_DError, self.ui.label4_DError, self.ui.label5_DError]
            if index != None:
                Camera.calcError(self, distance, self.Settings.ResultDistance, self.ui.label_HDistanceError, label[index])
            else:
                Camera.calcError(self, distance, self.Settings.ResultDistance, self.ui.label_HDistanceError, label[featureAlgorithm])
        # 创建一个浮点数数列
        arr = np.array(matchPointRate)
        # 找到最值的索引
        label = [self.ui.label1_1_2, self.ui.label2_1_2, self.ui.label3_1_2, self.ui.label4_1_2, self.ui.label5_1_2] 
        sort_list = np.argsort(arr)
        label[sort_list[0]].setStyleSheet("color: rgb(0, 255, 0);font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[1]].setStyleSheet("color: #33d9b2;font: 14pt '楷体';text-decoration: underline;") 
        label[sort_list[2]].setStyleSheet("color: #ffdd59;font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[3]].setStyleSheet("color: #ea8685;font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[4]].setStyleSheet("color: rgb(255, 0, 0);font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[0]].setText("1")
        label[sort_list[1]].setText("2")
        label[sort_list[2]].setText("3")
        label[sort_list[3]].setText("4")
        label[sort_list[4]].setText("5")
        # 创建一个浮点数数列
        arr = np.array(mathTimeCost)
        # 找到最值的索引
        sort_list = np.argsort(arr)
        label = [self.ui.label1_2_2, self.ui.label2_2_2, self.ui.label3_2_2, self.ui.label4_2_2, self.ui.label5_2_2] 
        label[sort_list[0]].setStyleSheet("color: rgb(0, 255, 0);font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[1]].setStyleSheet("color: #33d9b2;font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[2]].setStyleSheet("color: #ffdd59;font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[3]].setStyleSheet("color: #ea8685;font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[4]].setStyleSheet("color: rgb(255, 0, 0);font: 14pt '楷体';text-decoration: underline;")
        label[sort_list[0]].setText("1")
        label[sort_list[1]].setText("2")
        label[sort_list[2]].setText("3")
        label[sort_list[3]].setText("4")
        label[sort_list[4]].setText("5")
        # 总体评分
        all_data = [x + y for x, y in zip(matchPointRate, mathTimeCost)]
        arr = np.array(all_data)
        sort_list = np.argsort(arr)
        label = [self.ui.label1_3, self.ui.label2_3, self.ui.label3_3, self.ui.label4_3, self.ui.label5_3]
        label[sort_list[0]].setStyleSheet("color: rgb(0, 255, 0);font: 16pt '楷体';text-decoration: underline;")
        label[sort_list[1]].setStyleSheet("color: #33d9b2;font: 16pt '楷体';text-decoration: underline;")
        label[sort_list[2]].setStyleSheet("color: #ffdd59;font: 16pt '楷体';text-decoration: underline;")
        label[sort_list[3]].setStyleSheet("color: #ea8685;font: 16pt '楷体';text-decoration: underline;")
        label[sort_list[4]].setStyleSheet("color: rgb(255, 0, 0);font: 16pt '楷体';text-decoration: underline;")
        label[sort_list[0]].setText("最好")
        label[sort_list[1]].setText("较好")
        label[sort_list[2]].setText("一般")
        label[sort_list[3]].setText("较差")
        label[sort_list[4]].setText("最差")
        
        self.ui.btn_Setp1.setStyleSheet("")
        self.ui.btn_Setp2.setStyleSheet("")
        self.ui.btn_Setp3.setStyleSheet("")
        self.ui.btn_Setp4.setStyleSheet("")
        self.ui.btn_Setp5.setStyleSheet("")
        self.ui.line1.setStyleSheet("color: rgb(255, 255, 255)")
        self.ui.line2.setStyleSheet("color: rgb(255, 255, 255)")
        self.ui.line3.setStyleSheet("color: rgb(255, 252, 255)")
        self.ui.line4.setStyleSheet("color: rgb(255, 255, 255)")
        # 显示耗时
        label = [self.ui.label1_2_1, self.ui.label2_2_1, self.ui.label3_2_1, self.ui.label4_2_1, self.ui.label5_2_1]
        # timer.print()
        # print("{}耗时：{:.2f} s".format(self.Settings.getFeatureAlgorithm(), timer.get_total_time()))
        self.ui.label_timeCount.setText("耗时：{:.2f} s".format(total_time))
        if index != None:
            label[index].setText("耗时：{:.2f} s".format(total_time))
            mathTimeCost[index] = total_time
        else:
            label[featureAlgorithm].setText("耗时：{:.2f} s".format(total_time))
            mathTimeCost[featureAlgorithm] = total_time
    
    ######################################################
    #                    摄像头标定                      #
    ######################################################
    def biaoding(self, qipan_x, qipan_y, min_img_num, size):
        try:
            # 棋盘规格，这里是 9x6 的黑白相间的棋盘
            CHESSBOARD_SIZE = (qipan_x, qipan_y)
            CHESSBOARD_SQUARE_SIZE = size  # 棋盘格子的尺寸（单位为cm）
            MIN_COUNT_IMG = min_img_num  # 最少需要多少张图像进行标定

            # 存储所有棋盘角点的像素坐标和对应的实际坐标
            img_points_left = []   # 左侧相机的图像坐标
            img_points_right = []  # 右侧相机的图像坐标
            obj_points = []        # 实际坐标

            # 定义棋盘角点的真实坐标
            objp = np.zeros((CHESSBOARD_SIZE[0] * CHESSBOARD_SIZE[1], 3), np.float32)
            objp[:, :2] = np.mgrid[0:CHESSBOARD_SIZE[0], 0:CHESSBOARD_SIZE[1]].T.reshape(-1, 2)
            objp *= CHESSBOARD_SQUARE_SIZE

            # # 创建双目摄像头对象
            # cap_left = cv2.VideoCapture(1, cv2.CAP_DSHOW)
            # cap_right = cv2.VideoCapture(2, cv2.CAP_DSHOW)

            # # 设置摄像头分辨率
            # cap_left.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            # cap_left.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            # cap_right.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            # cap_right.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            # 定义摄像头参数
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
            flags = (cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_FAST_CHECK)

            # 创建窗口
            cv2.namedWindow("Calibration", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Calibration", 1280, 480)
            # 如果摄像头已经打开则先关闭再打开
            if self.openCamera:
                self.Camera.openClosecamera(self, openTimer=False)
            self.Camera.openClosecamera(self, openTimer=False)
            # 检查摄像头是否正常工作
            if not self.camera_left.isOpened() or not self.camera_right.isOpened():
                UIFunctions.showMessageBox(self, "摄像头未正常工作，请检查！", 2)
                return

            # 开始循环捕获图像
            while True:
                # 读取左右两个相机的图像
                ret_left, frame_left = self.camera_left.read()
                ret_right, frame_right = self.camera_right.read()

                # 调整左右摄像头的图像尺寸，使它们相同
                frame_left = cv2.resize(frame_left, (640, 480))
                frame_right = cv2.resize(frame_right, (640, 480))

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
                    cv2.putText(img, "Press Esc/Q to Exit", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    
                    # 降低频率
                    time.sleep(0.2)
                else:
                    # 如果只有一个相机检测到了角点，则在另一个相机的图像中绘制角点
                    if ret_left == True:
                        cv2.drawChessboardCorners(frame_right, CHESSBOARD_SIZE, corners_left, False)
                    if ret_right == True:
                        cv2.drawChessboardCorners(frame_left, CHESSBOARD_SIZE, corners_right, False)

                    # 将两个相机的图像合并到同一张图上，并显示当前标定进度
                    img = np.hstack((frame_left, frame_right))
                    cv2.putText(img, f"Image count: {len(img_points_left)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(img, "Press Esc/Q to Exit", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                # 显示合并后的图像
                cv2.imshow("Calibration", img)
                # if self.Settings.ShowResultImageExtreWin:
                    # cv2.imshow("Calibration", img)
                # else:
                #     img = QImage(img, img.shape[1], img.shape[0], QImage.Format.Format_RGB888)
                #     # 将QImage对象设置到QLabel中
                #     self.ui.cameraLabel.setPixmap(QPixmap.fromImage(img.rgbSwapped()))

                # 如果收集到了足够多的图像，则进行标定并保存结果
                if len(img_points_left) > MIN_COUNT_IMG:
                    cv2.destroyAllWindows()
                    self.Camera.openClosecamera(self, openTimer=False)
                    print("收集到足够多的照片，开始标定...")
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

                    # # 保存标定结果到文件
                    # file_path = os.path.join(os.getcwd(), "calibration_params.yml")
                    # with cv2.FileStorage(file_path, cv2.FILE_STORAGE_WRITE) as fs:
                    #     fs.write("dist_coeffs_left", dist_left)
                    #     fs.write("camera_matrix_right", mtx_right)
                    #     fs.write("dist_coeffs_right", dist_right)
                    #     fs.write("R", R)
                    #     fs.write("T", T)

                    # 显示标定结果
                    plt.imshow(cv2.cvtColor(frame_left, cv2.COLOR_BGR2RGB))
                    plt.title("Calibration Result")
                    plt.show()
                    break

                # 按下 ESC 或 Q键退出程序
                key = cv2.waitKey(1)
                if key == 27 or key == ord('q'):
                    cv2.destroyAllWindows()
                    self.Camera.openClosecamera(self, openTimer=False)
                    break

        except Exception as e:
            cv2.destroyAllWindows()
            self.Camera.openClosecamera(self, openTimer=False)
            UIFunctions.showMessageBox(self, f"Error:{e}", 2)
    
    # 计算误差并显示
    def calcError(self, calc_value, result_value, *labels):
        global horizontal_angle, vertical_angle, distance
        if calc_value == -1:
            calc_value = horizontal_angle
        elif calc_value == -2:
            calc_value = vertical_angle
        elif calc_value == -3:
            calc_value = distance
        error = abs((calc_value-float(result_value)) / self.Settings.ErrorAngle * 100)
        for label in labels:
            label.setText("{:.2f}%".format(error))
            if error > int(100 * self.Settings.MaxErrorValue):
                label.setStyleSheet("color: rgb(255, 0, 0);")
            else:
                label.setStyleSheet("color: rgb(0, 255, 0);")



