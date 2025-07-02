import yaml
import os
from download_svg import download_jpg_as_square_svg

def gen_data_by_cate(category: str, subcategory: str) -> list:
    file_path = os.getcwd() +'/data/raw_data/index.yaml'
    # print(file_path)
    item_types = []
    with open(file_path, 'r') as file:
        raw_data = yaml.safe_load(file)
    data = {
        "categories": [
            {
                "name":category,
                "subcategories": [
                    {
                        "name": subcategory,
                        "items": [
                            
                        ]
                    }
                ]
            }
        ]
    }
    re_cate ={
                "name":category,
                "subcategories": [
                    {
                        "name": subcategory,
                        "items": [
                            
                        ]
                    }
                ]
            }



    count_l = 0
    test_seb = []
    temp_item = {}
    for i in range(len(raw_data)):
        # print(data[i]['name'])
        if(raw_data[i]['name'] not in temp_item and 'logos'  in raw_data[i] and 'tags' in raw_data[i] ):
            if(subcategory  in raw_data[i]['tags']):
                if ('logos'  in raw_data[i]):
                    item_info = {
                    "name":raw_data[i]['name']+"_no_"+str(i),
                    "logo": raw_data[i]['name']+".svg",
                    # "crunchbase": "https://www.crunchbase.com/organization/cloud-native-computing-foundation",
                    "description": "This is the description of item",
                    "homepage_url": "https://cncf.io",
                    "project": "graduated",
                    # "repo_url": "https://github.com/cncf/landscape2",
                    # "twitter": "https://twitter.com/CloudNativeFdn"
                    
                    }
                if('summary' in raw_data[i]):
                    item_info["description"] = raw_data[i]['summary']
                if('link' in raw_data[i]):
                    item_info["homepage_url"] = raw_data[i]['link']['link']
                if('codeLink' in raw_data[i]):
                    item_info["repo_url"] = raw_data[i]['codeLink']['link']
                test_seb.append(item_info)
                temp_item[raw_data[i]['name']] = 1

    data["categories"][0]["subcategories"][0]["items"].extend(test_seb)
    re_cate["subcategories"][0]["items"].extend(test_seb)
    print(subcategory+":",end ="")
    print(len(data["categories"][0]["subcategories"][0]["items"]))
    
    if("/" in category):
        category = category.replace("/", "_")
    with open("data/cate/"+category+".yml", "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

    return re_cate
    # print(count_l)
    # image_url = "https://kaiyuanshe.cn/api/lark/file/UWJhbR9zOoIzohxNS48c1B0vnHw"  # 替换成你的JPG链接
    # save_svg = "output_image.svg"
    # download_jpg_as_square_svg(image_url, save_svg)





