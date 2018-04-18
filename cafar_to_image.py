import pickle as p
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as plimg
from PIL import Image


# import sys
#
# sys.setdefaultencoding('utf8')


def load_CIFAR_batch(filename):
    """ load single batch of cifar """
    with open(filename, 'rb')as f:
        datadict = p.load(f, encoding='iso-8859-1')
        X = datadict['data']
        Y = datadict['labels']
        X = X.reshape(10000, 3, 32, 32)
        Y = np.array(Y)
        return X, Y


def load_CIFAR_Labels(filename):
    with open(filename, 'rb') as f:
        lines = [x for x in f.readlines()]
        print(lines)


if __name__ == "__main__":
    load_CIFAR_Labels("./cifar-10-batches-py/batches.meta")
    imgX, imgY = load_CIFAR_batch("./cifar-10-batches-py/test_batch")
    print(imgY.shape)
    print(imgX.shape)
    print("正在保存图片:")
    for i in range(imgX.shape[0]):
        imgs = imgX[i - 1]
        if i < 1000:  # 只循环100张图片,这句注释掉可以便利出所有的图片,图片较多,可能要一定的时间
            img0 = imgs[0]
            img1 = imgs[1]
            img2 = imgs[2]
            i0 = Image.fromarray(img0)
            i1 = Image.fromarray(img1)
            i2 = Image.fromarray(img2)
            img = Image.merge("RGB", (i0, i1, i2))
            name = "img" + str(i)
            img.save("./cifar-10-batches-py/testimg/" + name, "png")  # 文件夹下是RGB融合后的图像
            for j in range(imgs.shape[0]):
                img = imgs[j - 1]
                name = "img" + str(i) + str(j) + ".png"
                print("正在保存图片" + name)
                plimg.imsave("./cifar-10-batches-py/testimg/" + name, img)  # 文件夹下是RGB分离的图像

    print("保存完毕.")