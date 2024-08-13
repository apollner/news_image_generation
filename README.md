# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hulk Hogan's Ex-Friend Is Willing to Work With Ben Affleck, Matt Damon on Gawker Film**

You can read more about it [here](https://news.google.com/rss/articles/CBMieEFVX3lxTFBkdk9fcDhGdjgzM1hIekY4c2JWOGNDT09yam9Xck1MZ1ZkTFh2OFFVbmJMYzkzZVBKdVhFNHl0eVNoV3RkN3J0d0t0MFc2alV2MW1OaGxhaUU5aHhaWUVlZzJpZHhCNzFQSHRvT0MwUjdVOHFKalB2bNIBeEFVX3lxTE91MjhTTERsYmFpUmpkTUlLMGNxX0NMSHlEYTN1RkdYYUY1TmZMRHU3YW1TMGN6UEh2TmxnVEpucW13ZW5SWGVYeXdNSDI1d01fWHVpamdvcU1DYTI1TWtyNXVoWWhmLU5za1RnU3U4LVFRYmg1a3pDXw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
