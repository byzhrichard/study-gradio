import gradio as gr
def submit(name, age, symptoms):
    if len(name) == 0:
        return {error_box: gr.update(value="请输入名字", visible=True)}#使出错框显示
    if age < 0 or age > 200:
        return {error_box: gr.update(value="非法的年龄", visible=True)}#使出错框显示
    return {
        output_col: gr.update(visible=True),
        diagnosis_box: "covid" if "Cough" in symptoms else "flu",
        patient_summary_box: f"{name}, {age} y/o"
    }
with gr.Blocks() as demo:
    # 出错提示框
    error_box = gr.Textbox(label="Error", visible=False)
    # 输入框
    name_box = gr.Textbox(label="Name")
    age_box = gr.Number(label="Age")
    symptoms_box = gr.CheckboxGroup(["Cough", "Fever", "Runny Nose"])
    submit_btn = gr.Button("Submit")
    # 输出不可见
    with gr.Column(visible=False) as output_col:###########
        diagnosis_box = gr.Textbox(label="Diagnosis")
        patient_summary_box = gr.Textbox(label="Patient Summary")
    submit_btn.click(
        submit,
        [name_box, age_box, symptoms_box],
        [error_box, diagnosis_box, patient_summary_box, output_col],
    )
demo.launch()
# ————————————————
# 版权声明：本文为CSDN博主「汀、人工智能」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/sinat_39620217/article/details/130343655