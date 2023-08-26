from PySide6.QtCore import QRunnable, Slot
from worker_signals import WorkerSignals


from supervision.video.dataclasses import VideoInfo
from supervision.video.source import get_video_frames_generator

from tqdm import tqdm
import cv2

# custom scripts
import args
from Detection.bee_track_system import BeeTrackingSystem


class VideoFeedThread(QRunnable):
    def __init__(self,video_path='NAN'):
        super(VideoFeedThread, self).__init__()
        self.signals = WorkerSignals()

        self.process_started = True
        self.video_path = video_path

        self.tracking_system = BeeTrackingSystem()

    @staticmethod
    def create_out_frame(in_frame):
        out_frame = in_frame.copy()
        out_frame = cv2.cvtColor(out_frame,cv2.COLOR_BGR2RGB)
        out_frame = cv2.resize(out_frame,(args.DISP_IMAGE_WIDTH,args.DISP_IMAGE_HEIGHT))
        out_frame = cv2.resize(out_frame,(0,0),fx=0.5,fy=0.5)
        return out_frame


    @Slot()
    def run_realtime(self):
        self.cap = cv2.VideoCapture(args.CAMERA_IDX)

        while self.process_started:
            print(self.process_started)
            ret, frame = self.cap.read()
            raw_frame = frame.copy()
            if not ret:
                print("Error: Unable to read frame from webcam.")
                self.process_started = False

            annotate_frame,count_info = self.tracking_system.run_tracking(frame)

            # create image to show in the GUI
            out_frame = self.create_out_frame(raw_frame)
            out_annotate_frame = self.create_out_frame(annotate_frame)

            self.signals.raw_image_signal.emit(out_frame)
            self.signals.process_image_signal.emit(out_annotate_frame)
            self.signals.track_info.emit(count_info)


    @Slot()      
    def run_video_tracking(self):
        source_video_path = self.video_path
        video_info = VideoInfo.from_video_path(source_video_path)
        
        # create frame generator
        generator = get_video_frames_generator(source_video_path)
        
        # loop over video frames
        for frame in tqdm(generator, total=video_info.total_frames):
            raw_frame = frame.copy()
            if self.process_started:
                annotate_frame,count_info = self.tracking_system.run_tracking(frame)

                # BGR to RGB before send
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                annotate_frame = cv2.cvtColor(annotate_frame,cv2.COLOR_BGR2RGB)

                # create image to show in the GUI
                out_frame = self.create_out_frame(raw_frame)
                out_annotate_frame = self.create_out_frame(annotate_frame)
                
                self.signals.raw_image_signal.emit(out_frame)
                self.signals.process_image_signal.emit(out_annotate_frame)
                self.signals.track_info.emit(count_info)
        else:
            # signals for video is end
            self.cap.release()
            self.signals.process_image_signal.emit(args.END_VIDEO_INDICATION)
            self.signals.raw_image_signal.emit(args.END_VIDEO_INDICATION)
    
    def stop_video_feed(self):
        self.process_started = False