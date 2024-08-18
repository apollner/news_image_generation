# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israeli strike kills at least 10 in southern Lebanon in one of the deadliest incidents since October 7**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxQd1pPTTJtMmIzRHR0UFlsRUZTamk4VG56aUJmeWFLem5uSnFfbXZQbGo1dHlFS0RySWJydVZNc0ZHaTI4cF9MLVEzMUhBc2VzZ280X0p3VDJMQkhCaENIWTJSMTRxMzdfY3lKWlVGWHM5R21BekFjY2hhN3JJUWxYLTVSUmg1Z3ZLeGJXOVVBS2F5SFFrcURBZ2d1TWVfUmhx0gGXAUFVX3lxTFBJTE1rcGRGQnhzaGlFM2NCMlBDRWt3bjEtRkNKRHdKQkpMLUVLemVmNENDOXl6SDJzVmZSS3dicDhOM01yTkI1R3Qyd2JPX2NUZDRhUXZuSkxNTWhYNVV1Q3dhb0FaWDg3c3VpSUhVVnFtVVgtLVAzdDRUbmxYeXNiWnhPUnJiYlRrU1Q2TzVNOXZvRzQ2UXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
