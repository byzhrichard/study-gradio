import gradio as gr
def change_textbox(awa):
    #根据不同输入对输出控件进行更新
    if awa == "short":
        return gr.update(lines=2, visible=True, value="Short story: ")
    elif awa == "long":
        return gr.update(lines=8, visible=True, value="Long story...")
    else:
        return gr.update(visible=False)
with gr.Blocks() as demo:
    radio = gr.Radio(
        ["short", "long", "none"], label="Essay Length to Write?"
    )
    text = gr.Textbox(lines=2, interactive=True)
    radio.change(fn=change_textbox, inputs=radio, outputs=text)
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655