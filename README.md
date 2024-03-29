# JianYingDraft.PY

## 项目简介

项目来源于 `https://github.com/xiaoyiv/JianYingProDraft`
因为原始库旷日持久没有更新，所以自己动手丰衣足食，基于此项目进行二次开发。
虽说是二次开发，但跟原始项目相比早就“肝胆楚越也”，因此也就没有对原始项目进行fork。

▌参考资料：
剪映草稿文件的说明，另外可以参考文章：https://blog.csdn.net/a820206256/article/details/134428639

## 剪映的草稿原理说明

1. 实现原理 : 剪映的草稿文件是 `json` 的形式存储的。我们只需要创建`draft_content.json`和`draft_mate_info.json`
   ，其他文件则会在打开剪映软件后会自动补全。
   `draft_mate_info.json`内的素材信息会出现在剪映左侧的素材库中；两个文件内都记录了素材信息，`draft_content.json`
   的素材信息会出现在剪映下侧的时间线上。
2. 添加一个媒体素材到剪映软件，剪映会将其数据记录进入“草稿元数据库” 和 “草稿内容库”（包括素材部分和轨道部分）

## 本软件的实现原理说明

1. `add_media` 会识别媒体类型，加入到对应轨道。
2. 当没有视频轨道时，创建音频轨道会先创建视频轨道。

## 使用步骤与说明

1. 使用前先修改配置文件`_projectConfig.ini`内，剪映草稿文件夹路径为你本地正确的路径。
   ```shell
   drafts_root=Z:/jianying/Data/JianyingPro Drafts
   ```
2. 根据自己的需求修改`main.py`内的代码。运行`main.py`。
