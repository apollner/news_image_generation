# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**K-pop star Taeil quits NCT boy band over sex crime accusation: What we know**

You can read more about it [here](https://news.google.com/rss/articles/CBMitgFBVV95cUxNR3pRRmd1TFY0YTZYMmgwTkpRYmNUYm4tOFphQTExdHlJMEZJbnJPYld2d0hKeTBwZ2FXRTZKV0R5SXhRZzFrSlc1VUVSZG5ha2xuRHVIb2lEQ0hOZld4Q29SZEo1RF9YX0JHRTlqYUhNUVFYRlVGRDFsd3JHb3lFZUl5LVhHUUhSMmFMMHgyaG8yT1N1clR4enpnOFNNanVoeVBHTHBDOEJkRzVGS19ocE5ka2l3UdIBuwFBVV95cUxOdlRkVnNfaHNaZzZ4TUI3U3NnZmJ2OHhfOXN0RXQ4ZFM2a2UzM1I1UVVBX0pvakt3MFRGTWtOUDc3ZWRCOGNMcGRIaWlUb0J1YU9CSTA1SEIzREdfdUhVdC00YW5hb3BLRlFwWUJKLTNwZ1p2SFpuLXZOZzBtcndEOHdHUFJtdGd3cHROZFlYM3d3UnZnOS1sdU9iSV83RTFNSXVIQm5heHg1MVJNUEhIWXByZVI3dXF5cGxN?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
