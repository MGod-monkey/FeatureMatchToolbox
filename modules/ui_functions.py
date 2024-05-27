# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
from PySide6.QtWidgets import QFileDialog, QGraphicsView, QScrollBar
from PySide6.QtGui import QMouseEvent, QWheelEvent, QDesktopServices
from PIL import Image
from matplotlib import pyplot as plt
# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False

class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        # 最大最小化
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("收缩")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/static/icons/shousuo.png"))
            self.ui.frame_size_grip.hide()
            self.ui.imageSArea.resize(1024, 480)
            
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("展开")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/static/icons/zhankai.png"))
            self.ui.frame_size_grip.show()
            self.ui.imageSArea.resize(640, 480)


    # 返回窗口状态
    def returStatus(self):
        return GLOBAL_STATE

    # 设置窗口状态
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status
    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = self.Settings.MENU_WIDTH
            standard = 64

            # SET MAX WIDTH
            if width == 64:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(self.Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()


    # 伸缩菜单选项
    def toggleSetting(self, frame):
        height = frame.height()
        if height == 0:
            last_height = 500
        else:
            last_height = 0
        self.animation = QPropertyAnimation(frame, b"maximumHeight")
        self.animation.setDuration(self.Settings.TIME_ANIMATION)
        self.animation.setStartValue(height)
        self.animation.setEndValue(last_height)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        
    # 伸缩左侧菜单栏
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = self.Settings.LEFT_BOX_WIDTH
            color = self.Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(self.Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # 伸缩右侧设置栏
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = self.Settings.RIGHT_BOX_WIDTH
            color = self.Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(self.Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 300
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 300
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(self.Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(self.Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(self, getStyle):
        select = getStyle + self.Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(self, getStyle):
        deselect = getStyle.replace(self.Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # 选择菜单
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(self, w.styleSheet()))

    # 重置菜单样式
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(self, w.styleSheet()))

    # 导入主题
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore
        self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
        self.ui.rightButtons.setFrameStyle(QFrame.NoFrame)
        if self.Settings.WebCameraIP == "":
            self.ui.setIPLEdit.setPlaceholderText("请输入IP地址")
        else:
            self.ui.setIPLEdit.setPlaceholderText(self.Settings.WebCameraIP)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.screen_width = self.app.primaryScreen().availableGeometry().width()
        self.screen_height = self.app.primaryScreen().availableGeometry().height()

        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus(self):
                UIFunctions.maximize_restore(self)
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.titleRightInfo.mouseMoveEvent = moveWindow
        
        # 实现图片的拖拽理论功能
        self.ui.resultLabel.installEventFilter(self)
        
        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(self.close)

        # 菜单选项按钮
        self.ui.btn_save.clicked.connect(lambda: UIFunctions.toggleSetting(self, self.ui.frame_save))
        self.ui.btn_more.clicked.connect(lambda: UIFunctions.toggleSetting(self, self.ui.frame_more))
        self.ui.btn_adjustments.clicked.connect(lambda: UIFunctions.toggleSetting(self, self.ui.frame_algorithm))

        # 左侧栏菜单按钮事件
        def ShowResultImageExtreWin():
            isChecked = self.ui.CBox_showImageFunction.isChecked()
            if isChecked:
                self.Settings.setConfig("ALGORITHM_OPTION", "ShowResultImageExtreWin", "True")
            else:
                self.Settings.setConfig("ALGORITHM_OPTION", "ShowResultImageExtreWin", "False")

        self.ui.CBox_showImageFunction.clicked.connect(ShowResultImageExtreWin)

        def featureAlgorithmChange(index):
            self.Settings.setConfig("ALGORITHM_OPTION", "FeatureAlgorithm", str(index))
            self.ui.GBox_show.setTitle(self.Settings.getFeatureAlgorithm())
            self.ui.label_featureExtraction.setText(f"特征提取算法：{self.Settings.getFeatureAlgorithm()}")
        self.ui.CBox_feature.activated.connect(lambda index: featureAlgorithmChange(index))

        def setIsImageCover():
            isChecked = self.ui.CBox_suffix.isChecked()
            if isChecked:
                self.Settings.setConfig("IMAGE_SAVE", "ImageCover", "True")
            else:
                self.Settings.setConfig("IMAGE_SAVE", "ImageCover", "False")
        self.ui.CBox_suffix.clicked.connect(setIsImageCover)

        def setImageSavePath(savepath):
            # print(savepath)
            if os.path.exists(r"{}".format(savepath)):
                self.Settings.setConfig("IMAGE_SAVE", "ImageSavePath", savepath)
                self.ui.LEdit_savePath.setPlaceholderText(savepath)
                UIFunctions.showMessageBox(self, "设置图片保存路径成功!", 2)
            else:
                UIFunctions.showMessageBox(self, "打开文件夹错误，请检查路径是否正确(不允许包含中文)!", 1)
            self.ui.LEdit_savePath.clear()
        self.ui.LEdit_savePath.returnPressed.connect(lambda: setImageSavePath(self.ui.LEdit_savePath.text()))

        def selectImageSavePath():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_path = QFileDialog.getExistingDirectory(self, "选择目录")
            if file_path:
                ImageSavePath = file_path
                self.ui.LEdit_savePath.setPlaceholderText(file_path)
                UIFunctions.showMessageBox(self, "设置图片保存路径成功!", 2)
            else:
                UIFunctions.showMessageBox(self, "打开文件夹错误，请检查路径是否正确(不允许包含中文)!", 1)

        self.ui.TButton_savePath.clicked.connect(selectImageSavePath)
        # self.ui.btn_saveOption.clicked.connect(lambda: self.Settings.saveConfig())
        def saveOption():
            self.Settings.saveConfig()
            UIFunctions.showMessageBox(self, "配置保存成功!", 2)
        self.ui.btn_saveOption.clicked.connect(saveOption)
        
        # 输入实际值
        def inputResultValue(self, btn_index):
            if btn_index == 0:
                value, ok = QInputDialog.getDouble(self, "请输入水平偏移角度实际值（单位：°）", "实际值：")
                if ok:
                    self.Settings.setConfig("ERROR_OPTION", "ResultHAngle", str(value))
                    self.ui.LEdit_H.setPlaceholderText(self.Settings.ResultHAngle)
                    label = [self.ui.label1_HError, self.ui.label2_HError, self.ui.label3_HError, self.ui.label4_HError, self.ui.label5_HError]
                    self.Camera.calcError(self, -1, self.Settings.ResultHAngle, self.ui.label_HError, label[int(self.Settings.FeatureAlgorithm)])
                    # self.Settings.saveConfig()
            elif btn_index == 1:
                value, ok = QInputDialog.getDouble(self, "请输入垂直偏移角度实际值（单位：°）", "实际值：")
                if ok:
                    self.Settings.setConfig("ERROR_OPTION", "ResultVAngle", str(value))
                    self.ui.LEdit_V.setPlaceholderText(self.Settings.ResultVAngle)
                    label = [self.ui.label1_VError, self.ui.label2_VError, self.ui.label3_VError, self.ui.label4_VError, self.ui.label5_VError]
                    self.Camera.calcError(self, -2, self.Settings.ResultVAngle, self.ui.label_VError, label[int(self.Settings.FeatureAlgorithm)])
                    # self.Settings.saveConfig()
            elif btn_index == 2:
                value, ok = QInputDialog.getDouble(self, "请输入水平距离实际值（单位：cm）", "实际值：")
                if ok:
                    self.Settings.setConfig("ERROR_OPTION", "ResultDistance", str(value))
                    self.ui.LEdit_D.setPlaceholderText(self.Settings.ResultDistance)
                    self.Camera.calcError(self, -3, self.Settings.ResultDistance, self.ui.label_HDistanceError)
                    # self.Settings.saveConfig()

        # 将QToolButton的clicked信号与on_button_clicked函数相关联
        self.ui.TButton_calcHError.clicked.connect(lambda: inputResultValue(self, 0))
        self.ui.TButton_HError.clicked.connect(lambda: inputResultValue(self, 1))
        self.ui.TButton_HDistanceError.clicked.connect(lambda: inputResultValue(self, 2))
        
        # 读取配置文件并初识化界面
        self.ui.LEdit_H.setPlaceholderText(self.Settings.ResultHAngle)
        self.ui.LEdit_V.setPlaceholderText(self.Settings.ResultVAngle)
        self.ui.LEdit_D.setPlaceholderText(self.Settings.ResultDistance)
        def setMatchDeadline(value):
            self.Settings.setConfig("ALGORITHM_OPTION", "MatchDeadline", str(value))
        self.ui.SBox_matchDeadline.valueChanged.connect(lambda value: setMatchDeadline(value))

        def setMatchRatio(value):
            self.Settings.setConfig("ALGORITHM_OPTION", "MatchRatio", str(value))
            # print(value)
        self.ui.DSBox_matchRatio.valueChanged.connect(lambda value: setMatchRatio(value))

        def editResultValue(value, index):
            if index == 0:
                self.Settings.setConfig("ERROR_OPTION", "ResultHAngle", str(value))
                self.ui.LEdit_H.setPlaceholderText(self.Settings.ResultHAngle)
            elif index == 1:
                self.Settings.setConfig("ERROR_OPTION", "ResultVAngle", str(value))
                self.ui.LEdit_V.setPlaceholderText(self.Settings.ResultVAngle)
            elif index == 2:
                self.Settings.setConfig("ERROR_OPTION", "ResultDistance", str(value))
                self.ui.LEdit_D.setPlaceholderText(self.Settings.ResultDistance)
            UIFunctions.updateError(self)
        self.ui.LEdit_H.returnPressed.connect(lambda: editResultValue(self.ui.LEdit_H.text(), 0))
        self.ui.LEdit_V.returnPressed.connect(lambda: editResultValue(self.ui.LEdit_V.text(), 1))
        self.ui.LEdit_D.returnPressed.connect(lambda: editResultValue(self.ui.LEdit_D.text(), 2))
    
        def setMatchThreshold(value):
            self.Settings.setConfig("ALGORITHM_OPTION", "MatchThreshold", str(value))
        def setKeypointThreshold(value):
            self.Settings.setConfig("ALGORITHM_OPTION", "KeypointThreshold", str(value))
        self.ui.DSBox_matchThreshold.valueChanged.connect(lambda value: setMatchThreshold(value))
        self.ui.DSBox_keypointThreshold.valueChanged.connect(lambda value: setKeypointThreshold(value))
        
        def setShowDoubleImage():
            isChecked = self.ui.CBox_showDoubleImage.isChecked()
            if isChecked:
                msg_box = QMessageBox()
                msg_box.setWindowTitle('确认操作')
                msg_box.setText('打开双目摄像头将会消耗极大的内存和带宽，画面将会有延迟，是否继续？')
                msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg_box.setDefaultButton(QMessageBox.Cancel)
                result = msg_box.exec_()
                if result == QMessageBox.Ok:
                    self.Settings.setConfig("ALGORITHM_OPTION", "ShowDoubleImage", "True")
                    UIFunctions.setCameraWindow(self, True)
            else:
                self.Settings.setConfig("ALGORITHM_OPTION", "ShowDoubleImage", "False")
                UIFunctions.setCameraWindow(self, False)
        self.ui.CBox_showDoubleImage.clicked.connect(setShowDoubleImage)
        UIFunctions.setCameraWindow(self, self.Settings.ShowDoubleImage)
        
        # 左右摄像头浏览器访问
        def visitWebsite(self, index):
            # 打开浏览器并访问网页
            if self.webCameraConnect:
                if not self.openCamera:
                    if index == 0:
                        QDesktopServices.openUrl(QUrl(f"http://{self.Settings.WebCameraIP}:8080/video_feed/{0}?width=640&height=480&quality=90"))
                    else:
                        QDesktopServices.openUrl(QUrl(f"http://{self.Settings.WebCameraIP}:8080/video_feed/{2}?width=640&height=480&quality=90"))
                else:
                    UIFunctions.showMessageBox(self, '请先关闭摄像头！', 1)
            else:
                UIFunctions.showMessageBox(self, '网络摄像头未连接！', 1)
        self.ui.CLinkBtn_Left.clicked.connect(lambda: visitWebsite(self, 0))
        self.ui.CLinkBtn_Right.clicked.connect(lambda: visitWebsite(self, 1))
        
        def setImageSaveCameraIndex(index):
            self.Settings.setConfig("IMAGE_SAVE", "ImageSaveCameraIndex", str(index))
        self.ui.CBox_chooseSaveImage.activated.connect(lambda index: setImageSaveCameraIndex(index))
        
        # 移动置屏幕中央
        window_rect = self.frameGeometry()
        x = (self.screen_width - window_rect.width()) / 2 - 10
        y = (self.screen_height - window_rect.height()) / 2 + 14
        self.move(x, y)
    
    def getResultFilePath(self, path):
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
    # # 获取文件绝对路径
    # def getResultFilePath(self, path):
    #     default_path = os.path.abspath(os.path.join(os.getcwd(), path))
    #     if os.path.exists(default_path) == False:
    #         default_path = os.path.abspath(os.path.join(os.getcwd(), f"./Software/Qt_Ui/{path}"))
    #     if os.path.exists(default_path) == False:
    #         default_path = "./"
    #     return default_path
    # 显示文件选择窗口,返回文件路径 0-选择全局照片文件 1-选择局部照片文件
    def showFileDialog(self, type):
        img = None
        # 判断./images是否存在，不存在则判断./Software/Qt_Ui/images是否存在
        default_path = UIFunctions.getResultFilePath(self, self.Settings.ImageSavePath)
        if type == 0:
            fname, _ = QFileDialog.getOpenFileName(self, '选择全局照片', default_path, 'Image files(*.jpg *.png)')
            if fname != '':
                self.Settings.setConfig("IMAGE_SAVE", "ImageChooseGloadPath", fname)
                img = cv2.imread(fname)
        else:
            fname, _ = QFileDialog.getOpenFileName(self, '选择局部照片', default_path, 'Image files(*.jpg *.png)')
            if fname != '':
                self.Settings.setConfig("IMAGE_SAVE", "ImageChooseLocalPath", fname)
                img = cv2.imread(fname)
        if img is not None:
            print(fname)
            print(img.shape)
            if type == 1:
                self.ui.label_localImgSize.setText(f"局部图片尺寸：{img.shape[1]}x{img.shape[0]}")
            elif type == 0:
                self.ui.label_globalImgSize.setText(f"全局图片尺寸：{img.shape[1]}x{img.shape[0]}")
            UIFunctions.showResultImage(self, img)
        else:
            UIFunctions.showMessageBox(self, "打开图像文件错误，请检查路径是否正确(不允许包含中文)!", 1)
    
    def showResultImage(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        q_img = QPixmap.fromImage(QImage(img.data, img.shape[1], img.shape[0], QImage.Format.Format_RGB888))
        self.ui.resultLabel.setPixmap(q_img)
        self.ui.resultLabel.setFixedSize(img.shape[1], img.shape[0])
    
    # 显示弹窗
    # type: 0-警告 1-错误 2-信息 3-询问
    def showMessageBox(self, text, type, *args):
        msg = QMessageBox(self)
        if type == 0: 
            msg.setWindowTitle('警告')
            msg.setIcon(QMessageBox.Warning)
        elif type == 1: 
            msg.setWindowTitle('错误')
            msg.setIcon(QMessageBox.Critical)
        elif type == 2: 
            msg.setWindowTitle('信息')
            msg.setIcon(QMessageBox.Information)
        elif type == 3:
            msg.setText(text)
            msg.setWindowTitle('询问')
            msg.setIcon(QMessageBox.Information)
            for btn in args:
                msg.addButton(btn, QMessageBox.YesRole)
            msg.exec()
            if not self.Settings.ImageSaveSuccess:
                msg = QMessageBox(self)
                msg.setWindowTitle('错误')
                msg.setIcon(QMessageBox.Critical)
                msg.setText("操作失败！")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
            else:
                msg = QMessageBox(self)
                msg.setWindowTitle('信息')
                msg.setIcon(QMessageBox.Information)
                msg.setText("保存照片成功！")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
            return
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    
    # 伸缩照片窗口
    def toggleCameraLabel(self, width, height):
        if width > 1280 or height > 720:
            width = 1280
            height = 720
        last_width = self.ui.cameraLabel.width()
        last_height = self.ui.cameraLabel.height()
        width_diff = width - last_width
        height_diff = height - last_height
        
        if width_diff == 0 or height_diff == 0:
            return
        
        if width == 1280 and height == 720:
            UIFunctions.maximize_restore(self)
            cameraWidth = self.ui.camera.width()+width_diff-180
            cameraHeight = self.ui.camera.height()+height_diff-100
        else:
            cameraWidth = self.ui.camera.width()+width_diff
            cameraHeight = self.ui.camera.height()+height_diff
            self.resize(self.width()+width_diff, self.height()+height_diff)
            # 移动置屏幕中央
            window_rect = self.frameGeometry()
            x = (self.screen_width - window_rect.width()) / 2 - 10
            y = (self.screen_height - window_rect.height()) / 2 + 14
            self.move(x, y)
        
        self.ui.camera.resize(cameraWidth, cameraHeight)

        # 动画
        self.animation = QPropertyAnimation(self.ui.cameraLabel, b"minimumWidth")
        self.animation.setDuration(self.Settings.TIME_ANIMATION)
        self.animation.setStartValue(last_width)
        self.animation.setEndValue(width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        
        self.animation2 = QPropertyAnimation(self.ui.cameraLabel, b"minimumHeight")
        self.animation2.setDuration(self.Settings.TIME_ANIMATION)
        self.animation2.setStartValue(last_height)
        self.animation2.setEndValue(height)
        self.animation2.setEasingCurve(QEasingCurve.InOutQuart)

        self.animation3 = QPropertyAnimation(self.ui.imageSArea, b"minimumWidth")
        self.animation3.setDuration(self.Settings.TIME_ANIMATION)
        self.animation3.setStartValue(last_width)
        self.animation3.setEndValue(width)
        self.animation3.setEasingCurve(QEasingCurve.InOutQuart)

        self.animation4 = QPropertyAnimation(self.ui.imageSArea, b"minimumWidth")
        self.animation4.setDuration(self.Settings.TIME_ANIMATION)
        self.animation4.setStartValue(last_width)
        self.animation4.setEndValue(width)
        self.animation4.setEasingCurve(QEasingCurve.InOutQuart)
        
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.animation)
        self.group.addAnimation(self.animation2)
        self.group.addAnimation(self.animation3)
        self.group.addAnimation(self.animation4)
        self.group.start()
    # 显示图片
    def showImage(self, imgs):
        if isinstance(imgs, (list, tuple)):
            # 设置交互模式
            plt.ion()

            # 创建一个有两列的子图
            fig, axs = plt.subplots(1, 2)

            # 在第一列中展示第一张图片
            axs[0].imshow(cv2.cvtColor(imgs[0], cv2.COLOR_BGR2RGB))
            axs[0].set_axis_off()
            axs[0].set_title('Local Image')

            # 在第二列中展示第二张图片
            axs[1].imshow(cv2.cvtColor(imgs[1], cv2.COLOR_BGR2RGB))
            axs[1].set_axis_off()
            axs[1].set_title('Global Image')

            # 关闭坐标轴
            axs[0].axis('off')
            axs[1].axis('off')

            # 显示图像
            plt.show(block=True)
            # 等待关闭图像窗口
            # plt.waitforbuttonpress()
            plt.close()
            return
        if self.Settings.ShowResultImageExtreWin:
            # 显示结果图
            plt.ion()
            plt.imshow(cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.title("Match Result")
            plt.show(block=True)  # 阻塞代码执行，直到用户关闭窗口
            plt.close()
            # cv2.imshow('Result', imgs)
            # cv2.waitKey()
            # cv2.destroyAllWindows()
        else:
            UIFunctions.showResultImage(self, imgs)
    
    # 刷新误差值
    def updateError(self):
        result_value = [float(self.Settings.ResultHAngle), float(self.Settings.ResultVAngle), float(self.Settings.ResultDistance)]
        value_labels = [[self.ui.label1_H, self.ui.label1_V, self.ui.label1_D],
                        [self.ui.label2_H, self.ui.label2_V, self.ui.label2_D],
                        [self.ui.label3_H, self.ui.label3_V, self.ui.label3_D],
                        [self.ui.label4_H, self.ui.label4_V, self.ui.label4_D],
                        [self.ui.label5_H, self.ui.label5_V, self.ui.label5_D]]
        error_labels = [[self.ui.label1_HError, self.ui.label1_VError, self.ui.label1_DError],
                  [self.ui.label2_HError, self.ui.label2_VError, self.ui.label2_DError],
                  [self.ui.label3_HError, self.ui.label3_VError, self.ui.label3_DError],
                  [self.ui.label4_HError, self.ui.label4_VError, self.ui.label4_DError],
                  [self.ui.label5_HError, self.ui.label5_VError, self.ui.label5_DError]]
        for i in range(len(value_labels)):
            for j in range(len(value_labels[i])):
                if float(value_labels[i][j].text()) != 0:
                    self.Camera.calcError(self, float(value_labels[i][j].text()), result_value[j], error_labels[i][j])

    
    # 设置相机窗口尺寸
    def setCameraWindow(self, enable):
        if enable:
            width = 1280
        else:
            width = 640
        start_width = self.ui.cameraLabel.width()
        self.animation = QPropertyAnimation(self.ui.cameraLabel, b"minimumWidth")
        self.animation.setDuration(self.Settings.TIME_ANIMATION)
        self.animation.setStartValue(start_width)
        self.animation.setEndValue(width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        
        self.animation.start()
    # def resize_grips(self):
    #     if self.Settings.ENABLE_CUSTOM_TITLE_BAR:
    #         self.left_grip.setGeometry(0, 10, 10, self.height())
    #         self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
    #         self.top_grip.setGeometry(0, 0, self.width(), 10)
    #         self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)
