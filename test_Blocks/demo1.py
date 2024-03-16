import gradio as gr
def greet(name):
    return "Hello " + name + "!"
with gr.Blocks() as demo:
    #设置输入组件
    name = gr.Textbox(label="Name")
    #设置输出组件
    output = gr.Textbox(label="Output Box")
    #设置按钮
    greet_btn = gr.Button("Greet")
    #设置按钮点击事件
    greet_btn.click(fn=greet, inputs=name, outputs=output)
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655