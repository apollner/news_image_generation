# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dricus Du Plessis Beat Israel Adesanya Physically and Mentally at UFC 305**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxOc2Rud1pGNmMtVVhMMUl0cHJfOWcwcVNpX0tjV0VkRGtvb1I1RTAzTzV1OXR1YXUzOXdhMGdkdUJ2ajdGWGRwZEVWMkdWYzlRNG9sVkRRR3VDdjdWUy13Y2tROUsxZE5ZRGtQZW54aGxFQW9LclZzLUdtTkdXT2lkRUg3c0I5cjVwaWZwb0JYUTFBNU9jaEcydXBQdzM1N0dSOTUxQUJ0WmFaVjlka1pTYnVhRkdHS1B1OEHSAc8BQVVfeXFMT3NYVW1OVFRNa2hXaTJlQVk4TGh4SV9UX1hVdnJ5aUZTRzBmclJKWms5SDBlbUxreHpHVHpIbThJN0U0ZEUtT21aSDdjTUFtNEMtZXJKaFNETTFKSkh3cUdrVWZRM1pLQ1dTVWpEblU3dDNpdDRaNjBlamhzTjR5MWY3aW5xc245SzBJUzFMX0xTa1NWUk05bXBIRjd3VGlXMlVzT3R1T3A5RGQzOGMySkR6cDc0Zkg0RHFiWGo1bWJJdURkTnU5RGswUlBmX1BJ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
