# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'Deadpool And Wolverine' projected to have $360 Million opening; Ryan Reynolds and Hugh Jackman to set ne**

You can read more about it [here](https://news.google.com/rss/articles/CBMi8wFodHRwczovL3RpbWVzb2ZpbmRpYS5pbmRpYXRpbWVzLmNvbS9lbnRlcnRhaW5tZW50L2VuZ2xpc2gvaG9sbHl3b29kL2JveC1vZmZpY2UvZGVhZHBvb2wtYW5kLXdvbHZlcmluZS1wcm9qZWN0ZWQtdG8taGF2ZS0zNjAtbWlsbGlvbi1ib3gtb2ZmaWNlLW9wZW5pbmctcnlhbi1yZXlub2xkcy1hbmQtaHVnaC1qYWNrbWFuLXRvLXNldC1uZXctcmVjb3JkLWZvci1yLXJhdGVkLW1vdmllL2FydGljbGVzaG93LzExMTk3MzI2MS5jbXPSAfcBaHR0cHM6Ly90aW1lc29maW5kaWEuaW5kaWF0aW1lcy5jb20vZW50ZXJ0YWlubWVudC9lbmdsaXNoL2hvbGx5d29vZC9ib3gtb2ZmaWNlL2RlYWRwb29sLWFuZC13b2x2ZXJpbmUtcHJvamVjdGVkLXRvLWhhdmUtMzYwLW1pbGxpb24tYm94LW9mZmljZS1vcGVuaW5nLXJ5YW4tcmV5bm9sZHMtYW5kLWh1Z2gtamFja21hbi10by1zZXQtbmV3LXJlY29yZC1mb3Itci1yYXRlZC1tb3ZpZS9hbXBfYXJ0aWNsZXNob3cvMTExOTczMjYxLmNtcw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
