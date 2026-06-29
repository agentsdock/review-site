# review-site 项目规范

## 项目定位

这是一个 Hugo 静态站点项目，用于生成和维护 review-site 内容。

## 目录约定

- `content/`：站点文章与页面内容
- `layouts/`：Hugo 模板
- `assets/`：需要 Hugo 处理的资源文件
- `static/`：直接复制到站点根目录的静态资源
- `config/`：Hugo 配置
- `public/`：Hugo 构建输出，不作为源代码维护
- `themes/`：主题目录
- `archetypes/`：内容模板
- `data/`：Hugo 数据文件

## 文件命名

- 内容文件使用小写英文、数字和连字符命名，例如 `example-post.md`
- 脚本文件使用英文命名，保持现有风格

## Git 约定

- 不提交系统文件、临时文件、构建缓存、密钥或 token
- `public/` 是构建产物，默认不提交，除非明确要求用仓库托管静态产物
- 修改项目结构前先更新本文件

## 验证

- 内容或模板变更后，优先运行 Hugo 构建验证
- 如果本机没有 Hugo，说明未验证原因，不伪造通过结果
