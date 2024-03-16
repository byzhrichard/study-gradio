import gradio as gr
# 这里用的是id属性设置
with gr.Blocks(css="#warning {background-color: red}") as demo:
    box1 = gr.Textbox(value="Good Job", elem_id="warning")
    box2 = gr.Textbox(value="Failure")
    box3 = gr.Textbox(value="None", elem_id="warning")
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655