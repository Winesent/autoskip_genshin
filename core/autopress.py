import threading
import time
import pyautogui
from .windows_tools import WindowManager

class AutoPressController:
    def __init__(self, status_callback):
        self.is_running = False
        self.status_callback = status_callback
        self.window_manager = WindowManager()

    def validate(self, params):
        errors = []
        if len(params['window_title']) < 3:
            errors.append("Название окна слишком короткое")
        if len(params['key']) != 1 or not params['key'].isalpha():
            errors.append("Укажите одну букву для нажатия")
        try:
            if float(params['interval']) <= 0:
                errors.append("Интервал должен быть положительным числом")
        except ValueError:
            errors.append("Неверный формат интервала")
        return errors

    def start(self, params):
        self.is_running = True
        self.thread = threading.Thread(
            target=self._run_loop,
            args=(params,),
            daemon=True
        )
        self.thread.start()

    def stop(self):
        self.is_running = False

    def _run_loop(self, params):
        while self.is_running:
            if self.window_manager.is_target_active(params['window_title']):
                pyautogui.press(params['key'])
                self.status_callback(f"Нажата клавиша {params['key'].upper()}")
            time.sleep(float(params['interval']))