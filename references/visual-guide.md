# 参考图怎么用

生成前实际查看图片，并把适用图片送入图像工具。GitHub 完整版附带图片；SkillHub 版通过公开链接补齐图片。

## 先取得参考图

1. 检查下表的本地图片。若缺失，执行 `python3 <技能目录>/scripts/fetch_references.py`。脚本仅依赖 Python 3 标准库，把图片下载到技能的 `references/` 目录，并按 [图片清单](images.json) 中的 SHA-256 校验。已有内容不同的图片不会被覆盖。
2. 没有 Python 但有下载工具时，使用清单中的完整 URL 下载，核对哈希，再用图像查看工具打开。URL 固定到 GitHub 的具体提交，不使用会变化的分支链接。
3. 网络不可达、下载失败或无法查看图片时，说明失败；可以让用户提供图片或安装 GitHub 完整版。不能静默退回纯文字猜测，更不能为了取图上传目标照片。
4. 图片在本地后，仍必须显式作为图像输入交给绘图工具。路径、URL 或 Markdown 链接仅写入提示词，不等于工具收到图像。

三张图片的公开下载地址：
- [single-layout.png](https://raw.githubusercontent.com/Leon0555/grok-bot-icon/73f7fcb4b9034af15255c35e3013a4d6fa2dc14e/references/single-layout.png)
- [pet-man-final.png](https://raw.githubusercontent.com/Leon0555/grok-bot-icon/73f7fcb4b9034af15255c35e3013a4d6fa2dc14e/references/pet-man-final.png)
- [pet-woman-final.png](https://raw.githubusercontent.com/Leon0555/grok-bot-icon/73f7fcb4b9034af15255c35e3013a4d6fa2dc14e/references/pet-woman-final.png)

## 参考范围

| 图片 | 用途 | 不借用的内容 |
| --- | --- | --- |
| [single-layout.png](single-layout.png) | 默认单人近景的脸型、头部倾斜、下巴与衣领的留白关系；仅看中间正方形插画 | 截图黑边、页码、关闭按钮、角色身份、服装、背景图案与文字 |
| [pet-man-final.png](pet-man-final.png) | 人宠合影的位置、大小关系、圆润脸型、自然颈长、猫脸结构 | 男生身份、眼镜配色、银灰猫、特定服装与背景色 |
| [pet-woman-final.png](pet-woman-final.png) | 同一套人宠合影的女生例子，长发与长毛宠物如何保持相近的基础脸部比例 | 女生身份、墨镜耳饰、橘白猫、特定服装与背景色 |

后两张是经过多轮修改后确认的一组成图，是视觉质量目标，但不是每个像素必须复制的几何模板。两张也不是数学意义上完全相同；用户指定其中一张为本轮基准时，才以它对齐。

若只制作单人图，首选单人构图参考。需要借用最终合影的圆脸画法时，可额外输入一张合影参考，但必须明确排除宠物、双主体布局与更长的颈部。

用户提供新的已认可参考时，其指定属性优先于技能示例。不要因为技能示例可用就替代用户指定的编辑底稿。
