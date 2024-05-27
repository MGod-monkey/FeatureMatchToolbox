import os
import configparser
from main import *


class Settings(MainWindow):
    def __init__(self, MainWindow):
        self.ui = MainWindow.ui
        self.config = configparser.ConfigParser()
        # 判断./Settings.ini是否存在，不存在则判断./Software/Qt_Ui/Settings.ini是否存在
        self.config_path = os.path.abspath(os.path.join(os.getcwd(), "./Settings.ini"))
        if os.path.exists(self.config_path) == False:
            self.config_path = os.path.abspath(os.path.join(os.getcwd(), "./Software/Qt_Ui/Settings.ini"))
        if os.path.exists(self.config_path) == False:
            print(f"{self.config_path} is not exist")
        else:
            self.config.read(self.config_path)

        # APP SETTINGS
        # ///////////////////////////////////////////////////////////////
        self.ENABLE_CUSTOM_TITLE_BAR = eval(self.config.get('APP_SETTINGS', 'ENABLE_CUSTOM_TITLE_BAR'))
        self.MENU_WIDTH = int(self.config.get('APP_SETTINGS', 'MENU_WIDTH'))
        self.LEFT_BOX_WIDTH = int(self.config.get('APP_SETTINGS', 'LEFT_BOX_WIDTH'))
        self.RIGHT_BOX_WIDTH = int(self.config.get('APP_SETTINGS', 'RIGHT_BOX_WIDTH'))
        self.TIME_ANIMATION = int(self.config.get('APP_SETTINGS', 'TIME_ANIMATION'))

        # BTNS LEFT AND RIGHT BOX COLORS
        self.BTN_LEFT_BOX_COLOR = self.config.get('APP_SETTINGS', 'BTN_LEFT_BOX_COLOR').replace('"', '')
        self.BTN_RIGHT_BOX_COLOR = self.config.get('APP_SETTINGS', 'BTN_RIGHT_BOX_COLOR').replace('"', '')

        # MENU SELECTED STYLESHEET
        self.MENU_SELECTED_STYLESHEET = self.config.get('APP_SETTINGS', 'MENU_SELECTED_STYLESHEET').replace('"', '')
        
        # 摄像头方面
        self.WebCameraIP = self.config.get('WEBCAMERA', 'WebCameraIP')
        if not self.WebCameraIP:
            self.WebCameraIP = ""

        self.WebCameraResolution = self.config.get('WEBCAMERA', 'WebCameraResolution').replace('"', '')
        self.WebCameraResolutionNum = int(self.config.get('WEBCAMERA', 'WebCameraResolutionNum'))
        self.WebCameraRefreshRate = int(self.config.get('WEBCAMERA', 'WebCameraRefreshRate'))
        self.WebCameraCalibrationParametersPath = self.config.get('WEBCAMERA', 'WebCameraCalibrationParametersPath')
        if not self.WebCameraCalibrationParametersPath:
            self.WebCameraCalibrationParametersPath = "./"

        # 图像保存
        self.ImageSaveSuccess = eval(self.config.get('IMAGE_SAVE', 'ImageSaveSuccess'))
        self.ImageSavePath = self.config.get('IMAGE_SAVE', 'ImageSavePath').replace('"', '')
        self.ImageCover = eval(self.config.get('IMAGE_SAVE', 'ImageCover'))
        self.ImageChooseGloadPath = self.config.get('IMAGE_SAVE', 'ImageChooseGloadPath').replace('"', '')
        self.ImageSaveCameraIndex = int(self.config.get('IMAGE_SAVE', 'ImageSaveCameraIndex'))
        if not self.ImageChooseGloadPath:
            self.ImageChooseGloadPath = ""
        self.ImageChooseLocalPath = self.config.get('IMAGE_SAVE', 'ImageChooseLocalPath').replace('"', '')
        if not self.ImageChooseLocalPath:
            self.ImageChooseLocalPath = ""

        # 算法选项
        self.FeatureAlgorithm = int(self.config.get('ALGORITHM_OPTION', 'FeatureAlgorithm'))    # 特征提取算法，0：SIFT算法 1：SURF算法 2：ORB算法
        self.MatchRatio  = float(self.config.get('ALGORITHM_OPTION', 'MatchRatio'))       # 匹配率值
        self.MatchDeadline = int(self.config.get('ALGORITHM_OPTION', 'MatchDeadline'))      # 认定为匹配的最低匹配点数
        self.KeypointThreshold = float(self.config.get('ALGORITHM_OPTION', 'KeypointThreshold'))
        self.MatchThreshold = float(self.config.get('ALGORITHM_OPTION', 'MatchThreshold'))
        self.ShowResultImageExtreWin = eval(self.config.get('ALGORITHM_OPTION', 'ShowResultImageExtreWin'))
        self.ShowDoubleImage = eval(self.config.get('ALGORITHM_OPTION', 'ShowDoubleImage'))
        
        # 误差值
        self.ErrorAngle = int(self.config.get('ERROR_OPTION', 'ErrorAngle')) # 误差计算的角度（合格偏移角度=+/-误差角*最大误差值）
        self.MaxErrorValue = float(self.config.get('ERROR_OPTION', 'MaxErrorValue')) # 最大误差值
        self.ResultHAngle = self.config.get('ERROR_OPTION', 'ResultHAngle') # 实际水平角度
        self.ResultVAngle = self.config.get('ERROR_OPTION', 'ResultVAngle') # 实际垂直角度
        self.ResultDistance = self.config.get('ERROR_OPTION', 'ResultDistance') # 实际距离 

        self.initUIConfig()

    def initUIConfig(self):
        self.ui.CBox_suffix.setChecked(self.ImageCover)
        self.ui.CBox_feature.setCurrentIndex(self.FeatureAlgorithm)
        self.ui.DSBox_matchRatio.setValue(self.MatchRatio)
        self.ui.SBox_matchDeadline.setValue(self.MatchDeadline)
        self.ui.CBox_showImageFunction.setChecked(self.ShowResultImageExtreWin)
        self.ui.LEdit_savePath.setPlaceholderText(self.ImageSavePath)
        self.ui.CBox_chooseSaveImage.setCurrentIndex(self.ImageSaveCameraIndex)
        if self.ImageChooseGloadPath != '' and self.ImageChooseLocalPath != '':
            img_global = cv2.imread(self.ImageChooseGloadPath)
            img_local = cv2.imread(self.ImageChooseLocalPath)
            self.ui.label_localImgSize.setText(f"局部图片尺寸：{img_local.shape[1]}x{img_local.shape[0]}")
            self.ui.label_globalImgSize.setText(f"全局图片尺寸：{img_global.shape[1]}x{img_global.shape[0]}")
        self.ui.label_featureExtraction.setText(f"特征提取算法：{self.getFeatureAlgorithm()}")
        self.ui.GBox_show.setTitle(f"{self.getFeatureAlgorithm()}流程")
        self.ui.SBox_matchDeadline.setValue(self.MatchDeadline)
        self.ui.DSBox_matchRatio.setValue(self.MatchRatio)
        self.ui.DSBox_matchThreshold.setValue(self.MatchThreshold)
        self.ui.DSBox_keypointThreshold.setValue(self.KeypointThreshold)
        self.ui.CBox_showDoubleImage.setChecked(self.ShowDoubleImage)
    
    # 获取特征提取算法
    def getFeatureAlgorithm(self):
        featureAlgorithm = ["SIFT算法", "SURF算法", "ORB算法", "AKAZE算法", "SuperGlue算法(深度学习)"]
        return featureAlgorithm[int(self.FeatureAlgorithm)]
    # 设置配置   
    def setConfig(self, section, option, value):
        # option是个字符串，根据option设置self的成员名字为跟option的值一样的成员的值为value
        setattr(self, option, value)
        self.config.set(section, option, value)
    # 读取配置
    def getConfig(self, section, option):
        return self.config.get(section, option)
    # 保存配置   
    def saveConfig(self):
        with open(self.config_path, 'w') as f:
            self.config.write(f)
        


        

