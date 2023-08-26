import os
import sys

import cv2
import numpy as np
from tqdm import tqdm

# To avoid yolox not found error
HOME = os.getcwd()
sys.path.append(f"{HOME}/Detection/ByteTrack")

import yolox
import supervision
from ultralytics import YOLO

from supervision.draw.color import ColorPalette
from supervision.geometry.dataclasses import Point
from supervision.video.dataclasses import VideoInfo
from supervision.video.source import get_video_frames_generator
from supervision.video.sink import VideoSink
from supervision.tools.detections import Detections, BoxAnnotator
import supervision.draw.color as color


## custom functions
from Detection import bee_counter
from Detection.track_utils import *
from Detection.BYTETrackerArgs import *
from Detection import detection_args


class BeeTrackingSystem:
    def __init__(self,camera_feed = True):
        # HOME = os.getcwd()
        # sys.path.append(f"{HOME}/Detection/ByteTrack")
        self.camera_feed = camera_feed
        self.initialize_components()

    def initialize_components(self):
        # set YOLO parameters
        self.model = YOLO(detection_args.YOLO_MODEL_PATH)
        self.model.fuse()

        # set class names
        self.class_names_dict = self.model.model.names

        # set tracking options
        self.line_start = Point(detection_args.LINE_START[0], detection_args.LINE_START[1])
        self.line_end = Point(detection_args.LINE_END[0], detection_args.LINE_END[1])
        self.byte_tracker = BYTETracker(BYTETrackerArgs())

        self.bee_counter = bee_counter.BeeCounter(start=self.line_start, end=self.line_end)
        self.bee_count_annotator = bee_counter.BeeCounterAnnotator(detection_args.FRAME_WIDTH, detection_args.FRAME_HEIGHT)
        
        # set annotator
        self.box_annotator = BoxAnnotator(
            color=ColorPalette([color.Color(0, 0, 255), color.Color(255, 255, 0)]),
            thickness=1,
            text_thickness=1,
            text_scale=0.5,
        )            

    def run_realtime_tracking(self):
        cap = cv2.VideoCapture(detection_args.CAMERA_IDX)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read frame from webcam.")
                break

            self.run_tracking(frame)
       
    def run_video_tracking(self,source_video_path):
        print("RUN TRACKING")
        video_info = VideoInfo.from_video_path(source_video_path)
        # create frame generator
        generator = get_video_frames_generator(source_video_path)
        
        # loop over video frames
        for frame in tqdm(generator, total=video_info.total_frames):
            self.run_tracking(frame)


    def run_tracking(self,frame):
        try:
            print("WORKING")
            results = self.model(frame)
            detections = Detections(
                xyxy=results[0].boxes.xyxy.cpu().numpy(),
                confidence=results[0].boxes.conf.cpu().numpy(),
                class_id=results[0].boxes.cls.cpu().numpy().astype(int),
            )

            tracks = self.byte_tracker.update(
                output_results=detections2boxes(detections=detections),
                img_info=frame.shape,
                img_size=frame.shape,
            )
            tracker_id = match_detections_with_tracks(detections=detections, tracks=tracks)
            detections.tracker_id = np.array(tracker_id)

            labels = [
                f"#{tracker_id} {self.class_names_dict[class_id]}"
                for _, confidence, class_id, tracker_id in detections
            ]

            count_info = self.bee_counter.update(detections=detections)

            frame = self.box_annotator.annotate(
                frame=frame, detections=detections, labels=labels
            )

            display_frame = self.bee_count_annotator.annotate(frame, self.bee_counter)

            return display_frame,count_info
        
        except Exception as e:
            print(e)
            white_image = np.ones((100, 100, 3), dtype=np.uint8) * 255
            return white_image,(0,0,0,0)


if __name__ == "__main__":
    tracking_system = BeeTrackingSystem()

    # track video
    tracking_system.run_video_tracking(detection_args.SOURCE_VIDEO_PATH)

    # track realtime
    # tracking_system.run_realtime_tracking()
