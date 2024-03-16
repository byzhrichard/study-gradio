import gradio as gr
def eat(food):
    if food > 0:
        return food - 1, "full"
    else:
        return 0, "hungry"
    
with gr.Blocks() as demo:
    food_box = gr.Number(value=10, label="Food Count")
    status_box = gr.Textbox()
    gr.Button("EAT").click(
        fn=eat,
        inputs=food_box,
        #根据返回值改变输入组件和输出组件
        outputs=[food_box, status_box]
    )
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655