# 小米商城 - Xiaomi Mall

一个基于前后端分离架构的电商平台，采用 Vue 3 + Django REST Framework 技术栈。

## 功能特性

- **用户认证**：登录、注册、验证码获取
- **商品管理**：商品分类、商品列表、商品搜索
- **购物车管理**：添加商品、更新数量、删除商品
- **地址管理**：获取地址列表、添加新地址
- **轮播图展示**：首页轮播图展示

## 技术栈

### 后端技术
| 技术 | 版本 | 说明 |
|------|------|------|
| Django | 5.2.4 | Web 框架 |
| Django REST Framework | 3.14.0+ | API 框架 |
| MySQL | 8.0+ | 数据库 |
| django-cors-headers | 4.3.0+ | 跨域处理 |
| PyJWT | 2.8.0+ | JWT 认证 |
| Pillow | 10.0+ | 图片处理 |

### 前端技术
| 技术 | 版本 | 说明 |
|------|------|------|
| Vue | 3.5.17 | 前端框架 |
| Vue Router | 4.5.1 | 路由管理 |
| Pinia | 2.0.0+ | 状态管理 |
| Axios | 1.11.0+ | HTTP 客户端 |
| Vite | 7.0.0+ | 构建工具 |

## 项目结构

```
xiaomi-mall/
├── Django_one/                 # 后端项目
│   ├── django_one/            # Django 配置目录
│   │   ├── address_app/       # 地址模块
│   │   ├── banner_app/        # 轮播图模块
│   │   ├── cart_app/          # 购物车模块
│   │   ├── user_app/          # 用户模块
│   │   ├── utils/             # 工具函数
│   │   ├── static/            # 静态文件
│   │   ├── templates/         # 模板文件
│   │   ├── test/              # 测试文件
│   │   ├── sql/               # SQL 脚本
│   │   └── django_one/        # 项目核心配置
│   └── manage.py              # Django 管理脚本
├── Vue_one/                   # 前端项目
│   └── vue_one/               # Vue 项目目录
│       ├── src/
│       │   ├── apis/          # API 调用
│       │   ├── components/    # 公共组件
│       │   ├── views/         # 页面组件
│       │   ├── stores/        # Pinia 状态管理
│       │   ├── router/        # 路由配置
│       │   ├── styles/        # 样式文件
│       │   └── utils/         # 工具函数
│       ├── public/            # 公共资源
│       └── package.json       # 前端依赖配置
├── README.md                  # 项目说明文档
├── requirements.txt           # 后端依赖
└── 项目文档.md               # 详细技术文档
```

## 快速开始

### 后端环境搭建

```bash
# 进入后端目录
cd Django_one/django_one

# 安装依赖
pip install -r ../../requirements.txt

# 创建数据库（MySQL）
CREATE DATABASE xiaomishopper CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 数据库迁移
python manage.py migrate

# 启动开发服务器
python manage.py runserver 0.0.0.0:8000
```

### 前端环境搭建

```bash
# 进入前端目录
cd Vue_one/vue_one

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

### 访问地址

- 前端：http://localhost:5173
- 后端 API：http://localhost:8000
- Django 管理后台：http://localhost:8000/admin/

## API 接口

### 用户接口
| 接口 | 方法 | 描述 |
|------|------|------|
| `/api/login/` | POST | 用户登录 |
| `/api/register/` | POST | 用户注册 |
| `/api/userinfo/<userId>/` | GET | 获取用户信息 |
| `/api/captcha/` | GET | 获取验证码 |

### 商品接口
| 接口 | 方法 | 描述 |
|------|------|------|
| `/api/category/` | GET | 获取商品分类 |
| `/api/goodsbycategory/` | GET | 根据分类获取商品 |
| `/api/goodsbyname/` | GET | 根据名称搜索商品 |

### 购物车接口
| 接口 | 方法 | 描述 |
|------|------|------|
| `/api/cart/` | GET | 获取购物车列表 |
| `/api/cart/` | POST | 添加商品到购物车 |
| `/api/cart/<ItemId>/` | PUT | 更新购物车商品数量 |
| `/api/cart/<ItemId>/` | DELETE | 删除购物车商品 |

### 轮播图接口
| 接口 | 方法 | 描述 |
|------|------|------|
| `/banner/` | GET | 获取轮播图列表 |

### 地址接口
| 接口 | 方法 | 描述 |
|------|------|------|
| `/address/` | GET | 获取地址列表 |
| `/address/` | POST | 添加新地址 |

## 开发规范

### 代码风格
- Python：遵循 PEP 8 规范
- JavaScript/TypeScript：使用 ESLint 规范
- 代码注释清晰，关键逻辑添加注释

### 分支管理
- `main`：主分支，稳定版本
- `develop`：开发分支，日常开发
- `feature/*`：功能分支，开发新功能
- `fix/*`：修复分支，修复 bug

### 提交规范
- `feat`: 新增功能
- `fix`: 修复 bug
- `docs`: 更新文档
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 添加测试

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
