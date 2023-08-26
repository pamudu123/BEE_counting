from Detection import detection_args

import cv2
import numpy as np
from typing import Dict

from supervision.geometry.dataclasses import Point, Vector
from supervision.tools.detections import Detections

# {0: 'no_pollen', 1: 'pollen'}

class BeeCounter:
    def __init__(self, start: Point, end: Point):
        """
        Initialize a BeeeCounter object.

        :param end: Point : The ending point of the line.
        """
        self.vector = Vector(start=start, end=end)
        self.tracker_state: Dict[str, bool] = {}
        
        self.poland_bee_in_count: int = 0
        self.poland_bee_out_count: int = 0
        self.non_poland_bee_in_count: int = 0
        self.non_poland_bee_out_count: int = 0


    def update(self, detections: Detections):
        """
        Update the in_count and out_count for the detections that cross the line.

        :param detections: Detections : The detections for which to update the counts.
        """
        for xyxy, confidence, class_id, tracker_id in detections:

            if tracker_id is None:
                continue

            # we check if all four anchors of bbox are on the same side of vector
            x1, y1, x2, y2 = xyxy
            anchors = [
                Point(x=x1, y=y1),
                Point(x=x1, y=y2),
                Point(x=x2, y=y1),
                Point(x=x2, y=y2),
            ]
            triggers = [self.vector.is_in(point=anchor) for anchor in anchors]

            # detection is partially in and partially out
            if len(set(triggers)) == 2:
                continue

            tracker_state = triggers[0]
            # handle new detection
            if tracker_id not in self.tracker_state:
                self.tracker_state[tracker_id] = tracker_state
                continue

            # handle detection on the same side of the line
            if self.tracker_state.get(tracker_id) == tracker_state:
                continue

            self.tracker_state[tracker_id] = tracker_state
            if tracker_state:
                if class_id == 1:
                    self.poland_bee_in_count += 1
                elif class_id == 0:
                    self.non_poland_bee_in_count += 1
            else:
                if class_id == 1:
                    self.poland_bee_out_count += 1
                elif class_id == 0:
                    self.non_poland_bee_out_count += 1

        return (self.poland_bee_in_count,
                self.poland_bee_out_count,
                self.non_poland_bee_in_count,
                self.non_poland_bee_out_count)

            
        # print(f'POLAND IN: {self.poland_bee_in_count} | POLAND OUT: {self.poland_bee_out_count}')
        # print(f'NON POLAND IN: {self.non_poland_bee_in_count} | NON POLAND OUT: {self.non_poland_bee_out_count}')

class BeeCounterAnnotator:
    def __init__(self, frame_width:int, frame_height:int):
        # Define frame dimensions
        self.frame_width  = frame_width
        self.frame_height = frame_height

    def annotate(self, frame: np.ndarray, bee_counter: BeeCounter):
        annotation_frame = frame.copy()

        # Draw Line
        cv2.line(annotation_frame,bee_counter.vector.start.as_xy_int_tuple(),
            bee_counter.vector.end.as_xy_int_tuple(),
            color=(0,0,0),thickness=2,lineType=cv2.LINE_AA)

        # # Draw a horizontal bar at the bottom
        # bar_height = 40
        # cv2.rectangle(annotation_frame, (0, self.frame_height - bar_height), (self.frame_width, self.frame_height), (255, 255, 255), -1)

        # # Define cell coordinates and dimensions
        # cell_width = self.frame_width // 2
        # cell_height = bar_height

        # # Draw the text on the first row
        # cv2.putText(annotation_frame, "POLAND BEE", (cell_width * 0 + 10, self.frame_height - bar_height + 25),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        # cv2.putText(annotation_frame, "NON POLAND BEE", (cell_width * 1 + 10, self.frame_height - bar_height + 25),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        # # Draw a horizontal line at the bottom of the previous bar
        # cv2.rectangle(annotation_frame, (0, self.frame_height - bar_height * 2), (self.frame_width, self.frame_height - bar_height),
        #             (255, 255, 255), -1)

        # # Define cell coordinates and dimensions for the second row
        # cell_width = self.frame_width // 4

        # # Draw the IN and OUT cells with their respective colors
        # cv2.rectangle(annotation_frame, (cell_width * 0, self.frame_height - bar_height * 2), (cell_width * 1, self.frame_height - bar_height),
        #             (0, 255, 0), -1)  # IN cell (GREEN)
        # cv2.rectangle(annotation_frame, (cell_width * 1, self.frame_height - bar_height * 2), (cell_width * 2, self.frame_height - bar_height),
        #             (0, 0, 255), -1)  # OUT cell (RED)
        # cv2.rectangle(annotation_frame, (cell_width * 2, self.frame_height - bar_height * 2), (cell_width * 3, self.frame_height - bar_height),
        #             (0, 255, 0), -1)  # IN cell (GREEN)
        # cv2.rectangle(annotation_frame, (cell_width * 3, self.frame_height - bar_height * 2), (cell_width * 4, self.frame_height - bar_height),
        #             (0, 0, 255), -1)  # OUT cell (RED)

        # # Draw the text on the second row
        # cv2.putText(annotation_frame, f"IN: {bee_counter.poland_bee_in_count}", (cell_width * 0 + 10, self.frame_height - bar_height * 2 + 25),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        # cv2.putText(annotation_frame, f"OUT: {bee_counter.poland_bee_out_count}", (cell_width * 1 + 10, self.frame_height - bar_height * 2 + 25),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        # cv2.putText(annotation_frame, f"IN: {bee_counter.non_poland_bee_in_count}", (cell_width * 2 + 10, self.frame_height - bar_height * 2 + 25),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        # cv2.putText(annotation_frame, f"OUT: {bee_counter.non_poland_bee_out_count}", (cell_width * 3 + 10, self.frame_height - bar_height * 2 + 25),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        return annotation_frame
    
        # Display the resulting image
        # cv2.imshow("COUNTING DISPLAY", annotation_frame)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
