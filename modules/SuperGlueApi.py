from pathlib import Path
import cv2
import matplotlib.cm as cm
import torch
from . models.matching import Matching
from . models.utils import (AverageTimer, VideoStreamer,
                          make_matching_plot_fast, frame2tensor,compute_pose_error, compute_epipolar_error,
                          estimate_pose, make_matching_plot,
                          error_colormap, AverageTimer, pose_auc, read_image,
                          rotate_intrinsics, rotate_pose_inplane,
                          scale_intrinsics)
import numpy as np
# from . models.superglue import *
# from . models.superpoint import *
torch.set_grad_enabled(False)


def videoMatch(local_image_path=None, camera_index='0', resize = (640, 480), showExtreWin=True, opt=None):
    #(input='0', output_dir=None, image_glob=['*.png', '*.jpg', '*.jpeg'], 
    # skip=1, max_length=1000000, resize=[640, 480], superglue='indoor', max_keypoints=-1,
    # keypoint_threshold=0.005, nms_radius=4, sinkhorn_iterations=20, match_threshold=0.2, show_keypoints=False, 
    # no_display=False, force_cpu=False)    
    if opt is None:
        opt = {
            'nms_radius': 4,
            'keypoint_threshold': 0.006,
            'max_keypoints': -1,
            'superglue': 'indoor',
            'sinkhorn_iterations': 20,
            'match_threshold': 0.28,
            'show_keypoints': False,
        }

    device = 'cuda' if torch.cuda.is_available() and not False else 'cpu'
    print('Running inference on device \"{}\"'.format(device))
    config = {
        'superpoint': {
            'nms_radius': opt['nms_radius'],
            'keypoint_threshold': opt['keypoint_threshold'],
            'max_keypoints': opt['max_keypoints'],
        },
        'superglue': {
            'weights': opt['superglue'],
            'sinkhorn_iterations': opt['sinkhorn_iterations'],
            'match_threshold': opt['match_threshold'],
        }
    }
    matching = Matching(config).eval().to(device)
    keys = ['keypoints', 'scores', 'descriptors']
    # if camera_index == '0':
    #     # vs = cv2.VideoCapture(int(camera_index))
    #     # if vs.isOpened():
    #     #     vs = cv2.VideoCapture(0)
    #     vs = VideoStreamer(camera_index, resize, 1,
    #                     ['*.png', '*.jpg', '*.jpeg'], 1000000)
    #     local_image, ret = vs.next_frame()
    #     if not ret:
    #         vs = VideoStreamer('0', resize, 1,
    #                         ['*.png', '*.jpg', '*.jpeg'], 1000000)
    # else:
    #     # vs = cv2.VideoCapture(f'http://{camera_index}:8080/video_feed/0?width=640&height=480&quality=90')
    #     # if vs.isOpened():
    #     #     vs = cv2.VideoCapture(0)
    #     vs = VideoStreamer(f'http://{camera_index}:8080/video_feed/2', 1,
    #                     ['*.png', '*.jpg', '*.jpeg'], 1000000)
    # 如果没有传入图片则默认以第一帧为参考帧
    # if local_image_path is None:
    #     local_image, ret = vs.next_frame()
    #     # ret, local_image = vs.read()
    #     assert ret, 'ERROR：读取摄像头错误！！'
    # else:
    local_image = cv2.imread(r'C:\Users\17814\Desktop\Qt_Ui\modules\SuperGluePretrainedNetwork\test.jpg')
    local_image = cv2.resize(local_image, resize, interpolation=cv2.INTER_AREA)
    local_image = cv2.cvtColor(local_image, cv2.COLOR_RGB2GRAY)
    # 转换为张量
    frame_tensor = frame2tensor(local_image, device)
    last_data = matching.superpoint({'image': frame_tensor})
    last_data = {k+'0': last_data[k] for k in keys}
    last_data['image0'] = frame_tensor
    last_frame = local_image
    last_image_id = 0

    # if opt.output_dir is not None:
    #     print('==> Will write outputs to {}'.format(opt.output_dir))
    #     Path(opt.output_dir).mkdir(exist_ok=True)

    # # Create a window to display the demo.
    # if showExtreWin:
    #     cv2.namedWindow('Smart matches', cv2.WINDOW_NORMAL)
    #     cv2.resizeWindow('Smart matches', 640*2, 480)

    # Print the keyboard help menu.
    print('==> Keyboard control:\n'
            '\tn: 选择当前帧作为锚 \n'
            '\te/r: 增大/减小关键点置信度阈值 \n'
            '\td/f: 增加/减少匹配过滤阈值 \n'
            '\tk: 切换关键点的可视化 \n'
            '\tq: 退出')

    timer = AverageTimer()
    vs = VideoStreamer(r'C:\Users\17814\Desktop\Qt_Ui\modules\SuperGluePretrainedNetwork\test.mp4', resize, 1,
                    ['.mp4'], 1000000)
    while True:
        frame, ret = vs.next_frame()
        # ret, frame = vs.read()
        if not ret:
            # print('Finished demo_superglue.py')
            break
        # 其他代码...
        timer.update('data')
        stem0, stem1 = last_image_id, vs.i - 1

        frame_tensor = frame2tensor(frame, device)
        pred = matching({**last_data, 'image1': frame_tensor})
        kpts0 = last_data['keypoints0'][0].cpu().numpy()
        kpts1 = pred['keypoints1'][0].cpu().numpy()
        matches = pred['matches0'][0].cpu().numpy()
        confidence = pred['matching_scores0'][0].cpu().numpy()
        timer.update('forward')

        # 设置阈值
        match_threshold = 0.8

        # 过滤低于阈值的匹配点
        # valid = (matches > -1) & (confidence > match_threshold)
        valid = matches > -1
        mkpts0 = kpts0[valid]
        mkpts1 = kpts1[matches[valid]]
        color = cm.jet(confidence[valid])
        text = [
            'SuperGlue',
            'Keypoints: {}:{}'.format(len(kpts0), len(kpts1)),
            'Matches: {}'.format(len(mkpts0))
        ]
        k_thresh = matching.superpoint.config['keypoint_threshold']
        m_thresh = matching.superglue.config['match_threshold']
        small_text = [
            'Keypoint Threshold: {:.4f}'.format(k_thresh),
            'Match Threshold: {:.2f}'.format(m_thresh),
            'Image Pair: {:06}:{:06}'.format(stem0, stem1),
        ]

        # 检查匹配的关键点数量是否大于等于4
        if len(mkpts0) >= 4 and len(mkpts1) >= 4:
            # 计算单应性矩阵
            M, mask = cv2.findHomography(mkpts0, mkpts1, cv2.RANSAC, 5.0)
            # 获取局部图像的高度和宽度
            h, w = local_image.shape[:2]
            # 计算局部图像四个角点在全局图像中对应的位置
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, M)
            # 在全局图像上绘制匹配区域边框
            frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)
            # 计算偏移角以及直线距离
            avg_dst = np.mean(dst, axis=0)
            center_pt = np.float32([w / 2, h / 2]).reshape(-1, 1, 2)
            center_dst = cv2.perspectiveTransform(center_pt, M)
            dx = center_dst[0, 0, 0] - avg_dst[0, 0]
            dy = center_dst[0, 0, 1] - avg_dst[0, 1]
            horizontal_angle = 180 + np.arctan2(dy, dx) * 180 / np.pi
            vertical_angle = 180 + np.arctan2(dx, dy) * 180 / np.pi
            distance = np.sqrt(dx**2 + dy**2) * 10
            # print("水平偏移角: {:.2f}°".format(horizontal_angle))
            # print("垂直偏移角: {:.2f}°".format(vertical_angle))
            # print("直线距离: {:.2f} 像素".format(distance))
            text.append("Horizontal offset angle: {:.2f}d".format(horizontal_angle))
            text.append("Vertical offset angle: {:.2f}d".format(vertical_angle))
            text.append("Straight line distance: {:.2f}px".format(distance))
            text.append("is Match: Match")
        else:
            text.append("is Match: No Match")      

        out = make_matching_plot_fast(
            local_image, frame, kpts0, kpts1, mkpts0, mkpts1, color, text,
            path=None, show_keypoints=opt['show_keypoints'], small_text=small_text)

        if showExtreWin:
            cv2.imshow('SuperGlue matches', out)
        
        key = chr(cv2.waitKey(1) & 0xFF)
        if key == 'q':
            vs.cleanup()
            # print('Exiting (via q) demo_superglue.py')
            break
        elif key == 'n':
            last_data = {k+'0': pred[k+'1'] for k in keys}
            last_data['image0'] = frame_tensor
            local_image = frame
            last_image_id = (vs.i - 1)
        elif key in ['e', 'r']:
            d = 0.1 * (-1 if key == 'e' else 1)
            matching.superpoint.config['keypoint_threshold'] = min(max(
                0.0001, matching.superpoint.config['keypoint_threshold']*(1+d)), 1)
            print('\nChanged the keypoint threshold to {:.4f}'.format(
                matching.superpoint.config['keypoint_threshold']))
        elif key in ['d', 'f']:
            d = 0.05 * (-1 if key == 'd' else 1)
            matching.superglue.config['match_threshold'] = min(max(
                0.05, matching.superglue.config['match_threshold']+d), .95)
            print('\nChanged the match threshold to {:.2f}'.format(
                matching.superglue.config['match_threshold']))
        elif key == 'k':
            opt['show_keypoints'] = not opt['show_keypoints']

        timer.update('viz')
        timer.print()

        # if opt.output_dir is not None:
        #     #stem = 'matches_{:06}_{:06}'.format(last_image_id, vs.i-1)
        #     stem = 'matches_{:06}_{:06}'.format(stem0, stem1)
        #     out_file = str(Path(opt.output_dir, stem + '.png'))
        #     print('\nWriting image to {}'.format(out_file))
        #     cv2.imwrite(out_file, out)

    cv2.destroyAllWindows()
    vs.cleanup()

def imgMatch(local_img_path, global_img_path, showResult=False, **kwargs):
    opt = {
        'resize': (640, 480),
        'nms_radius': 4,
        'keypoint_threshold': 0.006,
        'max_keypoints': 1024,
        'superglue': 'indoor',
        'sinkhorn_iterations': 20,
        'match_threshold': 0.28,
        'show_keypoints': True,
        'fast_viz': True,
        'opencv_display': True
    }
    opt.update(kwargs)

    # 导入模型
    device = 'cuda' if torch.cuda.is_available() and not False else 'cpu'
    print('Running inference on device \"{}\"'.format(device))
    config = {
        'superpoint': {
            'nms_radius': opt['nms_radius'],
            'keypoint_threshold': opt['keypoint_threshold'],
            'max_keypoints': opt['max_keypoints']
        },
        'superglue': {
            'weights': opt['superglue'],
            'sinkhorn_iterations': opt['sinkhorn_iterations'],
            'match_threshold': opt['match_threshold'],
        }
    }
    matching = Matching(config).eval().to(device)

    timer = AverageTimer(newline=True)

    # 导入图像
    image0, inp0, scales0 = read_image(
        r'{}'.format(local_img_path), device, opt['resize'], 0, False)
    image1, inp1, scales1 = read_image(
        r'{}'.format(global_img_path), device, opt['resize'], 0, False)
    if image0 is None or image1 is None:
        print('Problem reading image pair: {} {}'.format(
            input_dir/name0, input_dir/name1))
        return
    timer.update('load_image')

    # Perform the matching.
    pred = matching({'image0': inp0, 'image1': inp1})
    pred = {k: v[0].cpu().numpy() for k, v in pred.items()}
    kpts0, kpts1 = pred['keypoints0'], pred['keypoints1']
    matches, conf = pred['matches0'], pred['matching_scores0']
    timer.update('matcher')

    # Write the matches to disk.
    out_matches = {'keypoints0': kpts0, 'keypoints1': kpts1,
                    'matches': matches, 'match_confidence': conf}

    # Keep the matching keypoints.
    valid = matches > -1
    mkpts0 = kpts0[valid]
    mkpts1 = kpts1[matches[valid]]
    mconf = conf[valid]

    # Visualize the matches.
    color = cm.jet(mconf)
    text = [
        'SuperGlue',
        'Keypoints: {}:{}'.format(len(kpts0), len(kpts1)),
        'Matches: {}'.format(len(mkpts0)),
    ]

    # 显示结果图
    k_thresh = matching.superpoint.config['keypoint_threshold']
    m_thresh = matching.superglue.config['match_threshold']
    small_text = [
        'Keypoint Threshold: {:.4f}'.format(k_thresh),
        'Match Threshold: {:.2f}'.format(m_thresh),
    ]
    timer.update('clac_result')
    
    if len(mkpts0) >= 4 and len(mkpts1) >= 4:
        # 计算单应性矩阵
        M, mask = cv2.findHomography(mkpts0, mkpts1, cv2.RANSAC, 5.0)
        # 获取局部图像的高度和宽度
        h, w = image0.shape[:2]
        # 计算局部图像四个角点在全局图像中对应的位置
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)
        # 在全局图像上绘制匹配区域边框
        image1 = cv2.polylines(image1, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)
        # 计算偏移角以及直线距离
        avg_dst = np.mean(dst, axis=0)
        center_pt = np.float32([w / 2, h / 2]).reshape(-1, 1, 2)
        center_dst = cv2.perspectiveTransform(center_pt, M)
        dx = center_dst[0, 0, 0] - avg_dst[0, 0]
        dy = center_dst[0, 0, 1] - avg_dst[0, 1]
        horizontal_angle = 180 + np.arctan2(dy, dx) * 180 / np.pi
        vertical_angle = 180 + np.arctan2(dx, dy) * 180 / np.pi
        distance = np.sqrt(dx**2 + dy**2) * 10
        # print("水平偏移角: {:.2f}°".format(horizontal_angle))
        # print("垂直偏移角: {:.2f}°".format(vertical_angle))
        # print("直线距离: {:.2f} 像素".format(distance))
        text.append("Horizontal offset angle: {:.2f}d".format(horizontal_angle))
        text.append("Vertical offset angle: {:.2f}d".format(vertical_angle))
        text.append("Straight line distance: {:.2f}px".format(distance))
    else:
        image1 = image1.copy()
    total_time = timer.get_total_time()
    out_img = make_matching_plot_fast(
        image0, image1, kpts0, kpts1, mkpts0, mkpts1, color, text,
        path=None, show_keypoints=opt['show_keypoints'], small_text=small_text)
    if showResult:
        # # 显示匹配结果
        cv2.imshow("Match Result", out_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    timer.print()

    return mkpts0, kpts0, 53.5, 36, 199, total_time, out_img