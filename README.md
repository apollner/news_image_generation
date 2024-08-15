# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Judge rules with Jewish students, says UCLA can't allow them to be barred from accessing campus after protests**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxPMGVuWHlBbUxWMUs4ZjRWUGdhT1hhWDRMbXozVVNUMjM0YmFGSkdlUllVbHM5cnY3VnNyWGQwSDNHWWJRYnZZT2VkbkhsTGF3V0hjSVVQVUNJVTZLYWJRSFhKUUVlOEd0TnB1LXVOcXpTejRwaUtIamVaQ2xBY29tZmFBRTlVeXV3eFhvRGdVSHlhb0dCTnl6TmgwMWo0NERWNHFldFdEX3RncEFhb0g0R2E2YmV4SlNDTlHSAVZBVV95cUxNaGJLQnRuS2VyR1BUSFhOSG03cS0wSlNJRUhBS2hEVFdvR0xwRUxEaEltWHotLUZBUVRJSUtjY1JlajZEdTRGYy11SjI4WDVQQlJyOWVGQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
