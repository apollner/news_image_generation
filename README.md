# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**British safety adviser for Reuters killed in Russian strike on Ukraine hotel**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxNZjdTZko4bkt2aGpaWXB5QWpSbHlydE9FUXhTd0xOQjlkVHdUeTV6OW1zb2FYNHB1VDZvVTgzTVZGZktOX3ROQXB1eGRHMnQ1WThnSGk3Q1p1Z3RhZWhYNmExWXQxQWVIUmU5empiaUhKLTREc2Fjc1B5aWVSdDUzRV9zOEhuSjlzbDQyWDdnb0p6ZUc2SE00ZWlKSDRURTjSAZYBQVVfeXFMTkNBZEM4Umx1VlBvVDhaOEUzQnlFMFlWa1lGQTBTQl8tTjZTUC1XNVlDWEJjdFBncUZuTlEzSkR0RnkzMXNRQXQyRS15eFRfT2FQMGJJYkswOWxNU2I1ckZMMlZfU21leUluMGxDYnR1OGpMMlRESzRzWHlyQzZtdzdLM2NhMFM4U1IwR1lDWkV2NlhxX213?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
