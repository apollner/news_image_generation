# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Statement from President Joe Biden on the District Court’s Order on the Biden-Harris Administration’s Action to Keep Families Together**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgJBVV95cUxQYjgyTWlYX0d5emV4Snlnai05VkNVd1A5MFgwQmY0eFBiRzI5Q1dfV0h5RUZJTU5BcDRtVnhUUzZTVUJ5a3ZfYWo5SU8zcDh1cWdkU05kV2RVYkJZcjVjTThnSDVuUDdIVXNpUFBkUDgtYUMtS2NUcENjRDJDQXVqRGhhNy1mR3JRU3YtS2lidHFxX2JCM2U5ZjFpNVhnWm9nWE01ZVJlZDhpc2tobW9faVBUQ1hLV2xkNnlfM3NHLVhwejhMMGVnNFZwOXdPWm91SVlYQ2xMX1lqc0hPUnc5VHVIQzBTZUpkSXprazFBSEJBaElqd3FaNjBjVmRQbm5IQWlrdjd3YTFWaUdXNXN0WHY2c3hmaFFjbTZkcmxReWxqZ292LUcydGpneDlidw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
