import pygetwindow as gw

class WindowManager:
    def is_target_active(self, window_title):
        try:
            active_window = gw.getActiveWindow()
            return active_window and window_title.lower() in active_window.title.lower()
        except Exception:
            return False