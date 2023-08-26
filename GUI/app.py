import sys
import numpy as np
import os
import utils

from PySide6.QtCore import Qt, QThreadPool, QTimer
from PySide6.QtGui import QImage, QPixmap, QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
)

from MainWindow import Ui_MainWindow

## import custom functions
import args
from time_thread import TimerThread
from video_capture_thread import VideoFeedThread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        # set variables
        self.file_selected = False
        self.no_time_limit = False

        # start button
        self.start_btn.clicked.connect(self.start_btn_click)
        
        # stop button
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.stop_btn_click)

        # close button
        self.close_btn.clicked.connect(self.close_app)

        # brownse button
        self.browse_btn.clicked.connect(self.browse_files)

        self.threadpool = QThreadPool()

    def close_app(self):
        self.close()  # Close the main window and the entire app

    def start_process(self):

        # get time limit
        time_value = self.set_time_spinbox.value()
        time_unit = self.time_unit_combobox.currentText()

        if (self.file_selected==True) and (time_value==0):  # process file without time limit
            self.no_time_limit = True

        if time_value == 0 and (not self.no_time_limit):
            warning_box = QMessageBox()
            warning_box.setIcon(QMessageBox.Warning)
            warning_box.setWindowTitle("Warning")
            warning_box.setText("Time value is not set.")
            warning_box.exec_()
            return               # stop further exection

        self.time_limit = utils.convert_to_seconds(time_value,time_unit)

        print(f'set_time_limit : {self.time_limit}')

        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.browse_btn.setEnabled(False)

        # start timer
        self.start_timer()
        self.start_video_feed()

    def stop_process(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.browse_btn.setEnabled(True)
        self.timer.stop_timer()
        self.cam_feed.stop_video_feed()
        
        # bring back to default
        self.file_selected = False
        self.no_time_limit = False
        self.set_time_spinbox.setValue(0)

        # set information
        popup = QMessageBox()
        popup.setWindowTitle("Information")
        popup.setIcon(QMessageBox.Information)
        popup.setText("Video processing stopped.")
        popup.exec_()

        # Video Labels to white
        self.video_label.setPixmap(QPixmap())
        self.video_process_label.setPixmap(QPixmap())

        self.selected_file_label.setText("Stop Process")

        # Counter to Zero
        self.poland_in_lcd.display(0)
        self.poland_out_lcd.display(0)
        self.nonpoland_in_lcd.display(0)
        self.nonpoland_out_lcd.display(0)

    def set_time_elapsed(self,time_sec):
        time_str = utils.get_time_string(time_sec)
        self.timer_label.setText(time_str)
        
        # style time label
        self.timer_label.setStyleSheet("color: white; background-color: black;")
        self.timer_label.setAlignment(Qt.AlignCenter)  # Center-align the text
        font = QFont()
        font.setPointSize(12)  
        self.timer_label.setFont(font)

        if (time_sec >= self.time_limit) and (not self.no_time_limit):
            self.stop_process()

    @staticmethod
    def create_QImage(numpy_array):
        height, width, channel = numpy_array.shape
        bytes_per_line = channel * width
        q_image = QImage(numpy_array.data, width, height, bytes_per_line, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(q_image)
        return pixmap


    def display_raw_image(self,raw_numpy_array):
        if np.array_equal(raw_numpy_array, args.END_VIDEO_INDICATION):
            self.stop_process()
        else:
            raw_image_pixmap = self.create_QImage(raw_numpy_array)
            self.video_label.setPixmap(raw_image_pixmap)

    def display_annotate_image(self,annotate_numpy_array):
        if np.array_equal(annotate_numpy_array, args.END_VIDEO_INDICATION):
            self.stop_process()
        else:
            annotate_image_pixmap = self.create_QImage(annotate_numpy_array)
            self.video_process_label.setPixmap(annotate_image_pixmap)

    def set_LCD_display(self,track_info):
        poland_bee_in,poland_bee_out,non_poland_bee_in,non_poland_bee_out = track_info
        print(poland_bee_in)
        print(poland_bee_out)
        print(non_poland_bee_in)
        print(non_poland_bee_out)

        self.poland_in_lcd.display(poland_bee_in)
        self.poland_out_lcd.display(poland_bee_out)
        self.nonpoland_in_lcd.display(non_poland_bee_in)
        self.nonpoland_out_lcd.display(non_poland_bee_out)


    def start_timer(self):
        self.timer = TimerThread()
        self.timer.signals.timer_time_signal.connect(self.set_time_elapsed)
        self.threadpool.start(self.timer)

    def start_video_feed(self):
        if self.file_selected:
            self.cam_feed = VideoFeedThread(self.file_path)
            self.cam_feed.signals.raw_image_signal.connect(self.display_raw_image)
            self.cam_feed.signals.process_image_signal.connect(self.display_annotate_image)
            self.cam_feed.signals.track_info.connect(self.set_LCD_display)
            self.threadpool.start(self.cam_feed.run_video_tracking)
        else:
            self.cam_feed = VideoFeedThread()
            self.cam_feed.signals.raw_image_signal.connect(self.display_raw_image)
            self.cam_feed.signals.process_image_signal.connect(self.display_annotate_image)
            self.cam_feed.signals.track_info.connect(self.set_LCD_display)
            self.threadpool.start(self.cam_feed.run_realtime)
            self.selected_file_label.setText("Live Processing")


    def start_btn_click(self):
        self.start_process()


    def stop_btn_click(self):
        self.stop_process()

    def browse_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_filter = "Video Files (*.mp4 *.avi *.mkv);;All Files (*)"
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", file_filter, options=options)

        if self.file_path:
            self.selected_file_label.setText(f"Processing File: {os.path.basename(self.file_path)}")
            self.file_selected = True
        else:
            self.selected_file_label.setText("No file selected.")


############################
app = QApplication(sys.argv)
w = MainWindow()
app.exec()

# pyside6-uic mainwindow.ui -o MainWindow.py
