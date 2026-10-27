<div align="center">

# 毕业设计作品集 · Graduation Projects

**22 个项目** · Spring Boot + Vue 3 全栈 / 计算机视觉 / 推荐系统 / 数据分析 / AI Agent / 低代码 AI 办公

</div>

这些是我自己从头写完的项目：前后端分离、真实数据库、能跑起来，每个仓库都带启动说明和部署脚本。

大部分仓库是私有的（毕业设计 / 还在做的产品），🔒 标记的就是；**没标记的那几个可以直接 clone 下来跑**。
想看源码或者需要完整代码，发邮件找我就行。

---

## 怎么看

- **想找方向**：先看下面「按方向分」，对上了就去翻对应仓库；
- **想看工程细节**：「每个仓库都做了些什么」里写了统一规范，测试覆盖在「测试都测些什么」；
- **想直接跑**：挑没标 🔒 的，`git clone` 之后照着仓库里的 `docs/启动说明.md` 走就行。

## 按方向分

| 方向 | 项目 | 用到的技术 |
|---|---|---|
| **AI / Agent** | [kip-agent](https://github.com/LuOzawa/kip-agent) · [langgraph-multi-agent](https://github.com/LuOzawa/langgraph-multi-agent) · 🔒 [ai-tutor-miniapp](https://github.com/LuOzawa/ai-tutor-miniapp) | TypeScript 技能体系 / 沙箱 / DeepSeek / **LangGraph Supervisor 调度 + 审批门 + 检查点** / 微信小程序 |
| **低代码 / AI 办公** | 🔒 [feishu-hub](https://github.com/LuOzawa/feishu-hub) | 飞书多维表格 / YAML 工作流编排 / Aily 智能伙伴 / RAG 问答 / 权限与审计 |
| **计算机视觉** | [pf-mdd-yolov8-defect-detection](https://github.com/LuOzawa/pf-mdd-yolov8-defect-detection) · 🔒 [steel-surface-defect-detection](https://github.com/LuOzawa/steel-surface-defect-detection) | YOLOv8 / 宽幅图切块 / 滑窗推理融合 / SE 通道注意力 |
| **推荐系统** | [study-material-recommender](https://github.com/LuOzawa/study-material-recommender) · [gz-student-rental-recsys](https://github.com/LuOzawa/gz-student-rental-recsys) | UserCF / ItemCF / SVD / TF-IDF / 协同过滤 + 地理距离混合召回 |
| **数据分析** | 🔒 [boss-zhipin-data-analysis](https://github.com/LuOzawa/boss-zhipin-data-analysis) · [family-finance-tracker](https://github.com/LuOzawa/family-finance-tracker) | Selenium 采集 / 分词词云 / KMeans / 线性回归 / ARIMA |
| **企业级全栈** | 10 个项目（见下） | Spring Boot + Vue 3 + MyBatis-Plus + JWT/RBAC |
| **产品工程** | 🔒 [shiji-website](https://github.com/LuOzawa/shiji-website) · [shiji-releases](https://github.com/LuOzawa/shiji-releases) | Vite / Cloudflare Workers / 版本分发 |

---

## 项目清单

### 企业级全栈（Spring Boot + Vue 3）

| 项目 | 做什么的 | 亮点 |
|---|---|---|
| 🔒 [shop-platform](https://github.com/LuOzawa/shop-platform) | 电商平台 | Spring Boot 2.7 / Java 11；订单状态机、优惠券、支付流程 |
| 🔒 [pharmacy-management](https://github.com/LuOzawa/pharmacy-management) | 药店管理 | 员工端 + 会员端双端；库存预警、处方登记、会员积分 |
| 🔒 [traffic-repair-platform](https://github.com/LuOzawa/traffic-repair-platform) | 交通设施报修 | **RBAC 工单流转**：报修 → 审核 → 派单 → 维修 → 验收 → 申诉；前端产物打进 jar 单包部署 |
| 🔒 [community-suggestion-box](https://github.com/LuOzawa/community-suggestion-box) | 社区意见箱 | Spring Boot 2.7 / Java 8；Spring Security 三端权限隔离 |
| 🔒 [elder-health-management](https://github.com/LuOzawa/elder-health-management) | 老年健康管理 | **ADL-MMSE 量表评估**；慢病随访、预约挂号、健康指标趋势 |
| 🔒 [pet-center-management](https://github.com/LuOzawa/pet-center-management) | 宠物综合服务 | Sa-Token 三端隔离（用户/商家/管理员）；寄养、套餐、商城 |
| 🔒 [liupanshui-tourism](https://github.com/LuOzawa/liupanshui-tourism) | 云上凉都·六盘水文旅 | 游客端 15 模块 + 后台 13 模块；ECharts 数据看板 |
| 🔒 [jiufeng-park-management](https://github.com/LuOzawa/jiufeng-park-management) | 鹫峰森林公园运营 | **生态监测阈值告警**；在线购票、入园预约 |
| 🔒 [physical-fitness-test-system](https://github.com/LuOzawa/physical-fitness-test-system) | 高校体质测试 | 体测申请 / 审核 / 成绩录入 / 统计导出；单表大数据量分页 |
| 🔒 [internship-management-system](https://github.com/LuOzawa/internship-management-system) | 实习生全流程管理 | **双导师审批流**；周报、评价体系 |

### 数据 / 算法

| 项目 | 做什么的 | 亮点 |
|---|---|---|
| 🔒 [boss-zhipin-data-analysis](https://github.com/LuOzawa/boss-zhipin-data-analysis) | 招聘数据洞察 | Django + Selenium 采集；分词词云、KMeans 聚类、回归薪资预测 |
| [pf-mdd-yolov8-defect-detection](https://github.com/LuOzawa/pf-mdd-yolov8-defect-detection) | 塑料薄膜表面缺陷检测 | YOLOv8 + 宽幅图切块，12 类缺陷，滑窗推理融合 |
| [family-finance-tracker](https://github.com/LuOzawa/family-finance-tracker) | 家庭理财记账 | KMeans 消费聚类 + ARIMA 支出预测 + 四维财务健康评分 |
| 🔒 [steel-surface-defect-detection](https://github.com/LuOzawa/steel-surface-defect-detection) | 钢材表面缺陷检测 | YOLOv8 + SE 通道注意力，mAP@0.5 0.8291（+1.8 pt） |

### AI / 小程序 / 产品

| 项目 | 做什么的 | 亮点 |
|---|---|---|
| 🔒 [ai-tutor-miniapp](https://github.com/LuOzawa/ai-tutor-miniapp) | AI 助教 | uni-app 微信小程序 + Spring Boot 3；DeepSeek 答疑、作业批改、错题本 |
| [kip-agent](https://github.com/LuOzawa/kip-agent) | 桌面 AI Agent | TypeScript 技能体系、沙箱执行、CI + PR 流程 |
| [langgraph-multi-agent](https://github.com/LuOzawa/langgraph-multi-agent) | LangGraph 多 Agent 协作框架 | Supervisor 调度专家，专家可带工具；专家级/工具级人工审批、SQLite 检查点断点续跑、失败隔离、上下文 token 裁剪、22 个离线测试 |
| 🔒 [shiji-website](https://github.com/LuOzawa/shiji-website) | 拾机官网 | Vite + Cloudflare Workers 部署 |
| [shiji-releases](https://github.com/LuOzawa/shiji-releases) | 拾机版本分发 | Mac 安装包分发仓库 |
| 🔒 [feishu-hub](https://github.com/LuOzawa/feishu-hub) | 飞书内部办公自动化 | **配置驱动**：9 张多维表格 + 8 条工作流（幂等、退避重试、审计）；**开放平台集成**：token 缓存、频控退避、事件验签，离线 Mock 与真实接口同构；**Aily + RAG**：意图路由、5 个技能、护栏、引用溯源、没有依据就转人工；零第三方依赖内核 + 50 项测试 |

---

## 每个仓库都做了些什么

```text
README.md          # 架构图 · 目录结构 · 接口一览 · 安全记录 · 已知问题
LICENSE            # MIT
.env.example       # 口令全走环境变量，仓库里没有明文密钥
backend/           # Maven / Flask 后端
frontend/          # Vue 3 前端
sql/               # 建库脚本（⚠️ 文件头标了 DROP 风险）
docs/              # 启动说明.md · 功能清单.md
.github/workflows/ # CI：mvn compile + npm build
```

- **能照着跑起来**：`docs/启动说明.md` 里写了环境版本、导入顺序、环境变量和默认账号，Python 依赖用 `==` 锁死；
- **有版本基线**：每个仓库都有 `v1.0.0` tag 和对应的 Release；
- **不泄密钥**：数据库口令、JWT secret 都是 `${ENV:default}` 这种写法；
- **CI 都跑着**：22 个仓库都有 GitHub Actions（后端 `mvn test` / `pytest`，前端 `npm ci + build`；`feishu-hub` 跑的是 `doctor + pytest + demo`），日志里能直接看到测试通过数；
- **依赖有人盯**：Dependabot 全开；前端漏洞从 ~150 降到 ~43，剩下的都是要 breaking change 的 vite 主版本升级。

## 测试都测些什么

一共 94 个自动化测试，写的都是「真会出事」的地方：

| 仓库 | 用例 | 覆盖重点 |
|---|---|---|
| study-material-recommender | 10 | JWT 签发 / 校验、**别人的 token 越权拒绝**、过期拒绝、篡改拒绝、弱密钥启动就失败 |
| family-finance-tracker | 15 | 空数据兜底、聚合正确性、KMeans 样本边界、ARIMA 三级降级、健康评分四维规则 |
| pf-mdd-yolov8-defect-detection | 9 | 切块数量 / 尺寸、**全幅覆盖没有空隙**、YOLO 框跨块映射、越界框丢弃、结果确定性 |
| internship-management-system | 5 | 全局异常处理器契约、**500 响应不泄露异常原文** |
| ai-tutor-miniapp | 5 | 同上 |
| feishu-hub | 50 | 表达式引擎（中文标识符、错误可诊断）、字段校验与公式、工作流**幂等与重试**、开放平台 **token 缓存 / 频控 / 事件验签**、**RAG 引用溯源与兜底**、权限行列级过滤 |

全部在 CI 里跑，日志能看到 `Tests run: N, Failures: 0` / `N passed`。

---

## 这份索引怎么维护

项目清单的真实来源是 `projects.json`，`scripts/check_index.py` 会核对 README 和它是否对得上
（项目数量、收录情况、🔒 标记），`scripts/check_links.py` 检查相对链接和锚点，两项都在 CI 里。
加新项目只要改 `projects.json` 和 README 对应的表，CI 会挡住写错的地方。

> 一开始这里是手写的 Markdown，加过几次项目就出现了「说 17 个、实际 20 个、还漏收一个」的情况，
> 所以干脆把清单抽成了数据源，让机器来盯。

---

## 联系我

邮箱：[linlin700573@gmail.com](mailto:linlin700573@gmail.com) · 广州

私有仓库如果需要查看，邮件说明用途就行。
