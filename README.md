# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ann Coulter Deletes Post Mocking Gus Walz After Backlash From Rosie O’Donnell & Ana Navarro**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxOcVZkZ3Y1YmR1U0dfeHNlanViWGd1Zk5sYU9IZ08tWUZnRzFJOXp2WHh1VmJQcF9Ca2xYckU5ZkZMMDJrT3FGalhQRkgtYUR5eVZYelh3UzU2aFRaSU9MdFNiQ3B2Rl9UT0tYU2FycUlBRThhX0FkTTdTNVFFNEoybHhRTzBDSFBNVDJ4Uk9KaWIxQ3lESGVoSlg3ZTA3bllTelNYX1ItQ2VGSWZ3eGlKZktPcE85VWlPVHc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
