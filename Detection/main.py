import args
import os
import sys

HOME = os.getcwd()
sys.path.append(f"{HOME}/ByteTrack")


import cv2
import numpy as np
from tqdm import tqdm

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
import bee_track
from track_utils import *
from BYTETrackerArgs import *


print("yolox.__version__:", yolox.__version__)
print("supervision.__version__:", supervision.__version__)


## save and load video paths
source_video_path = args.SOURCE_VIDEO_PATH
target_video_path = args.SAVE_VIDEO_PATH

## SETUP YOLO MODEL ##
model = YOLO( args.YOLO_MODEL_PATH)
model.fuse()


# dict maping class_id to class_name
class_names_dict = model.model.names

line_start = Point(args.LINE_START[0], args.LINE_START[1])
line_end = Point(args.LINE_END[0], args.LINE_END[1])


# create BYTETracker instance
byte_tracker = BYTETracker(BYTETrackerArgs())
# create VideoInfo instance
video_info = VideoInfo.from_video_path(source_video_path)
# create frame generator
generator = get_video_frames_generator(source_video_path)

bee_counter = bee_track.BeeCounter(start=line_start, end=line_end)
bee_count_annotator = bee_track.BeeCounterAnnotator(args.FRAME_WIDTH, args.FRAME_HEIGHT)

# create instance of BoxAnnotator and LineCounterAnnotator
box_annotator = BoxAnnotator(
    color=ColorPalette([color.Color(0, 0, 255), color.Color(255, 255, 0)]),
    thickness=1,
    text_thickness=1,
    text_scale=0.5,
)

# open target video file
with VideoSink(target_video_path, video_info) as sink:
    # loop over video frames
    for frame in tqdm(generator, total=video_info.total_frames):
        # model prediction on single frame and conversion to supervision Detections
        results = model(frame)
        detections = Detections(
            xyxy=results[0].boxes.xyxy.cpu().numpy(),
            confidence=results[0].boxes.conf.cpu().numpy(),
            class_id=results[0].boxes.cls.cpu().numpy().astype(int),
        )
        
        # tracking detections
        tracks = byte_tracker.update(
            output_results = detections2boxes(detections=detections),
            img_info=frame.shape,
            img_size=frame.shape,
        )
        tracker_id = match_detections_with_tracks(detections=detections, tracks=tracks)
        detections.tracker_id = np.array(tracker_id)
        
        print(len(detections))
        print(detections.class_id)
        print(detections.tracker_id)
        print(len(detections.tracker_id))


        if len(detections.tracker_id) > 0:
            labels = [
                f"#{tracker_id} {class_names_dict[class_id]}"
                for _, confidence, class_id, tracker_id in detections
            ]

        bee_counter.update(detections=detections)

        # annotate and display frame
        frame = box_annotator.annotate(
            frame=frame, detections=detections, labels=labels
        )

        display_frame = bee_count_annotator.annotate(frame, bee_counter)

        sink.write_frame(display_frame)

        # Display the resulting image
        cv2.imshow("LIVE", display_frame)
        cv2.waitKey(1)
    cv2.destroyAllWindows()