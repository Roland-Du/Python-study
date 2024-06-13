from PIL import Image

# 灰度字符集，按灰度值从低到高排列
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    # 获取原始图像的宽度和高度
    width, height = image.size
    # 计算新的高度，以保持图像的宽高比
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    # 调整图像大小，使用LANCZOS重采样过滤器
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return resized_image

def grayify(image):
    # 将图像转换为灰度图
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    # 获取图像的像素数据
    pixels = image.getdata()
    # 将每个像素转换为相应的字符
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    try:
        # 打开图像文件
        image = Image.open(image_path)
    except Exception as e:
        # 如果图像文件无法打开，打印错误信息
        print(e)
        return

    # 调整图像大小
    image = resize_image(image, new_width)
    # 将图像转换为灰度图
    image = grayify(image)
    # 将灰度图像转换为ASCII字符
    ascii_str = pixels_to_ascii(image)

    # 获取图像的宽度
    img_width = image.width
    # 获取ASCII字符串的长度
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # 将ASCII字符串格式化为多行字符串，每行的宽度与图像的宽度相同
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i + img_width] + "\n"

    return ascii_img
