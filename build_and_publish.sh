#!/bin/bash

echo "🚀 开始构建和发布 fuck 包到 PyPI..."

# 检查是否在正确的目录
if [ ! -f "setup.py" ]; then
    echo "❌ 错误: 找不到 setup.py 文件"
    exit 1
fi

# 安装/升级必要的工具
echo "📦 检查并安装发布工具..."
pip install --upgrade setuptools wheel twine

# 清理旧的构建文件
echo "🧹 清理旧的构建文件..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

# 构建包
echo "🔨 构建包..."
python setup.py sdist bdist_wheel

# 检查构建结果
if [ $? -ne 0 ]; then
    echo "❌ 构建失败!"
    exit 1
fi

# 检查包完整性
echo "🔍 检查包完整性..."
twine check dist/*

if [ $? -ne 0 ]; then
    echo "❌ 包检查失败!"
    exit 1
fi

# 显示构建的文件
echo "📋 构建完成！文件列表："
ls -la dist/

echo ""
echo "✅ 包构建成功！现在开始上传到 PyPI..."

# 上传到 PyPI
echo "🚀 上传到 PyPI..."
twine upload dist/*

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 发布成功！"
    echo "📦 你的包现在可以通过以下命令安装："
    echo "   pip install fuck"
    echo ""
    echo "🔗 查看你的包："
    echo "   https://pypi.org/project/fuck/"
else
    echo "❌ 上传失败! 请检查错误信息。"
    exit 1
fi