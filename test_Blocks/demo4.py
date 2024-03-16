import gradio as gr
import numpy as np
import time
#生成steps张图片，每隔1秒钟返回
def fake_diffusion(steps):
    for i in range(steps):
        time.sleep(1)
        image = np.random.randint(255, size=(300, 600, 3))
        yield image
demo = gr.Interface(fake_diffusion,
                    #设置滑窗，最小值为1，最大值为10，初始值为3，每次改动增减1位
                    inputs=gr.Slider(1, 10, value=3, step=1),
                    outputs="image")
#生成器必须要queue函数
demo.queue()
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655