# Fuckme - 任务提醒器

一个帮助你对抗拖延症的Python包。当你设定的工作时间到了，它会用"FUCK"来叫醒你！

## 功能特点

- ⏰ 自定义提醒时间
- 🔊 系统声音提醒（可选）
- 🎵 自定义声音文件支持
- 💬 自定义提醒消息
- 📊 实时倒计时显示
- 🎯 任务描述记录
- 🚀 简单易用的命令行界面

## 安装

```bash
pip install fuckme
```

## 使用方法

### 命令行使用

```bash
# 默认25分钟番茄钟
fuckme

# 自定义时间（45分钟）
fuckme -t 45

# 自定义任务描述
fuckme "写代码"

# 自定义提醒消息
fuckme -t 30 -m "起来干活！"

# 关闭声音
fuckme -t 60 --no-sound

# 使用自定义声音文件
fuckme -t 20 -s /path/to/your/sound.mp3
```

### Python代码使用

```python
from fuckme import FuckReminder

# 创建提醒器
reminder = FuckReminder(
    timeout_minutes=25,
    message="FUCK! 时间到了！",
    sound_enabled=True
)

# 开始任务
reminder.start("写Python代码")

# 或者使用快速函数
from fuckme.reminder import quick_reminder
quick_reminder(minutes=30, task="学习新技术")
```

## 命令行参数

- `task`: 任务描述（可选，默认："专注工作"）
- `-t, --time`: 提醒时间（分钟，默认：25）
- `-m, --message`: 自定义提醒消息
- `--no-sound`: 禁用声音提醒
- `-s, --sound`: 自定义声音文件路径
- `--version`: 显示版本信息

## 使用场景

- 🍅 番茄工作法
- 📚 学习时间管理
- 💻 编程专注时间
- 📝 写作时间控制
- 🎯 任何需要时间提醒的任务

## 系统兼容性

- ✅ macOS
- ✅ Windows
- ✅ Linux

## 依赖

- Python 3.7+
- playsound (用于声音播放)

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 免责声明

本工具仅用于提醒和时间管理，请合理使用。如果你觉得"FUCK"这个词不合适，可以通过`-m`参数自定义提醒消息。