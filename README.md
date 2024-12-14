# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Oldest human DNA helps pinpoint when early humans interbred with Neanderthals**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxNR2N0WFdVcEFnQnNwWEozQmhtVmcwM0tlWVZ0MlR3eW5vQmFSVFVEMGs3UzBCWUFQTHNjUkFFcDd0UEU4ZWJiV1d4SGpKRVVNWlFpUXRxVDhYZWJqNjVhajkxQ08ydFcwdHFtQ0J3REFjXzZKZktpelluTGZ0T21MRV9rMU10eV9Cd09hQmpsSFfSAYcBQVVfeXFMT2FIQkxURmtBZFVyTFUzLW50bHozYTVFZVpadTFHMHVJZlV2dXFmNzhlS0RIeE1UUEtuYjFpTkM2dEdmS2FscWxTSURyOW56VVlhMmltNFB0anNGd0xMQnhhTkxUY3YwZHJvXzFBWW9JbVlSbW42Z1l3XzVoOXBPdlZ0bGFIalBF?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
