import time
import threading
import os
import sys
from typing import Optional, Callable
try:
    from playsound import playsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False
    print("Warning: playsound not available. Sound notifications will be disabled.")


class FuckReminder:
    """
    A task reminder that helps fight procrastination by shouting 'FUCK' when time is up.
    """
    
    def __init__(self, timeout_minutes: float = 25, message: str = "FUCK! 时间到了！别拖延了！", 
                 sound_enabled: bool = True, custom_sound_path: Optional[str] = None):
        """
        Initialize the FuckReminder.
        
        Args:
            timeout_minutes: Time in minutes before the reminder triggers
            message: Custom message to display (default includes 'FUCK')
            sound_enabled: Whether to play sound notification
            custom_sound_path: Path to custom sound file (optional)
        """
        self.timeout_seconds = timeout_minutes * 60
        self.message = message
        self.sound_enabled = sound_enabled and SOUND_AVAILABLE
        self.custom_sound_path = custom_sound_path
        self.timer_thread = None
        self.is_running = False
        self.start_time = None
        
    def _play_system_sound(self):
        """Play system notification sound."""
        try:
            if sys.platform == "darwin":  # macOS
                os.system("afplay /System/Library/Sounds/Sosumi.aiff")
            elif sys.platform == "win32":  # Windows
                import winsound
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            else:  # Linux
                os.system("paplay /usr/share/sounds/alsa/Front_Left.wav 2>/dev/null || echo -e '\a'")
        except Exception as e:
            print(f"Could not play system sound: {e}")
            # Fallback to terminal bell
            print("\a")
    
    def _play_custom_sound(self):
        """Play custom sound file."""
        try:
            if self.custom_sound_path and os.path.exists(self.custom_sound_path):
                playsound(self.custom_sound_path)
            else:
                print(f"Custom sound file not found: {self.custom_sound_path}")
                self._play_system_sound()
        except Exception as e:
            print(f"Could not play custom sound: {e}")
            self._play_system_sound()
    
    def _trigger_reminder(self):
        """Trigger the 'FUCK' reminder with sound and message."""
        print("\n" + "="*50)
        print(f"🔥 {self.message}")
        print("="*50)
        
        if self.sound_enabled:
            if self.custom_sound_path:
                self._play_custom_sound()
            else:
                self._play_system_sound()
        
        self.is_running = False
    
    def start(self, task_description: str = "工作任务"):
        """
        Start the reminder timer.
        
        Args:
            task_description: Description of the task being timed
        """
        if self.is_running:
            print("提醒器已经在运行中...")
            return
        
        self.is_running = True
        self.start_time = time.time()
        
        print(f"⏰ 开始计时: {task_description}")
        print(f"⏱️  时长: {self.timeout_seconds/60:.1f} 分钟")
        print(f"🎯 结束时间: {time.strftime('%H:%M:%S', time.localtime(time.time() + self.timeout_seconds))}")
        
        def timer_function():
            try:
                time.sleep(self.timeout_seconds)
                if self.is_running:  # Check if not manually stopped
                    self._trigger_reminder()
            except Exception as e:
                print(f"Timer error: {e}")
                self.is_running = False
        
        self.timer_thread = threading.Thread(target=timer_function, daemon=True)
        self.timer_thread.start()
        
        # Keep main thread alive and show progress
        try:
            while self.is_running and self.timer_thread.is_alive():
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
            raise
    
    def stop(self):
        """Stop the reminder timer."""
        if self.is_running:
            self.is_running = False
            print("\n⏹️  提醒器已停止")
        else:
            print("提醒器未在运行")
    
    def status(self):
        """Get current status of the reminder."""
        if not self.is_running:
            return "未运行"
        
        if self.start_time:
            elapsed = time.time() - self.start_time
            remaining = max(0, self.timeout_seconds - elapsed)
            return f"运行中 - 剩余时间: {remaining/60:.1f} 分钟"
        
        return "运行中"


def quick_reminder(minutes: float = 25, message: str = "FUCK! 时间到了！", task: str = "专注任务"):
    """
    Quick way to start a reminder.
    
    Args:
        minutes: Duration in minutes
        message: Reminder message
        task: Task description
    """
    reminder = FuckReminder(timeout_minutes=minutes, message=message)
    reminder.start(task_description=task)