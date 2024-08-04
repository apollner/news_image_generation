# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Vadim Krasikov: Vladimir Putin's trump card in prisoner swap**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxNUS1VY3VreUN6TkFjdllwNWotMGw0MmF2WnJCaERINjQ1OHdXbHNUQ3hDak1qMnB1RVJWZFV2YWpaS3V2X2Vtckw1VGVCaHh5TWdjSWNoTGhZa1M1TGVFM0NNcFVUN2R6UjNFYUxDeDVBYkJHR3JtSFBERG1jYzc5OVNtdE1uQmZ3bTk2WHZEUjdPT1BJbkHSAZYBQVVfeXFMT1FuX1B2M1M5WWVfNXpObXktd2NRXzFzR1hXRTZJRVhqT2dDZkZFMmJfLTVDb3BRUDNIZi1sMnJaS1FuV2RWbWhWY1pFTjlVRWV6c21ncFR2UlJpS09Qd0czNmlSX3lxelBua1FVcHhvZzRyQVZRdG9BLUpoeHdNSFREMmNHRTBTczhFU216VWxaODBxbGRn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
