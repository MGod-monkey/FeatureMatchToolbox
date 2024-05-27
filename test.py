# import numpy as np
# import cv2
# import imutils

# index = 0
# arr = []
# while True:
#     cap = cv2.VideoCapture(index)

#     if not cap.read()[0]:
#         break
#     else:
#         arr.append(index)
#     cap.release()
#     index += 1

# video_captures = [cv2.VideoCapture(idx, cv2.CAP_DSHOW) for idx in arr]
# print(arr)

# while True:
#     # Capture frame-by-frame
#     frames = []
#     frames_preview = []

#     for i in arr:
#         # skip webcam capture
#         if i == 1: continue
#         ret, frame = video_captures[i].read()
#         if ret:
#             frames.append(frame)
#             small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#             frames_preview.append(small)

#     for i, frame in enumerate(frames_preview):
#         cv2.imshow('Cam {}'.format(i), frame)


#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything is done, release the capture
# for video_capture in video_captures:
#     video_capture.release()
# cv2.destroyAllWindows()

#############################################
#        SIFT算法
#############################################
# import cv2
# import numpy as np

# def main():
#     # Load images
#     global_img = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box_in_scene.png")
#     local_img = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box.png")
    
#     # Step 1: 使用SIFT提取特征点和描述符
#     # 适配OpenCV3.0
#     if cv2.__version__.startswith('3.'):
#         sift = cv2.xfeatures2d.SIFT_create()
#         #     # 创建SURF对象
#         # surf = cv2.xfeatures2d.SURF_create(400, nOctaves=4, extended=True)
#     else:
#         sift = cv2.SIFT_create()
#     kp_global, des_global = sift.detectAndCompute(global_img, None)
#     kp_local, des_local = sift.detectAndCompute(local_img, None)


#     # # 在全景图和局部图中提取特征点和描述符
#     # kp_global, des_global = surf.detectAndCompute(global_img, None)
#     # kp_local, des_local = surf.detectAndCompute(local_img, None)
    
#     # Step 2: 使用FLANN匹配器进行特征点匹配
#     FLANN_INDEX_KDTREE = 0
#     index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
#     search_params = dict(checks=50)

#     flann = cv2.FlannBasedMatcher(index_params, search_params)
#     matches = flann.knnMatch(des_local, des_global, k=2)

#     good_matches = []
#     MIN_MATCH_COUNT = 4
#     for m, n in matches:
#         if m.distance < 0.7 * n.distance:
#             good_matches.append(m)
#     if len(good_matches) > MIN_MATCH_COUNT:
#         # 获取关 点的坐标
#         src_pts = np.float32([kp_local[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
#         dst_pts = np.float32([kp_global[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

#         # 第三个参数 Method used to computed a homography matrix. The following methods are possible: #0 - a regular method using all the points
#         # CV_RANSAC - RANSAC-based robust method
#         # CV_LMEDS - Least-Median robust method
#         # 第四个参数取值范围在 1 到 10  绝一个点对的 值。原图像的点经 变换后点与目标图像上对应点的 差 #    差就 为是 outlier
#         #  回值中 M 为变换矩 。
#         M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
#         matchesMask = mask.ravel().tolist()
#         # 获得原图像的高和宽
#         h, w = local_img.shape[:2]
#         # 使用得到的变换矩 对原图像的四个   变换 获得在目标图像上对应的坐标
#         pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
#         dst = cv2.perspectiveTransform(pts, M)
#         # 原图像为灰度图
#         global_img = cv2.polylines(global_img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
#         # Step 4: 计算局部图片相对于全局图片的变换矩阵
#         corners_global = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
#         corners_local = cv2.perspectiveTransform(corners_global, M)

#         # Step 5: 根据变换矩阵计算水平偏移角、垂直偏移角和直线距离
#         dx = corners_local[0][0][0] - corners_global[0][0][0]
#         dy = corners_local[0][0][1] - corners_global[0][0][1]
#         horizontal_angle = np.rad2deg(np.arctan2(dy, dx))
#         vertical_angle = np.rad2deg(np.arctan2(dx, dy))
#         distance = np.sqrt(dx**2 + dy**2)

#         print("水平偏移角: {:.2f}°".format(horizontal_angle))
#         print("垂直偏移角: {:.2f}°".format(vertical_angle))
#         print("直线距离: {:.2f} 像素".format(distance))
#     else:
#         matches_mask = None

#     # # Step 3: 利用RANSAC算法找到匹配点之间的单应性矩阵
#     # src_pts = np.float32([kp_local[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
#     # dst_pts = np.float32([kp_global[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

#     # # Step 4: 计算局部图片相对于全局图片的变换矩阵
#     # h, w = local_img.shape[:2]
#     # corners_global = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
#     # corners_local = cv2.perspectiveTransform(corners_global, H)

#     # # Step 5: 根据变换矩阵计算水平偏移角、垂直偏移角和直线距离
#     # dx = corners_local[0][0][0] - corners_global[0][0][0]
#     # dy = corners_local[0][0][1] - corners_global[0][0][1]
#     # horizontal_angle = np.rad2deg(np.arctan2(dy, dx))
#     # vertical_angle = np.rad2deg(np.arctan2(dx, dy))
#     # distance = np.sqrt(dx**2 + dy**2)
    
#     # print("水平偏移角: {:.2f}°".format(horizontal_angle))
#     # print("垂直偏移角: {:.2f}°".format(vertical_angle))
#     # print("直线距离: {:.2f} 像素".format(distance))
    
#     # Step 6: 展示匹配结果
#     # 最后我再绘制 inliers 如果能成功的找到目标图像的话  或者匹配的关  点 如果失败。matchColor=(17, 241, 21),
#     draw_params = dict(singlePointColor=None,
#                     matchesMask=matchesMask,  # draw only inliers
#                     flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
#     img_matches = cv2.drawMatches(local_img, kp_local, global_img, kp_global, good_matches, None, **draw_params)
#     # # 将结果图缩小一半
#     # img_matches = cv2.resize(img_matches, (0, 0), fx=0.5, fy=0.5)
#     # Step 7: 展示计算结果
#     # cv2.putText(img_matches, "horizontal offset angle: {:.2f}".format(horizontal_angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     # cv2.putText(img_matches, "vertical offset angle: {:.2f}".format(vertical_angle), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     # cv2.putText(img_matches, "Straight line distance: {:.2f} px".format(distance), (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     cv2.imshow("Results", img_matches)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()

####################################################
#                   ORB算法
####################################################
# import cv2
# import numpy as np

# # Load images
# global_img = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box_in_scene.png")
# local_img = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box.png")

# # Step 1: Use ORB to extract keypoints and descriptors
# orb = cv2.ORB_create()
# kp_global, des_global = orb.detectAndCompute(global_img, None)
# kp_local, des_local = orb.detectAndCompute(local_img, None)

# # Step 2: Use FLANN matcher for feature points matching
# FLANN_INDEX_LSH = 6
# index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=1)
# search_params = dict(checks=50)
# flann = cv2.FlannBasedMatcher(index_params, search_params)
# matches = flann.knnMatch(des_local, des_global, k=2)

# good_matches = []
# matches_mask = None
# for m, n in matches:
#     if m.distance < 0.75 * n.distance:
#         good_matches.append(m)

# # Step 3: Use RANSAC algorithm to find homography between matched points
# if len(good_matches) >= 4:
#     src_pts = np.float32([kp_local[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
#     dst_pts = np.float32([kp_global[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
#     M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
#     matches_mask = mask.ravel().tolist()
#     h, w = global_img.shape[0], global_img.shape[1]
#     pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
#     dst = cv2.perspectiveTransform(pts, M)
#     global_img = cv2.polylines(global_img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

#     # Step 4: Compute transformation matrix between local image and global image
#     h, w = local_img.shape[:2]
#     corners_global = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
#     corners_local = cv2.perspectiveTransform(corners_global, M)

#     # Step 5: Compute horizontal angle, vertical angle, and straight line distance based on transformation matrix
#     dx = corners_local[0][0][0] - corners_global[0][0][0]
#     dy = corners_local[0][0][1] - corners_global[0][0][1]
#     horizontal_angle = np.rad2deg(np.arctan2(dy, dx))
#     vertical_angle = np.rad2deg(np.arctan2(dx, dy))
#     distance = np.sqrt(dx**2 + dy**2)

#     print("水平偏移角: {:.2f}°".format(horizontal_angle))
#     print("垂直偏移角: {:.2f}°".format(vertical_angle))
#     print("直线距离: {:.2f} 像素".format(distance))

#     # Step 6: Show matching results
#     img_matches = cv2.drawMatches(local_img, kp_local, global_img, kp_global, good_matches, None, matchesMask=matches_mask, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

#     # Step 7: Show calculation results
#     cv2.putText(img_matches, "horizontal offset angle: {:.2f}".format(horizontal_angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     cv2.putText(img_matches, "vertical offset angle: {:.2f}".format(vertical_angle), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     cv2.putText(img_matches, "Straight line distance: {:.2f} px".format(distance), (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     cv2.imshow("Results", img_matches)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Not enough matches are found - {}/{}".format(len(good_matches), 4))


####################################################
#                  SURF匹配算法
####################################################
# import cv2
# import numpy as np

# # 读取全景图和局部图
# global_img = cv2.imread("./images/globalImage.png")
# local_img = cv2.imread("./images/localImage.png")

# # 创建SURF对象
# surf = cv2.xfeatures2d.SURF_create(400, nOctaves=4, extended=True)

# # 在全景图和局部图中提取特征点和描述符
# kp_global, des_global = surf.detectAndCompute(global_img, None)
# kp_local, des_local = surf.detectAndCompute(local_img, None)

# # 使用FLANN匹配器进行特征点匹配
# FLANN_INDEX_KDTREE = 1
# index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
# search_params = dict(checks=50)
# flann = cv2.FlannBasedMatcher(index_params, search_params)
# matches = flann.knnMatch(des_local, des_global, k=2)

# # 对匹配结果进行筛选
# good_matches = []
# for m, n in matches:
#     if m.distance < 0.7 * n.distance:
#         good_matches.append(m)

# # 根据匹配结果计算变换矩阵
# src_pts = np.float32([kp_local[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
# dst_pts = np.float32([kp_global[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
# M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# # 计算局部图的四个角点在全景图中的坐标
# h, w = local_img.shape[:2]
# corners_local = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
# corners_global = cv2.perspectiveTransform(corners_local, M)

# # 计算偏移角度和距离
# dx = corners_global[0][0][0] - corners_local[0][0][0]
# dy = corners_global[0][0][1] - corners_local[0][0][1]
# horizontal_angle = np.rad2deg(np.arctan2(dy, dx))
# vertical_angle = np.rad2deg(np.arctan2(dx, dy))
# distance = np.sqrt(dx**2 + dy**2)

# # 在匹配结果中绘制偏移角度和距离信息
# img_matches = cv2.drawMatches(local_img, kp_local, global_img, kp_global, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# cv2.putText(img_matches, "Horizontal offset angle: {:.2f}".format(horizontal_angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
# cv2.putText(img_matches, "Vertical offset angle: {:.2f}".format(vertical_angle), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
# cv2.putText(img_matches, "Straight line distance: {:.2f} px".format(distance), (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
# cv2.imshow("Results", img_matches)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# """
# findHomography.py:联合使用特征提取和 calib3d 模块中的 findHomography 在复杂图像中查找已知对象
# """

# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# MIN_MATCH_COUNT = 10
# img1 = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box.png", 0)  # queryImage
# img2 = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box_in_scene.png", 0)  # trainImage

# # Initiate SIFT detector
# sift = cv2.xfeatures2d.SIFT_create()
# # find the keypoints and descriptors with SIFT
# kp1, des1 = sift.detectAndCompute(img1, None)
# kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN_INDEX_KDTREE = 0
# index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
# search_params = dict(checks=50)
# flann = cv2.FlannBasedMatcher(index_params, search_params)
# matches = flann.knnMatch(des1, des2, k=2)

# # store all the good matches as per Lowe's ratio test.
# good = []
# for m, n in matches:
#     if m.distance < 0.7 * n.distance:
#         good.append(m)
# '''
# 现在我们 置只有存在 10 个以上匹 时才去查找目标 MIN_MATCH_COUNT=10   否则显示 告消息  现在匹 不   
# 如果找到了 够的匹  我们 提取两幅图像中匹 点的坐标。把它们传 入到函数中 算  变换。一旦我们找到 3x3 的变换矩  就可以使用它将查  图像的四个 点 四个  变换到目标图像中去了。然后再绘制出来。
# '''

# if len(good) > MIN_MATCH_COUNT:
#     # 获取关 点的坐标
#     src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
#     dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

#     # 第三个参数 Method used to computed a homography matrix. The following methods are possible: #0 - a regular method using all the points
#     # CV_RANSAC - RANSAC-based robust method
#     # CV_LMEDS - Least-Median robust method
#     # 第四个参数取值范围在 1 到 10  绝一个点对的 值。原图像的点经 变换后点与目标图像上对应点的 差 #    差就 为是 outlier
#     #  回值中 M 为变换矩 。
#     M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
#     matchesMask = mask.ravel().tolist()
#     # 获得原图像的高和宽
#     h, w = img1.shape
#     # 使用得到的变换矩 对原图像的四个   变换 获得在目标图像上对应的坐标
#     pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
#     dst = cv2.perspectiveTransform(pts, M)
#     # 原图像为灰度图
#     img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
# else:
#     print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
#     matchesMask = None

# # 最后我再绘制 inliers 如果能成功的找到目标图像的话  或者匹配的关  点 如果失败。
# draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
#                    singlePointColor=None,
#                    matchesMask=matchesMask,  # draw only inliers
#                    flags=2)

# img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)

# plt.imshow(img3, 'gray'), plt.show()
# # 复杂图像中被找到的目标图像被标记成白色


# import cv2
# import numpy as np
# import torch
# from SuperGluePretrainedNetwork.models.matching import Matching

# # Load the SuperPoint and SuperGlue models
# superpoint_model, superpoint_feature = torch.hub.load('superpoint', 'superpoint_v1')
# superglue = Matching()

# # Load the images
# img1 = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box_in_scene.png", cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box.png", cv2.IMREAD_GRAYSCALE)

# # Convert the images to PyTorch tensors
# tensor1 = superpoint_feature({'image': img1})
# tensor2 = superpoint_feature({'image': img2})

# # Perform feature matching with SuperGlue
# matches = superglue({'image0': tensor1, 'image1': tensor2})

# # Visualize the matches
# img3 = cv2.drawMatches(img1, superpoint_model.keypoints[0], img2, superpoint_model.keypoints[1], matches['matches0'], None)
# cv2.imshow('Matches', img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import torch
# import numpy as np
# from pathlib import Path
# import os
# import sys

# super_glue_base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SuperGluePretrainedNetwork')
# super_glue_models_dir = os.path.join(super_glue_base_dir, 'models')

# sys.path.append(super_glue_base_dir)
# sys.path.append(super_glue_models_dir)

# from pathlib import Path
# from superpoint import SuperPoint
# from superglue import SuperGlue
# from utils import plot_matches

# # 初始化SuperPoint
# weights_path = 'SuperGluePretrainedNetwork/models/weights/superpoint_v1.pth'
# superpoint_config = {'weights_path': weights_path}
# superpoint = SuperPoint(superpoint_config)

# # 初始化SuperGlue
# superglue_weights_path = 'SuperGluePretrainedNetwork/models/weights/superglue_outdoor.pth'
# superglue = SuperGlue({'descriptor_dim': 256, 'weights_path': superglue_weights_path})

# # 读取图像并转换为灰度图
# image1 = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box.png", cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box_in_scene.png", cv2.IMREAD_GRAYSCALE)

# # 提取SuperPoint特征
# points1, descriptors1, _ = superpoint(image1)
# points2, descriptors2, _ = superpoint(image2)

# # 将数据转换为SuperGlue格式
# data = {
#     'image1': (image1, points1, descriptors1),
#     'image2': (image2, points2, descriptors2),
# }

# # 运行SuperGlue
# data = {k: (torch.tensor(v[0])[None], torch.tensor(v[1])[None], torch.tensor(v[2])[None]) for k, v in data.items()}
# pred = superglue(data)

# # 绘制匹配结果
# image1_color = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box.png")
# image2_color = cv2.imread(r"C:\Users\17814\Documents\XiaoMiNet\Upupoo\Docker\config\Qt\Graduation\Software\Qt_Ui\images\box_in_scene.png")
# image_matches = plot_matches(image1_color, image2_color, points1, points2, pred['matches'][0], color=(0, 255, 0))

# # 保存匹配结果
# cv2.imwrite('assets/matches.jpg', image_matches)

# imgMatch
    # 获取文件绝对路径
import os
def getResultFilePath(path):
    # 获取当前脚本所在的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 将路径拼接起来
    file_path = os.path.join(script_dir, path)
    # 判断文件是否存在
    if os.path.exists(file_path):
        return file_path
    else:
        # 如果文件不存在，返回当前目录
        return os.path.abspath(script_dir)
# 获取 calibration_params.yml 文件的绝对路径
print(getResultFilePath("calibration_params.yml"))