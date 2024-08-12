# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Lively-Reynolds Box Office Domination: ‘Deadpool & Wolverine’ Stays No. 1 With $54M, ‘It Ends With Us’ Soars to Huge $50M**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxOWG5YSGp1bUF3VkgyM2lUUl81VHduWlY2aDlCWUg5V05yZEZ0VVEtSEN2R3V0U05nVkhNVjZNems1R3QzNzZqMG5abmQ0WWZTQUw1QktydzNUeHgwN292SFBYS2J2cDFtZTF0LXJiaEVfbk5ILXNKLW9jTy1raVBfeFlpbkVhMXY3Qll0WW9EMjFTTHpuWTJoTVZzNG9xcFZt0gGmAUFVX3lxTE56YktGcUg1Ry1yQjNSdzFTam9FNkFBUnpIYjlTU0ducGdheFIxMEdoaEFPMGNjcmR5aVp0OVNjNFU0MzkwN0YyTmVtSzJpa29keGU1cHEtTG9TUDRweThqbEt3VjBHSmNHSjZYMmwxcDNHZWlQQ2NGNm9mOXhLQTcwZFVXSnkyalR0T3JQV2x6V0tVQ3czWGN5elNYX2ZQRUJUMXZQdVE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
