# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Speaker Johnson: Shapiro was ‘overlooked’ for VP because of Jewish heritage**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxPMmxiWGNKX2dRamNuc2JKNnBReHVUZFJ4b09XMFo3dUh4QVlBcU9rWHNFU19UV1JRcTNGclZLMFl0Z2g2cTluWElJNENFNkRISHFQbHFpXzA1bkZiYmN1SExwdzAwM2hKLXFHaHBfVXdNZWlpMUM3U3BNQ2VpamNMQ3JidGozbVR2XzNVV1ZB0gGTAUFVX3lxTE9IUDFYcDhKTDQ1c2dBQ3U3akM2YjVMTkJ6dEQzbnpTcWc0MUUyaTFjd3k4a3ZHX0hQVmxrNjR6X2J0TFpxRktMVV9BZWI0RWZNYUk3SWJacEloNEpTX1FtdlRnSDlfdlN4Ry0yN1lFUlhMTUFyOGFoZHRvV0lVOHN0VGdoZXlRQjlPakh3b0RET0tuOA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
