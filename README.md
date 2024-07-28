# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Three members of Gospel Music Hall of Fame quartet The Nelons among 7 killed in Wyoming plane crash**

You can read more about it [here](https://news.google.com/rss/articles/CBMiXWh0dHBzOi8vYWJjbmV3cy5nby5jb20vVVMvd2lyZVN0b3J5L21lbWJlcnMtZ29zcGVsLW11c2ljLWhhbGwtZmFtZS1xdWFydGV0LW5lbG9ucy03LTExMjMyODEyN9IBYWh0dHBzOi8vYWJjbmV3cy5nby5jb20vYW1wL1VTL3dpcmVTdG9yeS9tZW1iZXJzLWdvc3BlbC1tdXNpYy1oYWxsLWZhbWUtcXVhcnRldC1uZWxvbnMtNy0xMTIzMjgxMjc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
