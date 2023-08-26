from PySide6.QtCore import Signal, QObject
import numpy as np


class WorkerSignals(QObject):
    timer_time_signal    = Signal(int)
    raw_image_signal     = Signal(np.ndarray)
    process_image_signal = Signal(np.ndarray)
    track_info           = Signal(tuple)
    


