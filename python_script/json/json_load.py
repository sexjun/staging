import json

# json.dumps: 将 Python 对象编码成 JSON 字符串
# json.loads: 将已编码的 JSON 字符串解码为 Python 对象


# 将json文件转python对象····
def load_file_2_json(file_path):
    with open(file_path) as f:
        return json.loads(f.read())


# 将python对象转为json····
def load_obj_2_json(object):
    return json.dumps(obj=object,
                      indent=4,
                      sort_keys=False,
                      separators=(',', ': '))


# 将 python对象存为json格式
def save_py_obj_2_json_file(obj, file_path):
    with open(file_path, "w") as f:
        f.write(load_obj_2_json(obj))
    print(f"wirt obj info to file {file_path}")


# 测试上面三个函数接口
def test():
    print(load_file_2_json("./test_data.json"))
    str = load_obj_2_json(load_file_2_json("./test_data.json"))
    print(str)
    save_py_obj_2_json_file(str, "./test_save,json")
