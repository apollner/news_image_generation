# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ukraine drones set oil depot ablaze in Russia's Rostov, governor says By Reuters**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2AFBVV95cUxOSGt5MHliZkd2YzlVWHdubFRsVktGSU9oVGVEV1Y3X25CLUxMdEZ5bHFwbThxdkRDRFNPYUM4TnZZNk0tc0dGUHFPSm8xSi0tZkJFTVNqWTF3RGFydDYwbDJhSnlsY01PTURidnRMSVJtTElsOVFNSzZWUWNNMzdfcU1xZnBtYmx1SWF1blJ3Q2dkNi1oRFd0Qkw3NGtvdF82ZmNqTTF4X0poNWZ2aTlTOWlQOGNteWh0dHRYS3V5Z0dZYjhxZ2xKQ1lsOWVsZDV0NVBrZDdjS2U?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
