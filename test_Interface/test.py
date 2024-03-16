import gradio as gr

def image_classifier(inp):
    return inp

demo = gr.Interface(fn=image_classifier, inputs=gr.Checkbox(label="awa"), outputs="text")
demo.launch()