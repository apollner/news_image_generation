# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump doubles down on ‘enemy from within’ comments at Fox town hall**

You can read more about it [here](https://news.google.com/rss/articles/CBMifEFVX3lxTE9tVGl1RkFDbG9aNGpoLUk5NnUyaURlTG5sMFlSaGpvLW5XMng1c0NJMUp0LTlDcjA2Y2tUZnBodGZMZ2ZEMDhuZDhveTBUcjY4R1lfZ0ItX3ltWHVacWlhQ2JfNE14UV9pam1FY1ZLUEM2Wjd5OTFPSFpUTjbSAXxBVV95cUxNREczS2dKd19qbUxTLVJHcUhRRW1BdFFBMDRUYllKR21TY215MEt6MndNS28tcjVZZE5SY2I5ZkpsTVh1TzZyOEFjc0E0QnVyMk1CRFhLeUt6R1I1Q2huaVJSR3RlaHQyQ3JkVGhDYmpkemRkRzJEa1c5VDdL?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
