#!/usr/bin/env python3
"""
使用示例 - 展示如何使用 fuck 提醒器
"""

from fuckme.reminder import FuckReminder, quick_reminder
import time


def example_basic_usage():
    """基本使用示例"""
    print("📝 示例1: 基本使用")
    print("创建一个2分钟的提醒器...")
    
    reminder = FuckReminder(
        timeout_minutes=2,
        message="FUCK! 2分钟到了！该休息一下了！",
        sound_enabled=True
    )
    
    # 开始任务
    reminder.start("写文档")


def example_custom_settings():
    """自定义设置示例"""
    print("\n📝 示例2: 自定义设置")
    print("创建一个1分钟的自定义提醒器...")
    
    reminder = FuckReminder(
        timeout_minutes=1,
        message="🎯 专注时间结束！你做得很好！",
        sound_enabled=False  # 关闭声音
    )
    
    reminder.start("学习Python")


def example_quick_reminder():
    """快速提醒示例"""
    print("\n📝 示例3: 快速提醒")
    print("使用快速函数创建30秒提醒...")
    
    quick_reminder(
        minutes=0.5,  # 30秒
        message="⚡ 快速测试完成！",
        task="快速测试"
    )


if __name__ == "__main__":
    print("🎉 Fuckme 提醒器使用示例")
    print("=" * 40)
    
    try:
        # 运行示例（注意：这些会实际运行计时器）
        print("选择要运行的示例:")
        print("1. 基本使用 (2分钟)")
        print("2. 自定义设置 (1分钟)")
        print("3. 快速提醒 (30秒)")
        print("4. 退出")
        
        choice = input("\n请输入选择 (1-4): ").strip()
        
        if choice == "1":
            example_basic_usage()
        elif choice == "2":
            example_custom_settings()
        elif choice == "3":
            example_quick_reminder()
        elif choice == "4":
            print("👋 再见！")
        else:
            print("❌ 无效选择")
            
    except KeyboardInterrupt:
        print("\n⏹️  示例被中断")
    except Exception as e:
        print(f"\n❌ 运行示例时出错: {e}")