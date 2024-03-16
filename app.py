import numpy as np
import gradio as gr

def flip_text(a1,a2,a3,a4,a5,a6,a7,a8,a9):#翻转字符串
    inputs = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
    for i in range(len(inputs)):
        if inputs[i] == "":
            inputs[i] = "0"
    mat = (inputs[0]+" "+inputs[1]+" "+inputs[2]+";"+
           inputs[3]+" "+inputs[4]+" "+inputs[5]+";"+
           inputs[6]+" "+inputs[7]+" "+inputs[8])
    mat = np.mat(mat)
    zhi = np.linalg.matrix_rank(mat)
    try:
        inverse = np.linalg.inv(mat)
        inverse = inverse.flatten()
        outputs = inverse.tolist()[0]
        outputs.append(f"秩：{zhi}")
    except:
        outputs = ["不可逆","不可逆","不可逆","不可逆","不可逆","不可逆","不可逆","不可逆","不可逆"]
        outputs.append(f"秩：{zhi}")

    return outputs
def flip_image(x):
    return np.fliplr(x)
with gr.Blocks() as demo:
    with gr.Tab("3x3"):# 设置tab选项卡
        #Blocks特有组件，设置所有子组件按垂直排列(垂直排列是默认情况，不加也没关系)
        with gr.Row():
            with gr.Column():#垂直排列
                with gr.Row():
                    text_1 = gr.Textbox()
                    text_2 = gr.Textbox()
                    text_3 = gr.Textbox()
                with gr.Row():
                    text_4 = gr.Textbox()
                    text_5 = gr.Textbox()
                    text_6 = gr.Textbox()
                with gr.Row():
                    text_7 = gr.Textbox()
                    text_8 = gr.Textbox()
                    text_9 = gr.Textbox()
                text_btn = gr.Button("Flip")
            with gr.Column():#垂直排列
                with gr.Row():
                    text_o1 = gr.Textbox()
                    text_o2 = gr.Textbox()
                    text_o3 = gr.Textbox()
                with gr.Row():
                    text_o4 = gr.Textbox()
                    text_o5 = gr.Textbox()
                    text_o6 = gr.Textbox()
                with gr.Row():
                    text_o7 = gr.Textbox()
                    text_o8 = gr.Textbox()
                    text_o9 = gr.Textbox()
                text_o10 = gr.Textbox("秩:")

    with gr.Tab("4x4"):# 设置tab选项卡
        #Blocks特有组件，设置所有子组件按水平排列
        with gr.Row():#水平排列
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("Flip")
    #设置折叠内容
    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me...")
    text_btn.click(flip_text, inputs=[text_1,text_2,text_3,
                                      text_4,text_5,text_6,
                                      text_7,text_8,text_9], outputs=[text_o1,text_o2,text_o3,
                                                                      text_o4,text_o5,text_o6,
                                                                      text_o7,text_o8,text_o9,text_o10])
    image_button.click(flip_image, inputs=image_input, outputs=image_output)
demo.launch()
