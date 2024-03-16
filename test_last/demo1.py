#报错
import gradio as gr
from transformers import pipeline

pipe = pipeline("text-classification")

def clf(text):
    result = pipe(text)
    label = result[0]['label']
    score = result[0]['score']
    res = {label: score, 'POSITIVE' if label == 'NEGATIVE' else 'NEGATIVE': 1 - score}
    return res

demo = gr.Interface(fn=clf, inputs="text", outputs="label")
gr.close_all()
demo.launch(share=True)
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / sinat_39620217 / article / details / 130343655