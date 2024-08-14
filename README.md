# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Greece fires: Fresh evacuation alert in place as threat continues**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9uMDdEZUFvb3R5VnBxQ0hySm94RlhUc1E5dG54SGV6U0dfQlAtdGU5dmtWUUdiY3R2MlhrZ2VUR0V2ZExBakpuZGJjRnByZUFBWUZtTDBlZnZuQdIBX0FVX3lxTE53QjF1VzBMRDZETGo2YThmM3VkRFJYR3RIM2ZxQkFxWXhyblAtR0tXNTVBa0dRNVVqNnY1X1M0dExqNUVYaWgxeVZxLUJ3Tm9PMy01Z2JzSUJxVGJZQjZj?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
