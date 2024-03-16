import random
import gradio as gr
def chat(message, history):
    # history代表界面的状态(一开始为0,故赋值为[]   之后都是等于自身)
    history = history or []
    if message.startswith("how many"):
        response = f"{random.randint(1, 10)}"
    elif message.startswith("how"):
        response = random.choice(["Great", "Good", "Okay", "Bad"])
    elif message.startswith("where"):
        response = random.choice(["Here", "There", "Somewhere"])
    else:
        response = "I don't know"
    history.append((message, response))#history中添加元组
    return history, history
#设置一个对话窗
demo = gr.Interface(
    chat,
    # 添加state组件
    ["text", "state"],
    [gr.Chatbot(), "state"],
    # 设置没有保存数据的按钮
    allow_flagging="never",
    live=True
)
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655