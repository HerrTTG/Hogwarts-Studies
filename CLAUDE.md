# CLAUDE.md - Hogwarts-Studies AI 助手配置

## 项目概述

霍格沃茨学社（Hogwarts-Studies）是一个 **Python 学习与练习仓库**，包含编程作业、练习题、自动化测试框架实践等内容。项目以模块化目录组织，便于按主题学习和查阅。

- 仓库地址：`git@github.com:HerrTTG/Hogwarts-Studies.git`
- 项目语言：Python 为主，混合 Shell / YAML / HTML

---

## 目录结构

```
Hogwarts-Studies/
├── homework/                # 课程作业
│   ├── docker/              # Docker 部署作业
│   ├── git l1/              # Git 基础作业
│   ├── postman/             # Postman 接口测试作业
│   ├── python/              # Python 基础作业
│   ├── web自动化/           # Selenium Web 自动化作业
│   ├── 接口自动化/           # API 自动化测试作业（Pytest + DDT）
│   ├── 数据驱动测试框架搭建/  # DDT 框架实践
│   ├── pytest_and_allure/   # Pytest + Allure 报告实践
│   └── shell脚本/           # Shell 脚本集合
├── 练习和考试题/              # 练习题与考试题
│   ├── CSV/                 # CSV 文件处理
│   ├── JSON/                # JSON 数据处理
│   ├── OOP/                 # 面向对象编程
│   ├── PDF/                 # PDF 操作
│   ├── excel处理/           # Excel 读写（openpyxl）
│   ├── gui界面开发/          # Tkinter GUI 开发
│   ├── gui自动化/            # GUI 自动化（pyautuogui 等）
│   ├── python语言进阶/        # 元编程 / 高阶函数 / 异步编程
│   ├── web开发/              # Flask 后端 + 爬虫
│   ├── web自动化/            # Selenium 进阶（POM、Grid）
│   ├── 接口自动化/           # API 自动化（企业微信、宠物商店）
│   ├── 自动化测试相关/       # Pytest / Allure / Fixture
│   ├── 多线程/               # 多线程 / 多进程 / 协程
│   ├── 图像处理/             # OpenCV / PIL 图像处理
│   ├── 实例词云/             # WordCloud 词云生成
│   ├── 设计模式/             # 单例 / 工厂 / 代理等设计模式
│   ├── 调试和日志/           # Logging 模块
│   ├── 后端开发/             # Flask 框架（蓝图、ORM、SQL）
│   ├── 数据库操作/           # SQL 数据库交互
│   ├── 高阶函数/             # 装饰器 / 闭包 / 生成器
│   ├── yaml文件处理/         # YAML 读写
│   ├── shell脚本/            # Shell 脚本练习
│   └── 其他/                 # 杂项练习（100+ 小脚本）
├── shell脚本/                # 独立 Shell 脚本集合
├── .gitignore
└── README.md
```

---

## 技术栈

| 类别 | 技术 / 库 |
|---|---|
| **语言** | Python 3、Bash/Shell |
| **Web 框架** | Flask、Blueprint、Flask-CORS |
| **测试框架** | Pytest、Allure Report、DDT、YAML 参数化 |
| **UI 自动化** | Selenium WebDriver、POM 模式、DrissionPage |
| **API 测试** | requests、pytest（企业微信 API、宠物商店 API） |
| **GUI 开发** | Tkinter |
| **GUI 自动化** | pyautogui、pygetwindow |
| **数据处理** | openpyxl（Excel）、csv、json、PyYAML |
| **图像处理** | Pillow、OpenCV |
| **爬虫** | requests、BeautifulSoup、selenium |
| **构建部署** | Docker、Docker Compose |
| **其他** | logging、concurrent.futures（多线程/多进程）、asyncio |

---

## 开发环境

- **操作系统**：Windows 10/11
- **IDE**：Trae CN（基于 VSCode）
- **Python**：3.x（版本未锁定）
- **包管理**：pip
- **Git**：通过 SSH key 连接 GitHub（`git@github.com:HerrTTG/...`）
- **终端**：PowerShell

---

## 编码约定

### Python
- 文件编码：UTF-8
- 每个练习/作业独立成目录，互不依赖
- 测试文件命名：`test_*.py`（Pytest 约定）
- 使用 Pytest 测试时需 `pytest.ini` 或 `conftest.py`

### Shell
- 脚本 `.sh` 在 Windows 上通过 WSL 或 Git Bash 运行
- 编码与换行符注意兼容问题

### Git
- 提交前**必须填写提交信息**（Trae IDE 强制要求）
- `.gitignore` 已配置：`report/`、`logs/`、`__pycache__/`、临时日志等

---

## 常用命令

```bash
# 运行 Pytest 测试
pytest <测试目录> -v

# 生成 Allure 报告
pytest <测试目录> --alluredir=./report/allure-results
allure serve ./report/allure-results

# 安装依赖（示例）
pip install pytest pytest-allure selenium requests openpyxl pyyaml flask

# Git 推送
git push origin main
```

---

## 给 AI 助手的特别说明

1. **不要随意删除文件或目录** —— 本仓库是学习积累，每个脚本都有参考价值
2. **新增代码应放到对应主题目录下**，保持现有结构
3. **编写测试用例时**，参考已有的 `pytest.ini` 和 `conftest.py` 配置模式
4. **Shell 脚本**注意区分 Linux 环境（`.sh`）和 Windows 环境的命令差异
5. **用户偏好**（来自全局记忆）：
   - Python 熟练、Tkinter UI 开发、Selenium 自动化
   - Selenium 替代库：DrissionPage
   - Excel 操作：openpyxl
   - 打包工具：PyInstaller
   - 浏览器默认隐藏，Debug 模式才显示
