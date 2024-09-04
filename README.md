# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 college football rankings: Georgia, Ohio State on top; Nebraska cracks top 25**

You can read more about it [here](https://news.google.com/rss/articles/CBMixgFBVV95cUxOWjFiTWpqa1ZaazdtbHpzdm5ZQ2R6djRKblRZQWhkMVNBcFRva2FuaUVmQW83eXpjbm1SS1JOdXNxdkV2MG84U29RWGtQNE00c044WE9KS1BNOXFMZWFvamoydE82NVhVd0dIVmZnQTBIdjlheF9oN0lSOVJld1lQQ2xoNllEMDkxdVVGemJFdXI2eEJZM0l0QkJUTG00dEh1TnVodFpBTk1tSURSeVQ0V1EzSGRCQWNvN0dkZVByck54Z0kxeEHSAcYBQVVfeXFMTnVrNTIxN3lCSU5KTWt4MzhDcGxYemJYeEozSHAzRFJkVFdLdlkzcXlmVmZyZnZkTVhXcEJZZU5LUHNBZXlDT2ZxOUZVTGh3ODlwbTJKWTlEa0t5VEZjaFptYXp5ME4zU3hUYmlqcS1YYVF1UkRKcXpVeHFlV2V5YXplLTlQNURpLTNpRS1KZDQyNld6bGQ2cE9vUFY5cmZmUHkyODE5Ny0yY1VHajZiWUZWSllDMHg4VG9SZEU1N2hYNjRrajVB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
