import yaml
from gen_data_by_cate import gen_data_by_cate

data = {
        "categories": [
            
        ]
}
tag_type = dict()
type_d = ['法务合规', '实时数据集成', 'MLOps', '操作系统', '开源公益', '微服务', '机器学习', '合作社区', '工业互联网', 'RISC-V', '移动客户端', '编程语言', 'DevOps（CI/CD）', '开源布道', '后端', '数据库', '区块链', '软件供应链安全', '物联网', '云计算', '云原生', '大数据', '企业管理', '人工智能', '赞助伙伴', '开源教育', 'HPC（高性能计算）', '中间件', 'Web 前端', '桌面客户端']
for d in type_d:
    tag_type[d] = []
for i in range(len(type_d)):
    data["categories"].append(gen_data_by_cate(type_d[i], type_d[i]))
with open("data/data.yml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)
print("done!")
