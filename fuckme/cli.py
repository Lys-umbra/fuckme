#!/usr/bin/env python3
"""
Command line interface for the Fuckme reminder tool.
"""

import argparse
import sys
from .reminder import FuckReminder, quick_reminder


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fuckme - A task reminder that wakes you up when you're procrastinating",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  fuckme                          # Start 25-minute timer with default settings
  fuckme -t 45                    # 45-minute timer
  fuckme -t 30 -m "起来干活！"      # Custom message
  fuckme -t 60 --no-sound         # No sound notification
  fuckme -t 20 -s /path/to/sound.mp3  # Custom sound file
  fuckme -t 15 "写代码"            # 15 minutes for coding task
        """
    )
    
    parser.add_argument(
        "task",
        nargs="?",
        default="专注任务",
        help="Task description (optional)"
    )
    
    parser.add_argument(
        "-t", "--time",
        type=float,
        default=25,
        help="Timer duration in minutes (default: 25)"
    )
    
    parser.add_argument(
        "-m", "--message",
        default="FUCK! 时间到了！别拖延了！",
        help="Custom reminder message"
    )
    
    parser.add_argument(
        "--no-sound",
        action="store_true",
        help="Disable sound notifications"
    )
    
    parser.add_argument(
        "-s", "--sound",
        help="Path to custom sound file"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="fuckme 1.0.0"
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.time <= 0:
        print("错误: 时间必须大于0分钟")
        sys.exit(1)
    
    try:
        # Create and start reminder
        print(f"🎯 任务: {args.task}")
        print(f"⏰ 时间: {args.time} 分钟")
        print(f"💬 提醒: {args.message}")
        print("🚀 开始计时...")
        print("按 Ctrl+C 可以随时停止")
        
        reminder = FuckReminder(
            timeout_minutes=args.time,
            message=args.message,
            sound_enabled=not args.no_sound,
            sound_file=args.sound
        )
        
        reminder.start(task_description=args.task)
        
    except KeyboardInterrupt:
        print("\n⏹️  计时器已停止")
        sys.exit(0)
    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()