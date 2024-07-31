# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Russell Wilson finally gets some training-camp work with Steelers**

You can read more about it [here](https://news.google.com/rss/articles/CBMixgFBVV95cUxNTjAwbXpsOTQ4MzdubFZ6T1pQaXdhamhKTmNGWDU3MkVPWU5zMDFyWGFTczJDWWp6emZrRHN2aUZkaGlpOVk1R3RSQkRFRlFwcHI5bHA0ZV9BajdTNGVSZ0hVRXZNWm9kNDlSYkV6Yk41UVJIYWlEZkZVNnA1WlMzTW54OXRfUkJkY0ZfMjBrY1FuQmJtcGFkWjVhdXE2czJJN2RfM3gxeDg0LW9KV3g5MFNFbTV5bUR6bnFScVU1V0dJa2NSdXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
