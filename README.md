# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel-Gaza ceasefire progress is an illusion, says Hamas**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE8wVGkwTC1QZ0MyRm5IQ3YwWGNRdmdxTmxKcUFFN0lyTlpMQUJqRFZwR01yYXVZWjZhNlQ1Zm1BU3R6UGhUQmloYXRha3BvWXo4UE8ydmd3ZjVDZ9IBX0FVX3lxTE9jZVFOX3hNaldPSk9mcHRjMGwwTDI4bTM5blhxRHRlNk85ZkhudlV1Tk1EN3NaM3NlR0wzQmpXMFdzV1JLRkZ0SFJraFB0U3NzR1BGZlZWLW5pdU9FS3Jj?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
