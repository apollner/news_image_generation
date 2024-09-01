# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Carson Beck, No. 1 Georgia manhandle No. 14 Clemson**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOd2EtYTNkS3pNOE9uN1RwN2pTSGdiaHItcVZ4ajVqcXNsOEhWdDJxV0RsX1Z0UTRSV2JaRldKZGpmbWtXUEJBZ2N5cVlLUjVsR3dCd082Zld1cHVmdGptV1Y2TXozMllMQWlXeUVVNkRxU1hFbjZOaTN4ME9QX2M4RzZhUFpQMXFVdXY4em9ZUmExZEFidTNaN0l1NmdMSDN2b1dUSWt0b05IQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
