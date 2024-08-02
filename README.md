# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ballerina Farm TikToker Defends Marriage, Farm Life After Article Thrust ‘Trad Wife’ Influencer Into Turmoil**

You can read more about it [here](https://news.google.com/rss/articles/CBMi_gFBVV95cUxNTmYwVFFpSG5DTzQyQXZRVHpxN0N6Y1lfbWVtVjFnU1FmbkcwVnRzYnVaeDVlMXdRM3BsWW54NEI3WjZRQmZNTFE3SlJmZ1h3SGdDYzVTaGprSy1uTVVjQ1Fkb2NsUTYzTGxRVV83c3FQRmZ1dG5DTl8zRENoWXFvTml3d3hOVUhUbnJHa2FDRVk4WEd3a3FiaDNtVkF6UmJvOGFXRFhWTkJ6MU9laGJGTjVDRF85Ul9DSlZuMWZRaVVCYXBFLWZTOHVmaHdjMm9TQUJTdk1YTHRzMHloOWdMTFZfUVFyNks3V0R4VHRMNFJWOXdVSW1jWHU1aFNIUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
