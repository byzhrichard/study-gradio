import gradio as gr

with gr.Blocks() as demo:
    input_textbox = gr.Textbox()
    gr.Examples(["hello", "bonjour", "merhaba"], input_textbox)
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655