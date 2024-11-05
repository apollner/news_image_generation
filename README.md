# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Apple To Release iOS 18.2 Update Earlier Than Expected, As The Company Desperately Wants Apple Intelligence To Make A Difference On The iPhone**

You can read more about it [here](https://news.google.com/rss/articles/CBMifEFVX3lxTE05QnYtbkwwTEVGdnBvWVZaU2REUXo3R2w0MFlIYWNZY2VUWU9yd0dTYzVIU1RDRzM1ME5aV3NoMVZtTTByVUhhU21ZbmRTa3BGb09nUndfN3BWZ05rYno5RE5JbVRBeWdXbEhWSXU5N2dXZ0lIVF9zWnREYWTSAYIBQVVfeXFMTVgyRTFvVUtFWF82Z3dNYTVtXzRpUGwydjlJM2cxemUtVndzUEZabmtTeGtvRlJfSVc0OEFGN0lENExOZWJaTWFXYUVzLW5RYmdKdDJ5MGlXa0wwZ01lQkRBQVlTbWJMMGlIVDRHQWJpM3JQWnRhamZidjlybU5tdndXZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
