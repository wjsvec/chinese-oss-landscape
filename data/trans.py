import yaml
import os
import requests
from pathlib import Path
from download_svg import download_jpg_as_square_svg

def download_image(url, save_path):
    # send GET request
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 确保父文件夹存在
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        # 以二进制写入文件
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"图片已保存到 {save_path}")
    else:
        print(f"下载失败，状态码：{response.status_code}")
file_path = os.getcwd() +'/data/raw_data/index.yaml'
print(file_path)

with open(file_path, 'r') as file:
    data = yaml.safe_load(file)
count_l = 0
print(type(data))
for i in range(len(data)):
    # print(data[i]['name'])
    if ('logos'  in data[i]):

        image_url = "https://kaiyuanshe.cn/api/lark/file/"+data[i]['logos'][0]['file_token']
        save_file = "data/images/"+data[i]['name']+".svg"
        count_l+=1
        download_jpg_as_square_svg(image_url, save_file)

        
print(count_l)
# image_url = "https://kaiyuanshe.cn/api/lark/file/HYkmbui54ouFjTxxaTTcMpONnOf"  # 替换成你的JPG链接
# save_svg = "output_image.svg"
# download_jpg_as_square_svg(image_url, save_svg)






