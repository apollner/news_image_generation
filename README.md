# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Blinken heads to Israel for 9th time since Oct. 7, hoping to close hostage-truce deal**

You can read more about it [here](https://news.google.com/rss/articles/CBMitAFBVV95cUxNRnNPMTEzR3lwbjRwQVdxNnhSaUkzS2luaEZKcnNhUnlBbDBoVmREc1BycjBIdUNwNTk1Nksxb1MyMzJmVnR3TW14YTE4MVlVM28wc090UVY3Y1MxM3A2YkN3T3BzdGpjWHRnVFpMZWpzTzRvT3NWU3hxV2poeVo2RHNmbDc0SkNQbE1uSnFhUkhkV2RJYmlqcVcyRGxoM09sQUxTMnZxbldxSlQwbjNWeWp0M03SAboBQVVfeXFMTXAxeVJVOUUydzIyQXFmT0xMUG5mamJWeHRWY2lUSk1iQ01hNmR0ZUM2anJUMGJ0ZnVsQXh3OUpjTkt3NndMR3ppODQ4LXJZcjVPdE5BeEp1NG5xRHIyVDJWSVd2c1JVVmpwbVplRFR6STVXUjAtY3lQNVJsa0ZUbDBoWHRSV1FOQkdYM09CU3BZa2o5aVhFR2RJZWpCTjZmMHYzZGhDNnRaeVI5ckswWkhZYWJkc1dGekdB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
