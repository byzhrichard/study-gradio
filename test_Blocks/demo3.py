import gradio as gr
import numpy as np





with gr.Blocks() as demo:
    gr.Image(width=12,height=123)
demo.queue()
demo.launch()