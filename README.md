<div align="center">

# 毕业设计作品集 · Graduation Projects

**21 个项目的索引与技术点速查** — Spring Boot + Vue 3 全栈 / 计算机视觉 / 推荐系统 / 数据分析 / AI Agent / 低代码 AI 办公

</div>

> 除特别说明外，项目均为独立完整实现：前后端分离、真实数据库、可运行、含启动脚本与部署说明。
> Java 全栈仓库结构统一为 `backend/ · frontend/ · sql/ · docs/`；
> Python 项目（`pf-mdd-yolov8-defect-detection` · `feishu-hub`）为 `src/ · tests/ · config/ · docs/`。
> 每个仓库都带 MIT License、CI 与 `v1.0.0` 定稿 tag。

**工程质量现状**：21/21 仓库 CI 全绿 · 94 个自动化测试 · 前端依赖漏洞从 ~150 降到 ~43 · Dependabot 漏洞告警全开

**可见性**：本索引**公开可浏览**；🔒 = 私有仓库（可邮件申请只读）；公开仓库可直接 clone 运行。

## 🚦 3 分钟速看（按目标看）

| 你的目的 | 先看这里 |
|---|---|
| 30 秒判断水平 | [精选 5 个主推项目](#一主推项目面试重点讲这-5-个) 的「核心难点 / 工程亮点」两行 |
| 找对口的仓库 | [能力矩阵](#二能力矩阵) 按方向挑，再看[全部项目卡片](#三全部项目卡片) |
| 只看能不能跑 | 表里标 🔒 的是私有仓库；未标 🔒 的 5 个（pf-mdd / study-material / family-finance / gz-student-rental / kip-agent / shiji-releases）可直接 clone |
| 关心工程规范 | [公共工程规范](#四公共工程规范21-个仓库一致) + [测试明细](#五自动化测试明细94-个) |
| 想让我讲细节 | 每个仓库都有 `docs/` 与启动说明；主推项目还有「可讲点」行（面试 Q&A 提纲） |

---

## 一、主推项目（面试重点讲这 5 个）

### 1. 🔒 🔒 [steel-surface-defect-detection](https://github.com/LuOzawa/steel-surface-defect-detection) · 本科毕业设计 · 钢材表面缺陷检测

| 项 | 内容 |
|---|---|
| 技术栈 | Python / PyTorch / Ultralytics YOLOv8 / SE 通道注意力 / PyQt5 |
| ★ 指标 | NEU-DET 六类缺陷，mAP@0.5 **0.8107 → 0.8291（+1.8 pt）**，mAP@0.5:0.95 0.4971 → **0.5153** |
| ★ 核心难点 | **在骨干 SPPF 后插入 SE 模块**（reduction=16，512→32→512）做通道重标定，只加 32 KB 参数（+0.2%）换 1.8 个点；训练 / 评估 / 推理 / PyQt5 界面全流程，已通过答辩 |
| 可讲点 | 注意力模块插在哪、精度与开销如何权衡、跨设备复现差异 0.3 pt 怎么解释 |

### 2. [study-material-recommender](https://github.com/LuOzawa/study-material-recommender) · 考研资料推荐

| 项 | 内容 |
|---|---|
| 技术栈 | Spring Boot 3.2 / Java 17 / Vue 3 / Hadoop 3.3.6 / HDFS / MySQL 8 |
| ★ 核心难点 | **四路推荐融合**：UserCF + ItemCF + SVD + TF-IDF 加权融合，不依赖第三方推荐库，纯手写实现与调参 |
| ★ 工程亮点 | HDFS 归档大规模资料；离线评测（留一法 + Precision/Recall/NDCG/覆盖率）；`ProcessBuilder` 夜间定时跑批 |
| 可讲点 | 冷启动如何缓解、融合权重如何确定、评测指标为什么选 NDCG |

### 3. [pf-mdd-yolov8-defect-detection](https://github.com/LuOzawa/pf-mdd-yolov8-defect-detection) · 工业缺陷检测

| 项 | 内容 |
|---|---|
| 技术栈 | Python / PyTorch / Ultralytics YOLOv8 |
| ★ 核心难点 | **4096×256 线扫宽幅图的切块（tiling）策略**：直接 resize 会把微小缺陷压没，需要滑窗切块 + 推理结果融合回全图 |
| ★ 工程亮点 | 12 类缺陷、数据流水线（step0→step10 可复现）、迭代实验追踪、类别稳定性评估、类别不平衡分析报告 |
| 可讲点 | 切块重叠率怎么定、跨块缺陷如何合并去重、小样本类别的召回怎么提 |

### 4. [family-finance-tracker](https://github.com/LuOzawa/family-finance-tracker) · 家庭理财

| 项 | 内容 |
|---|---|
| 技术栈 | Flask / Vue 3 / scikit-learn / statsmodels / MySQL |
| ★ 核心难点 | **算法与业务真的咬合**：KMeans 消费聚类（自动发现消费模式）+ ARIMA 支出预测 + 四维财务健康评分 |
| 可讲点 | K 值怎么选、ARIMA 定阶过程、健康评分的权重来源（可解释性） |

### 5. [gz-student-rental-recsys](https://github.com/LuOzawa/gz-student-rental-recsys) · 租房推荐

| 项 | 内容 |
|---|---|
| 技术栈 | Spring Boot 3 / Vue 3 / Redis / 高德地图 / MyBatis-Plus |
| ★ 核心难点 | **协同过滤 + 地理距离的混合召回**：纯 CF 推荐会在"校园附近"这个硬约束上翻车，需引入距离惩罚项 |
| ★ 工程亮点 | Redis 缓存推荐结果、地图可视化、租房全流程 + 后台管理 |

---

## 二、能力矩阵

| 方向 | 项目 | 关键技术 |
|---|---|---|
| **AI / Agent** | [kip-agent](https://github.com/LuOzawa/kip-agent) · 🔒 [ai-tutor-miniapp](https://github.com/LuOzawa/ai-tutor-miniapp) | TypeScript 技能体系 / 沙箱 / DeepSeek LLM / 微信小程序 |
| **低代码 / AI 办公** | 🔒 [feishu-hub](https://github.com/LuOzawa/feishu-hub) | 飞书多维表格 Schema / YAML 工作流编排 / Aily 智能伙伴 / RAG 引用溯源问答 / 权限与审计 |
| **计算机视觉** | [pf-mdd-yolov8-defect-detection](https://github.com/LuOzawa/pf-mdd-yolov8-defect-detection) · 🔒 🔒 [steel-surface-defect-detection](https://github.com/LuOzawa/steel-surface-defect-detection) | YOLOv8 / tiling 滑窗推理融合 / SE 通道注意力 |
| **推荐系统** | [study-material-recommender](https://github.com/LuOzawa/study-material-recommender) · [gz-student-rental-recsys](https://github.com/LuOzawa/gz-student-rental-recsys) | UserCF / ItemCF / SVD / TF-IDF / 混合召回 |
| **数据分析预测** | 🔒 [boss-zhipin-data-analysis](https://github.com/LuOzawa/boss-zhipin-data-analysis) · [family-finance-tracker](https://github.com/LuOzawa/family-finance-tracker) | Selenium 采集 / KMeans / 线性回归 / ARIMA |
| **企业级全栈** | 10 个项目（见下表） | Spring Boot + Vue 3 + MyBatis-Plus + JWT/RBAC |
| **产品工程** | 🔒 [shiji-website](https://github.com/LuOzawa/shiji-website) · [shiji-releases](https://github.com/LuOzawa/shiji-releases) | Vite / Cloudflare Workers / 版本分发 |

---

## 三、全部项目卡片

### 企业级全栈（Spring Boot + Vue 3）

| 项目 | 业务 | 差异化技术点 |
|---|---|---|
| 🔒 [shop-platform](https://github.com/LuOzawa/shop-platform) | 电商平台 | Spring Boot 2.7 / Java 11；订单状态机、优惠券、支付流程 |
| 🔒 [pharmacy-management](https://github.com/LuOzawa/pharmacy-management) | 药店管理 | 员工端 + 会员端双端；库存预警、处方登记、会员积分 |
| 🔒 [traffic-repair-platform](https://github.com/LuOzawa/traffic-repair-platform) | 交通设施报修 | **RBAC 工单流转**：报修→审核→派单→维修→验收→申诉；前端产物打进 jar 单包部署 |
| 🔒 [community-suggestion-box](https://github.com/LuOzawa/community-suggestion-box) | 社区意见箱 | Spring Boot 2.7 / Java 8；Spring Security 三端权限隔离 |
| 🔒 [elder-health-management](https://github.com/LuOzawa/elder-health-management) | 老年健康管理 | **ADL-MMSE 量表评估**；慢病随访、预约挂号、健康指标趋势 |
| 🔒 [pet-center-management](https://github.com/LuOzawa/pet-center-management) | 宠物服务中心 | Sa-Token 三端隔离（用户/商家/管理员）；寄养、套餐、商城 |
| 🔒 [liupanshui-tourism](https://github.com/LuOzawa/liupanshui-tourism) | 六盘水文旅 | 游客端 15 模块 + 后台 13 模块；ECharts 数据看板 |
| 🔒 [jiufeng-park-management](https://github.com/LuOzawa/jiufeng-park-management) | 森林公园运营 | **生态监测阈值告警**；在线购票、入园预约 |
| 🔒 [physical-fitness-test-system](https://github.com/LuOzawa/physical-fitness-test-system) | 高校体测 | 体测申请/审核/成绩录入/统计导出；单表大数据量分页 |
| 🔒 [internship-management-system](https://github.com/LuOzawa/internship-management-system) | 实习全流程 | **双导师审批流**；周报、评价体系 |

### 数据 / 算法

| 项目 | 业务 | 差异化技术点 |
|---|---|---|
| 🔒 [boss-zhipin-data-analysis](https://github.com/LuOzawa/boss-zhipin-data-analysis) | 招聘数据洞察 | Django + Selenium 采集；分词词云、KMeans 聚类、回归薪资预测 |
| [pf-mdd-yolov8-defect-detection](https://github.com/LuOzawa/pf-mdd-yolov8-defect-detection) | 工业缺陷检测 | 见主推项目 |
| [family-finance-tracker](https://github.com/LuOzawa/family-finance-tracker) | 家庭理财 | 见主推项目 |
| 🔒 🔒 [steel-surface-defect-detection](https://github.com/LuOzawa/steel-surface-defect-detection) | 钢材表面缺陷检测 | 见主推项目；YOLOv8 + SE 注意力，mAP@0.5 0.8291 |

### AI / 小程序 / 产品

| 项目 | 业务 | 差异化技术点 |
|---|---|---|
| 🔒 [ai-tutor-miniapp](https://github.com/LuOzawa/ai-tutor-miniapp) | AI 助教 | uni-app 微信小程序 + Spring Boot 3；DeepSeek 答疑、错题本 |
| [kip-agent](https://github.com/LuOzawa/kip-agent) | 桌面 AI Agent | TypeScript 技能体系、沙箱执行、CI + PR 流程 |
| 🔒 [shiji-website](https://github.com/LuOzawa/shiji-website) | 产品官网 | Vite + Cloudflare Workers 部署 |
| [shiji-releases](https://github.com/LuOzawa/shiji-releases) | 版本分发 | Mac 安装包分发仓库 |
| 🔒 [feishu-hub](https://github.com/LuOzawa/feishu-hub) | 飞书内部办公自动化 | **YAML 声明式低代码**：9 张多维表格 + 8 条工作流（幂等键/退避重试/审计/递归保护）；**开放平台集成**：token 缓存·频控退避·事件验签，Mock 与真实同构；**Aily + RAG**：意图路由·5 技能·护栏·引用溯源·兜底转人工；零第三方依赖内核 + 50 项测试 |

---

## 四、公共工程规范（21 个仓库一致）

```text
README.md          # 架构图 · 目录结构 · 接口一览 · 安全记录 · 已知问题
LICENSE            # MIT
.env.example       # 口令全部走环境变量，仓库内无明文密钥
backend/           # Maven / Flask 后端
frontend/          # Vue 3 前端
sql/               # 建库脚本（⚠️ 文件头标注 DROP 风险）
docs/              # 启动说明.md · 功能清单.md
.github/workflows/ # CI：mvn compile + npm build
```

- **可复现**：每个仓库 `docs/启动说明.md` 给出环境版本表、导入顺序、环境变量、默认账号；Python 依赖全部 `==` 精确锁定
- **有版本基线**：每个仓库打 `v1.0.0 — 答辩定稿版` tag 与 Release
- **无密钥泄露**：数据库口令、JWT secret 均为 `${ENV:default}` 形式
- **CI 全覆盖**：21/21 仓库 GitHub Actions（后端 `mvn test`/`pytest`，前端 `npm ci + build`；feishu-hub 为 `doctor + pytest + demo 冒烟`），日志可查测试通过数
- **有测试**：94 个自动化测试，聚焦"会出事的地方"（鉴权越权、token 失效、切块覆盖、异常信息泄露、财务算法边界、**工作流幂等/重试/事件验签/RAG 引用兜底**）
- **依赖安全**：Dependabot 告警全开；前端漏洞经 `npm audit fix` 从 ~150 降至 ~43，剩余均为需 breaking change 的 vite 主版本升级

---

## 五、自动化测试明细（94 个）

| 仓库 | 用例 | 覆盖重点 |
|---|---|---|
| study-material-recommender | 10 | JWT 签发/校验、**他人 token 越权拒绝**、过期拒绝、篡改拒绝、弱密钥启动即失败 |
| family-finance-tracker | 15 | 空数据兜底、聚合正确性、KMeans 样本边界、ARIMA 三级降级、健康评分四维规则 |
| pf-mdd-yolov8-defect-detection | 9 | 切块数量/尺寸、**全幅覆盖无空隙**、YOLO 框跨块映射、越界框丢弃、结果确定性 |
| internship-management-system | 5 | 全局异常处理器契约、**500 响应不泄露异常原文** |
| ai-tutor-miniapp | 5 | 同上 |
| feishu-hub | 50 | 表达式引擎（中文标识符/错误可诊断）、表格字段校验与公式、工作流**幂等与重试**、开放平台 **token 缓存/频控/事件验签**、**RAG 引用溯源与兜底**、权限行列级过滤 |

全部在 CI 中执行，日志可见 `Tests run: N, Failures: 0` / `N passed`。

## 六、本索引仓库自身的工程约定

```text
README.md              # 本文件（唯一内容）
projects.json          # 索引数据源：21 个项目的名称/可见性/分类/技术栈/亮点
scripts/check_index.py # 一致性自检：README ↔ projects.json ↔ 声明数量 ↔ 🔒 标记
scripts/check_links.py # 相对链接与锚点可达性检查（不联网，避免私有仓库误报）
.github/workflows/ci.yml  # CI：一致性自检 + Markdown 规范 + 链接检查
```

> 为什么要 `projects.json`：手写索引最容易出现「README 说 17 个、实际 20 个、还漏收一个主打项目」这种漂移。
> 现在**数量、收录、可见性标记全部由 manifest 决定，CI 每次提交都会核对**，漂移会直接让 CI 变红。

---

## 七、待补

- [ ] 各项目界面截图 / GIF（`docs/screenshots/`）
- [ ] 面试速查：每个项目的 Q&A（为什么这么设计、如果重做会怎么改）
- [x] 主推项目公开：`pf-mdd-yolov8-defect-detection`、`study-material-recommender`、`family-finance-tracker`、`gz-student-rental-recsys` 已转 public（其余保持 private，可邮件申请只读）
- [ ] 其余 11 个 Java 仓库补单测（当前仅 3 个有测试）
- [ ] 抽 `spring-vue-starter` 模板仓库，消除 10 个同构仓库的重复
- [ ] feishu-hub：接真实飞书租户验证「Mock 与真实同构」假设；补 90 秒演示录屏
