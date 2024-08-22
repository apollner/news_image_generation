# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Richard Simmons' brother says fitness icon died from 'recent falls, heart disease'**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxNTE9tbUFoTXNfVzV1ZmJ2dk9KVFJFaUtVVVVSYzRjdU1weTZlTnJ5YVh4S29fa1BDbjBKR1VrdmMzbUJTRENvd3dnYWRCRTJ6QndEVGVDekVaa2Z3NlhKaGlGeDVLaU5kb1czazlBZWY0WUxpYmNqVF9mOXBUX0JFTVNHYy1say1OUEtKSkJNZ1RpUmZ4c0cyM1Z5MjhpVGlmNkNRRVVRQ19QZzFTdG90c1BXY1ZNY3fSAbwBQVVfeXFMTXB3WUlqS19CaDFhaC10MkFyMHNjR3B6amhiMWpUMVRuWkVFeVFNUXNVTFRPbzdqUGgtYy0ySFk5X19wOUI1Yy1ERzFVbDBrRTRmM0lIUG1Zb1hCVG5PamlGMXItVzd2b1A4em83eTNnbVZSRkZGR3AyTWN4T0ZFRTRTR193cFFNWERhcFN6U0V5b09sTnZEejJDZmZuekJGRDhTM0VVRWNkcmppUWVIUnlSWjgtTzlYWS1IU2o?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
