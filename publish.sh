#!/bin/bash

# 发布脚本 - 将包发布到PyPI

echo "🚀 准备发布 fuck 包到 PyPI..."

# 检查是否安装了必要的工具
echo "📦 检查发布工具..."
pip install --upgrade setuptools wheel twine

# 清理之前的构建
echo "🧹 清理旧的构建文件..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

# 构建包
echo "🔨 构建包..."
python setup.py sdist bdist_wheel

# 检查包
echo "🔍 检查包完整性..."
twine check dist/*

echo "📋 构建完成！文件列表："
ls -la dist/

echo ""
echo "🎯 下一步操作："
echo "1. 测试发布到 TestPyPI (可选):"
echo "   twine upload --repository testpypi dist/*"
echo ""
echo "2. 发布到正式 PyPI:"
echo "   twine upload dist/*"
echo ""
echo "⚠️  注意：发布前请确保："
echo "   - 已经注册 PyPI 账号"
echo "   - 包名 'fuck' 在 PyPI 上可用"
echo "   - 版本号是唯一的"
echo ""
echo "🔑 如果需要认证，请运行："
echo "   pip install keyring"
echo "   或使用 API token"