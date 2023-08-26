from PySide6.QtCore import  QRunnable, Slot
from worker_signals import WorkerSignals
import time

class TimerThread(QRunnable):
    def __init__(self):
        super(TimerThread, self).__init__()
        self.signals = WorkerSignals()
        self.timer_is_working = True
        

    @Slot()
    def run(self):
        start_time = time.time()
        while self.timer_is_working:
            elapsed_time = time.time() - start_time
            self.signals.timer_time_signal.emit(elapsed_time)
            time.sleep(1)

    def stop_timer(self):
        self.timer_is_working = False   

