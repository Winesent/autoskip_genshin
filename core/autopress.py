import threading
import time
import pyautogui
from .windows_tools import WindowManager


class AutoPressController:
    # Список поддерживаемых специальных клавиш
    SPECIAL_KEYS = [
        'space', 'tab', 'enter', 'esc', 'backspace',
        'delete', 'insert', 'home', 'end', 'pageup',
        'pagedown', 'up', 'down', 'left', 'right',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7',
        'f8', 'f9', 'f10', 'f11', 'f12'
    ]

    def __init__(self, status_callback):
        self.is_running = False
        self.status_callback = status_callback
        self.window_manager = WindowManager()

    def validate(self, params):
        errors = []
        if len(params['window_title']) < 3:
            errors.append("Название окна слишком короткое")

        key = params['key'].lower()
        if not (key.isalpha() and len(key) == 1 or key in self.SPECIAL_KEYS):
            errors.append(f"Неподдерживаемая клавиша. Доступные: буквы или {', '.join(self.SPECIAL_KEYS)}")

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
                self.status_callback(f"Нажата клавиша: {params['key'].upper()}")
            time.sleep(float(params['interval']))