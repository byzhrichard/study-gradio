import gradio as gr
import pandas as pd
from ultralytics import YOLO


model = YOLO('yolov8n-cls.pt')
def predict(img):
    result = model.predict(source=img)
    df = pd.Series(result[0].names).to_frame()
    df.columns = ['names']
    df['probs'] = result[0].probs
    df = df.sort_values('probs', ascending=False)
    res = dict(zip(df['names'], df['probs']))
    return res


gr.close_all()
demo = gr.Interface(fn=predict, inputs=gr.Image(type='pil'), outputs=gr.Label(num_top_classes=5),
                    examples=['lion.jpg', 'lion.jpg', 'lion.jpg'])
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / sinat_39620217 / article / details / 130343655