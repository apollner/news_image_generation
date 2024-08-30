# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ex-politician found guilty of murder in Vegas reporter’s stabbing death sentenced to life in prison**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxQYW01MHRYRWlveHNLRmFIN2gtSDlXTTFyY1dYM1JMZ2NGQXVtSGtTN3YyN3BPZ3NQZ3NSRmtsUU9QSXFGU3htV2VWN0NETFVSYlE4ME10WUVzMkxMMkdoNnJOeEMwT0dZa0tXd2o5XzJUNU82Sk1zcUwzVE1vZlVXaHJKdDUxN3BJUWg3aWRrZ9IBhgFBVV95cUxNVUNhaUNIU3lwY0t0WXdwdFJWZEhjSDRLcl9vQ0tmT280cnJzMXFOVy1PYVU4RlJvZ3MtSW1pSVA3emdRcjJKeC0xdVcwTGNGdWxURXJPaVpZWUk4Vko2d3pmYnZCNk0wZnhScWZhZVhVX2dPeXBhNDdPLXNzN0dBLTRUdDMtdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
