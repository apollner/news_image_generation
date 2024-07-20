# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump shooter signed up online to attend rally a week before shooting: Source**

You can read more about it [here](https://news.google.com/rss/articles/CBMiY2h0dHBzOi8vYWJjbmV3cy5nby5jb20vVVMvdHJ1bXAtc2hvb3Rlci1zaWduZWQtb25saW5lLWF0dGVuZC1yYWxseS13ZWVrLXNob290aW5nL3N0b3J5P2lkPTExMjAxMjMwMdIBZ2h0dHBzOi8vYWJjbmV3cy5nby5jb20vYW1wL1VTL3RydW1wLXNob290ZXItc2lnbmVkLW9ubGluZS1hdHRlbmQtcmFsbHktd2Vlay1zaG9vdGluZy9zdG9yeT9pZD0xMTIwMTIzMDE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
