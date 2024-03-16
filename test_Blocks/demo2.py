import numpy as np
import gradio as gr

# with gr.Tab("Flip Text"):  # 设置tab选项卡
#     with gr.Column():  # 垂直排列
#         xxx
# with gr.Tab("Flip Image"):  # 设置tab选项卡
#     with gr.Row():  # 水平排列

# Blocks特有组件，设置所有子组件按水平排列
def flip_text(x):#翻转字符串
    return x[::-1]
def flip_image(x):
    return np.fliplr(x)
with gr.Blocks() as demo:
    #用markdown语法编辑输出一段话
    gr.Markdown("Flip text or image files using this demo.")

    with gr.Tab("Flip Text"):# 设置tab选项卡
        #Blocks特有组件，设置所有子组件按垂直排列(垂直排列是默认情况，不加也没关系)
        with gr.Column():#垂直排列
            text_input = gr.Textbox()
            text_output = gr.Textbox()
            text_button = gr.Button("Flip")
    with gr.Tab("Flip Image"):# 设置tab选项卡
        #Blocks特有组件，设置所有子组件按水平排列
        with gr.Row():#水平排列
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("Flip")
    #设置折叠内容
    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me...")
    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655