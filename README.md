## 校园网自动登录工具 (Python + Selenium)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)

一个基于 Python 和 Selenium 的校园网自动登录脚本，可自动输入账号密码并选择运营商完成登录。

## 功能特性

- 自动填充校园网登录账号和密码
- 支持选择不同运营商（中国移动、中国电信、中国联通）
- 完全模拟浏览器操作，避免被检测为机器人
- 可设置定时执行，保持网络连接
- 支持无头模式（无界面运行）
- 登录状态检测和结果反馈

## 快速开始

### 前提条件

- Python 3.7 或更高版本
- Chrome 浏览器
- 校园网登录页面可访问

### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/yangdi09128036/Automatic-login-to-the-campus-network.git
cd Automatic-login-to-the-campus-network
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 下载对应版本的 ChromeDriver
- 查看你的 Chrome 浏览器版本
- 从 [ChromeDriver官网](https://chromedriver.chromium.org/downloads) 下载匹配的驱动
- 将 `chromedriver.exe` 放在项目目录下

### 配置使用

1. 修改 `config.ini` 文件
```ini
[LOGIN_INFO]
username = 你的校园网账号
password = 你的密码
operator = 运营商 (移动/电信/联通)

[SETTINGS]
login_url = 校园网登录页面URL
headless = False  # 是否使用无头模式
check_interval = 60  # 检查网络状态间隔(分钟)
```

2. 运行程序
```bash
python auto_login.py
```

## 定时运行 (Windows)

1. 创建批处理文件 `run.bat`
```bat
@echo off
python "%~dp0auto_login.py"
```

2. 使用任务计划程序设置定时任务
- 搜索并打开"任务计划程序"
- 创建基本任务
- 设置触发器(如每天或登录时)
- 操作为"启动程序"，选择上面的 `run.bat`

## 程序结构

```
Automatic-login-to-the-campus-network/
├── auto_login.py      # 主程序
├── config.ini        # 配置文件
├── requirements.txt  # 依赖文件
└── README.md        # 说明文档
```

## 注意事项

1. 请确保 Chrome 浏览器已安装
2. ChromeDriver 版本必须与 Chrome 浏览器版本匹配
3. 首次运行时请关闭无头模式测试
4. 校园网登录页面结构变化时可能需要调整代码
5. 请勿将账号密码直接写在代码中，使用配置文件

## 自定义修改

1. 修改定位元素
- 如果登录页面结构不同，需要修改 `auto_login.py` 中的元素定位
- 使用开发者工具(F12)查看页面HTML结构

2. 调整等待时间
- 根据网络情况调整 `WebDriverWait` 的超时时间

## 常见问题

**Q: 程序报错说找不到ChromeDriver?**  
A: 请下载正确版本的 ChromeDriver 并放在项目目录中

**Q: 登录页面加载不出来?**  
A: 尝试增加 `WebDriverWait` 的等待时间，或检查网络连接

**Q: 如何查看无头模式的运行情况?**  
A: 将 `headless` 设置为 `False` 或查看程序输出

## 开发者

- 作者: 你的名字
- 邮箱/QQ: 你的联系方式
- 仓库: [GitHub](https://github.com/yangdi09128036/Automatic-login-to-the-campus-network)

## 许可证

[MIT License](LICENSE)
```

这个README包含:
1. 项目简介和徽章
2. 功能列表
3. 详细的安装和配置说明
4. 定时运行设置
5. 项目结构
6. 注意事项
7. 自定义修改指南
8. 常见问题解答
9. 开发者信息
10. 许可证信息

你可以根据实际情况修改配置项、登录页面URL和元素定位方式。建议将敏感信息(如账号密码)放在配置文件中，不要直接写入代码。
