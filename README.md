# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stock futures are little changed after Dow closes at another record high: Live updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMid0FVX3lxTE1weTdWSnJpSHp3MEwtTGQxM2hDS29LVEZtT0k0LTJZQXlFVmlLVU5MaHJCcEJQMXNwT25POUU2UHFsTml4eEszZEs1NGRNWFhTMHh3dk54ek0wam94VTI5U01haU9wWnE2Wmd5dE5MLURfbXJGdldF0gF8QVVfeXFMTWtwZDdjdl9QQzdsaU00SjNnOG1nWk8ybHRRNlVOWGI5QWloQk15TmdVZTJtbEZ4RWpPTVNDczNGSHU3aHdNaE1IdEo2RWxMMmdIcEtHeUFybUR6OXUyN2g1RjJkamFtd01CN0pLOS1pYkhjck1MbHVyZktKdg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
