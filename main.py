import sys
import os
import platform
import cv2
import matplotlib
matplotlib.use('TKAgg')
# ///////////////////////////////////////////////////////////////
from modules import *
# os.environ["QT_FONT_DPI"] = "96"

# SET AS GLOBAL self.ui
# ///////////////////////////////////////////////////////////////

class MainWindow(QMainWindow):
    def __init__(self, app):
        global stop_event
        QMainWindow.__init__(self)

        # UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.app = app
        
        # 配置初识化
        self.Settings = Settings(self)
        
        # 摄像头
        self.Camera = Camera.init_camera(self)

        # APP初识化
        title = "Smart Camera"
        description = "Smart Camera"
        self.setWindowTitle(title)
        self.ui.titleRightInfo.setText(description)
        
        # # UPS系统线程
        # # 创建并启动Flask服务器线程
        # self.stop_event = threading.Event()
        # self.flask_server_thread = threading.Thread(target=run_flask_server, args=(self.ups, self.stop_event))
        # self.flask_server_thread.start()
        # Flask线程的启动
        self.ups = UPS(self)
        self.flask_thread = FlaskThread(self, self.ups)
        self.flask_thread.start()

        # TOGGLE MENU
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # 界面初识化
        UIFunctions.uiDefinitions(self)

        # 按键点击事件
        self.ui.btn_camera.clicked.connect(self.menuBtnClick)
        self.ui.btn_image.clicked.connect(self.menuBtnClick)
        self.ui.btn_liucheng.clicked.connect(self.menuBtnClick)
        self.ui.btn_statistic.clicked.connect(self.menuBtnClick)
        self.ui.btn_exit.clicked.connect(self.menuBtnClick)
        self.ui.cameraBtn.clicked.connect(lambda: Camera.openClosecamera(self))
        self.ui.changeCameraBtn.clicked.connect(lambda: Camera.changeCamera(self))
        self.ui.shutterBtn.clicked.connect(lambda: Camera.shutter(self))
        self.ui.setIPBtn.clicked.connect(lambda: Camera.setIP(self, self.ui.setIPLEdit.text()))
        self.ui.matchImageBtn.clicked.connect(lambda: Camera.matchStep(self, step=3))
        self.ui.angleImageBtn.clicked.connect(lambda: Camera.matchStep(self, step=4))
        self.ui.calcHDistanceBtn.clicked.connect(lambda: Camera.matchStep(self, step=5))
        self.ui.btn_runStep.clicked.connect(lambda: Camera.matchStep(self, showLiucheng=True))
        self.ui.btn_runStep1.clicked.connect(lambda: Camera.matchStep(self, index=0))
        self.ui.btn_runStep2.clicked.connect(lambda: Camera.matchStep(self, index=1))
        self.ui.btn_runStep3.clicked.connect(lambda: Camera.matchStep(self, index=2))
        self.ui.btn_runStep4.clicked.connect(lambda: Camera.matchStep(self, index=3))
        self.ui.btn_runStep5.clicked.connect(lambda: Camera.matchStep(self, index=4))
        def cameraBiaoding(self):
            text, ok = QInputDialog.getMultiLineText(self, '输入标定的参考规格', r'请输入棋盘的尺寸,最小参考图片数量和每个方格的实际尺寸(单位:cm),一行输入一个数据,如9\n6\n50\n23.3:')
            if ok:
                if text == '':
                    text = '9\n6\n50\n23.3'
                inputs = text.strip().split('\n')
                if len(inputs) == 4:
                    try:
                        int1 = int(inputs[0])
                        int2 = int(inputs[1])
                        int3 = int(inputs[2])
                        float1 = float(inputs[3])
                        print(f"\r标定的规格：棋盘{int1}x{int2}\n\r最小参考图片数量{int3}\n\r每个方格的实际尺寸：{float1}cm")
                        Camera.biaoding(self, int1, int2, int3, float1)
                    except ValueError:
                        UIFunctions.showMessageBox(self, "无法解析数字，请重试！", 1)
                else:
                    UIFunctions.showMessageBox(self, "输入的数字不合规范！", 1)
        self.ui.btn_biaoding.clicked.connect(lambda: cameraBiaoding(self))
        
        # 绑定实时匹配按钮
        def videoMatchBtnClicked(self):
            if self.openCamera:
                self.Camera.openClosecamera(self)
            if self.Settings.ImageChooseLocalPath != '':
                if self.webCameraConnect:
                    videoMatch(self.Settings.ImageChooseLocalPath, self.Settings.WebCameraIP)
                else:
                    videoMatch(self.Settings.ImageChooseLocalPath)
            else:
                videoMatch()
        self.ui.videoMatchBtn.clicked.connect(lambda: videoMatchBtnClicked(self))
        
        # 改变分辨率
        def changeResolution(index):
            Camera.changeResolution(self, index)
        self.ui.resolutionBox.currentIndexChanged.connect(changeResolution)

        # 左侧栏伸缩
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        self.ui.toggleLeftBox.clicked.connect(openCloseLeftBox)
        self.ui.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # 右侧栏伸缩
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        self.ui.settingsTopBtn.clicked.connect(openCloseRightBox)
        
        # 设置主页
        self.ui.stackedWidget.setCurrentWidget(self.ui.camera)
        self.ui.btn_camera.setStyleSheet(UIFunctions.selectMenu(self, self.ui.btn_camera.styleSheet()))
        
        self.show()


    # 菜单按钮点击事件
    def menuBtnClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        # 摄像头APP
        if btnName == "btn_camera":
            self.ui.stackedWidget.setCurrentWidget(self.ui.camera)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))

        # 图片APP
        if btnName == "btn_image":
            self.ui.stackedWidget.setCurrentWidget(self.ui.images)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))
        
        # 流程APP
        if btnName == "btn_liucheng":
            self.ui.stackedWidget.setCurrentWidget(self.ui.liucheng)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))
        
        # 统计APP
        if btnName == "btn_statistic":
            self.ui.stackedWidget.setCurrentWidget(self.ui.statistic)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))
        
        # 退出APP
        if btnName == "btn_exit":
            # sys.exit()
            self.close()
    

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    # def resizeEvent(self, event):
    #     # Update Size Grips
    #     UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # if event.buttons() == Qt.MouseButton.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.MouseButton.RightButton:
        #     print('Mouse click: RIGHT CLICK')
    
    # 图片拖动事件
    def eventFilter(self, obj, event):
        if event.type() == QMouseEvent.MouseButtonPress:
            # 报错上次鼠标位置
            self.last_mouse_pos = event.position()
        elif event.type() == QMouseEvent.MouseButtonRelease:
            # 清除鼠标位置
            self.last_mouse_pos = None
        elif event.type() == QMouseEvent.MouseMove and self.last_mouse_pos is not None:
            # 计算移动距离
            delta = self.last_mouse_pos - event.position()
            self.ui.imageSArea.verticalScrollBar().setValue(self.ui.imageSArea.verticalScrollBar().value() + delta.y())
            self.ui.imageSArea.horizontalScrollBar().setValue(self.ui.imageSArea.horizontalScrollBar().value() + delta.x())

        return super().eventFilter(obj, event)
    # def closeEvent(self, event):
    #     self.stop_event.set()
    #     event.accept()
    def update_frame(self, _):
        if not self.frame_update_thread.buffer.empty():
            frame = self.frame_update_thread.buffer.get()
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format.Format_RGB888)
            self.ui.cameraLabel.setPixmap(QPixmap.fromImage(image.rgbSwapped()))
    
    def camera_closed_slot(self):
        self.ui.cameraLabel.clear()
        self.ui.cameraLabel.setText('请打开摄像头')
    
    def closeEvent(self, event):
        self.flask_thread.stop()  # 停止Flask线程
        self.flask_thread.wait()
        event.accept()
    
if __name__ == "__main__":
    plt.switch_backend('TKAgg')
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./icon.ico"))
    window = MainWindow(app)
    sys.exit(int(app.exec()))