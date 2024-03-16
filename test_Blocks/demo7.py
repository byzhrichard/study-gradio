import gradio as gr
#可以正常用,报错是因为不建议两个click使用同一个方法,但是无所谓
def increase(num):
    return num + 1
with gr.Blocks() as demo:
    a = gr.Number(label="a")
    b = gr.Number(label="b")
    # 要想b>a，则使得b = a+1
    atob = gr.Button("b > a")
    atob.click(increase, a, b)
    # 要想a>b，则使得a = b+1
    btoa = gr.Button("a > b")
    btoa.click(increase, b, a)
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655