import yaml
import os
import requests
from pathlib import Path
from download_svg import download_jpg_as_square_svg


file_path = os.getcwd() +'/data/raw_data/index.yaml'
print(file_path)

with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
count_l = 0
tag_type = dict()
type_d = ['法务合规', '实时数据集成', 'MLOps', '操作系统', '开源公益', '微服务', '机器学习', '合作社区', '工业互联网', 'RISC-V', '移动客户端', '编程语言', 'DevOps（CI/CD）', '开源布道', '后端', '数据库', '区块链', '软件供应链安全', '物联网', '云计算', '云原生', '大数据', '企业管理', '人工智能', '赞助伙伴', '开源教育', 'HPC（高性能计算）', '中间件', 'Web 前端', '桌面客户端']
for d in type_d:
    tag_type[d] = []

print(type(data))
for i in range(len(data)):
    # print(data[i]['name'])
    if ('logos'  in data[i]):
        if( 'tags' in data[i]):
            for tag in data[i]['tags']:
                tag_type[tag].append(data[i]['name'])

        



print(tag_type)
# image_url = "https://kaiyuanshe.cn/api/lark/file/HYkmbui54ouFjTxxaTTcMpONnOf"  # 替换成你的JPG链接
# save_svg = "output_image.svg"
# download_jpg_as_square_svg(image_url, save_svg)






