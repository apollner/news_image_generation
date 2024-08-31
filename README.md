# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**North Carolina hiker's death is believed to be 6th in a month at Grand Canyon National Park**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxOZFNlVVdaMDROZWtOUGFVWnItNER3Y25tSzVlUDBXcGM3UDgyLXJ2SF94SWpHcTdTQWc0S1pqbGxpWFVWclIxNmU5TWI5dEI4N0dSdUUzRWVJcXB2MEVfb0QzMWVwQ2M0UjNxY2J1MFl3U0l2M2JuVVU0MGZOUWlPc0R2NVlOZFA4WXZEZXVKc3VWNlR2c0dPbERwZDhXcHBUc0JoUHdwZDNKS0hEN0szUTVMUWRkLUVsaEHSAVZBVV95cUxPS3hKdGwzWWFtRnF1SlhRR2lkblFoUW9CVF9HeHBuMHg0NXhidTg0WFR5eHpPRjlObUs3X2lxRXBZMlNJOHhXb3VNNXN6SzloSTZMMUMxQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
