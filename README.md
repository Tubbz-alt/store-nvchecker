# Deepin 商店软件上游更新检测

## 机制简述
采用nvchecker检测上游版本号，nvchecker的具体用法见[nvchecker](https://github.com/lilydjwg/nvchecker)

本项目的配置文件为store.ini, 用于定义需要检测包的上游

store_nvtake.py为nvtake脚本，用于在仓库合并之后通过rr任务的data.json文件更新版本状态，保存至old_ver.txt

## 流程
在jenkins定时任务中执行`nvchecker store.ini`显示结果，建立一个rr合并任务的下游任务拉取data.json并执行store_nvtake.py，两个任务需共用一个old_ver.txt使数据共通
