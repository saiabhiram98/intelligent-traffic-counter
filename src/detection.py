import cv2
from ultralytics import YOLO


class TrafficMonitor:
    def __init__(self, video_source):
        self.model = YOLO("yolov8m-seg.pt")
        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)
        self.path_lines = {
            1: [(100, 550), (650, 550)],
            2: [(650, 550), (1200, 550)],
            3: [(1050, 180), (1250, 130)],
        }
        self.car_counts = {1: 0, 2: 0, 3: 0}
        self.crossed_ids = {1: set(), 2: set(), 3: set()}
        self.frame_count = 0

    def process_frame(self, frame):
        results = self.model(frame)[0]
        annotated_frame = results.plot()
        return results, annotated_frame
    
    def get_status(self):
        return self.car_counts
    
