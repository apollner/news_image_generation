# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Namibia plans to kill more than 700 animals including elephants and hippos — and distribute the meat**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxObmVsdkV4MWNHbUlWb0JCTWpqbjNReDhaTmVFZ0RhMGpfMm5jdzB2c0dGRlBISFhjOXl6cWhFdVdZU2tvaDZwNVprUk1EandfNzI4LWw5T05RSUNlcWFFc1NURVkzWlhrZ2ZhenJCdzV3eWJqVG54cnVtUlRqSlpaV0FPSFpDb1ZSbTN5TGFB0gGEAUFVX3lxTE1IcWJ2Y1VRLVk5THNXUmlyc3pmN2JIa0p1Y2hHMFBWTmpEOFNnVVVTQllMZlhnUFBvd0ZVbmc3MTdlQVItQ1gzZFN6VVdPcmVrQVo3azR2NDc5MnVxbFg2bW9mSEhNRm9GUFZabGtGMzNHZHVrZ2JlLUcwbGs2d0N3TnA3VQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
