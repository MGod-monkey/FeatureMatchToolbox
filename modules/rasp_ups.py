# from main import *
# import atexit
# import threading
# from functools import partial
# from flask import Flask, request
# from PySide6.QtCore import QObject, Signal
# from werkzeug.serving import make_server
# from json import loads
# app = Flask(__name__)


# class UPS(QObject):
#     data_received = Signal(str)

#     def __init__(self, parent):
#         super().__init__()
#         self.parent = parent
#         # self.lcd_battery = lcd_battery
#         # self.label_batteryVoltage = label_batteryVoltage
#         # self.label_chargeStatus = label_chargeStatus
#         # self.label_inputVoltage = label_inputVoltage
#         # self.label_timeRemaining = label_timeRemaining
#         self.data_received.connect(self.update_label)

#         receive_data_func = partial(self.receive_data)
#         receive_data_func.__name__ = 'receive_data'
#         app.route('/data', methods=['POST'])(receive_data_func)

#     def receive_data(self):
#         data = request.get_data().decode('utf-8')
#         sender_ip = request.remote_addr  # 获取发送端的IP地址
#         if sender_ip !=  self.parent.Settings.WebCameraIP:
#             self.parent.Settings.setConfig('WEBCAMERA', 'WebCameraIP', sender_ip)
#         self.data_received.emit(data)
#         return "OK"

#     def update_label(self, data):
#         data = loads(data)
#         self.parent.ui.lcd_battery.display(data['BatteryPercentage'])
#         self.parent.ui.label_batteryVoltage.setText("{:.1f}V".format(data['BatteryVoltage']))
#         self.parent.ui.label_chargeStatus.setText(data['ChargeStatus'])
#         self.parent.ui.label_inputVoltage.setText("{:.1f}V".format(data['InputVoltage']))
#         self.parent.ui.label_timeRemaining.setText("{}m".format(data['TimeRemaining']))

# def run_flask_server(receiver, stop_event):  
#     def shutdown_server():
#         stop_event.set()

#     atexit.register(shutdown_server)

#     server = make_server('0.0.0.0', 5000, app)
#     while not stop_event.is_set():
#         try:
#             server.handle_request()
#         except Exception as e:
#             if not stop_event.is_set():
#                 print(f"Error in Flask server: {e}")
from main import *
import PySide6.QtCore as QtCore
from PySide6.QtCore import QThread, QObject, Signal
from flask import Flask, request
from PySide6.QtNetwork import QTcpServer, QTcpSocket
from json import loads
from werkzeug.serving import make_server

class UPS(QObject):
    data_received = Signal(str)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.data_received.connect(self.update_label)

    def receive_data(self, data):
        sender_ip = request.remote_addr  # 获取发送端的IP地址
        if sender_ip != self.parent.Settings.WebCameraIP:
            self.parent.Settings.setConfig('WEBCAMERA', 'WebCameraIP', sender_ip)
        self.data_received.emit(data)

    def update_label(self, data):
        data = loads(data)
        self.parent.ui.lcd_battery.display(data['BatteryPercentage'])
        self.parent.ui.label_batteryVoltage.setText("{:.1f}V".format(data['BatteryVoltage']))
        self.parent.ui.label_chargeStatus.setText(data['ChargeStatus'])
        self.parent.ui.label_inputVoltage.setText("{:.1f}V".format(data['InputVoltage']))
        self.parent.ui.label_timeRemaining.setText("{}m".format(data['TimeRemaining']))

class FlaskThread(QThread):
    def __init__(self, parent, ups, debug=False):
        super().__init__()
        self.parent = parent
        self.ups = ups
        self.debug = debug
        self.flask_app = Flask(__name__)
        self.flask_server = None

        if not self.debug:
            import logging
            log = logging.getLogger('werkzeug')
            log.setLevel(logging.ERROR)

    def run(self):
        self.ups = UPS(self.parent)

        @self.flask_app.route('/data', methods=['POST'])
        def receive_data():
            data = request.get_data().decode('utf-8')
            self.ups.receive_data(data)
            return "OK"

        self.flask_server = make_server('0.0.0.0', 5000, self.flask_app)
        self.flask_server.serve_forever()

    def stop(self):
        if self.flask_server is not None:
            self.flask_server.shutdown()