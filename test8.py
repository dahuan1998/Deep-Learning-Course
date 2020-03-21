from PIL import Image
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
img=Image.open("lena.tiff")
img_r,img_g,img_b=img.split()
plt.figure(figsize=(10,10))

plt.subplot(221)
img_s=img_r.resize((50,50))
plt.axis("off")
plt.imshow(img_s,cmap="gray")
plt.title("R-缩放",fontsize=14)

plt.subplot(222)
img_gf=img_g.transpose(Image.FLIP_LEFT_RIGHT)
img_G=img_gf.transpose(Image.ROTATE_270)
plt.imshow(img_G,cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
plt.axis("off")
img_bc=img_b.crop((0,0,150,150))
plt.imshow(img_b,cmap="gray")
plt.title("B-裁剪",fontsize=14)

plt.subplot(224)
plt.axis("off")
img_rgb=Image.merge("RGB",[img_r,img_g,img_b])
plt.imshow(img_rgb)
plt.title("RGB",fontsize=14)
img_rgb.save("test.png")

plt.suptitle("图像基本操作",fontsize=20,color="b")
plt.show()