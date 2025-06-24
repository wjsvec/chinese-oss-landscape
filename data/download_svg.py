import requests
from io import BytesIO
from PIL import Image
import base64

def download_jpg_as_square_svg(url, save_path):
        # 1. 请求图片
    response = requests.get(url)
    response.raise_for_status()
    content_type = response.headers.get('Content-Type', '').lower()

    # 判断是不是svg格式
    if 'svg' in content_type or url.lower().endswith('.svg'):
        print("检测到SVG图片，直接保存",end="")
        # 直接按二进制保存SVG文件
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"SVG图片已保存到: {save_path}")
        return

    # 下面处理位图格式（假设原图是jpg或其他位图）

    # 2. 打开位图
    original_img = Image.open(BytesIO(response.content)).convert("RGBA")
    w, h = original_img.size
    size = max(w, h)

    # 3. 新建正方形透明画布
    square_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))

    # 4. 图片居中粘贴
    paste_x = (size - w) // 2
    paste_y = (size - h) // 2
    square_img.paste(original_img, (paste_x, paste_y))

    # 5. 保存成内嵌PNG的SVG
    buffered = BytesIO()
    square_img.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()

    svg_content = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}">
  <image href="data:image/png;base64,{img_b64}" width="{size}" height="{size}"/>
</svg>
"""

    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)

    print(f"图片已处理为正方形SVG并保存到: {save_path}")

# 使用示例
# image_url = "https://kaiyuanshe.cn/api/lark/file/UWJhbR9zOoIzohxNS48c1B0vnHw"  # 替换成你的JPG链接
# save_svg = "output_image.svg"
# download_jpg_as_square_svg(image_url, save_svg)