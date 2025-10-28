#!/usr/bin/env python3
"""
Test script for the fuck reminder package.
"""

import time
from fuckme.reminder import FuckReminder, quick_reminder


def test_basic_functionality():
    """Test basic reminder functionality."""
    print("🧪 测试基本功能...")
    
    # Test with very short timeout for testing
    reminder = FuckReminder(
        timeout_minutes=0.1,  # 6 seconds
        message="测试提醒！",
        sound_enabled=False  # Disable sound for testing
    )
    
    print("开始5秒测试...")
    reminder.start("测试任务")
    print("✅ 基本功能测试完成")


def test_quick_reminder():
    """Test quick reminder function."""
    print("\n🧪 测试快速提醒功能...")
    print("这将运行5秒钟的快速测试...")
    
    # This will run for 5 seconds
    quick_reminder(minutes=0.08, message="快速测试完成！", task="快速测试")
    print("✅ 快速提醒测试完成")


if __name__ == "__main__":
    print("🚀 开始测试 Fuckme 提醒器...")
    
    try:
        test_basic_functionality()
        time.sleep(1)
        test_quick_reminder()
        print("\n🎉 所有测试完成！")
        
    except KeyboardInterrupt:
        print("\n⏹️  测试被用户中断")
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")