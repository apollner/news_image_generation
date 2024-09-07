# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Decision on Trump sentencing date in "hush money" case coming Friday, prosecutors say**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQaHplU0VWUUUzMjAyTWMzTVBQblRKYk9QbHhtSHRITUFqNzhlUVdHNC1PbXJnRmkxV0puNFM4RERXbXVWeGNNTXVLVW9ObjVqdFIyVEgyQnpScjZYaVJfd2FrVTlUSXFwbldXWnZVV2t5SUtrUmVTeFU5bHFLMzhZamEyUXYtRDd3RS1UV3RNRl9IWTJBR21EOHEyTnd0ZFVTb3FZMGhYOW9XUdIBrwFBVV95cUxNdE9pSDVrLVF1UjhsVUd6YUtvWVJ1UjlRZTZiNnR6QU0yT1kxbVRyb3pmYVZjcS1TcVdObUh5YUc3aGJpUjlrMVBRTHRuR25DczJqTnNYb1gyOF9hb1hwQ3ZoZUt4eWNUcjVpbHAyYXgteU11MkhCUFJ4d3hIX2xJQ3VqXzQtaXU5bU5WVFZTT2tMSGNyWGdWUWNqMW93ZGFKY0U4aTlrdm96Nl9feFBz?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
