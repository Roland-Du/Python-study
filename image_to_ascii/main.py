import sys  # 导入sys模块以处理命令行参数
from utils import convert_image_to_ascii  # 导入我们之前定义的convert_image_to_ascii函数

def main(image_path, new_width=100):
    # 将图像转换为ASCII艺术
    ascii_image = convert_image_to_ascii(image_path, new_width)
    if ascii_image:
        # 如果转换成功，将ASCII艺术写入文件
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)
        print("ASCII art written to ascii_image.txt")

# 如果此脚本是作为主程序运行的
if __name__ == "__main__":
    # 检查命令行参数的数量
    if len(sys.argv) != 2:
        # 如果参数数量不对，打印使用提示
        print("Usage: python main.py <image_path>")
    else:
        # 获取图像路径
        image_path = sys.argv[1]
        # 调用main函数进行处理
        main(image_path)
