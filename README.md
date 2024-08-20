# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hamas claims Tel Aviv attack as Blinken promotes cease-fire in Israel**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZXlodnhoUWtZT2RkMkRpNG5WTWF0clNLUWoyaGx3N3NmU01KdndtR0w0TnE2UzZnT2RNd0FlMDJSSWhpbjFibkNIbEJTRWtpb2lBNVYtUGVraUF4ZGRJYUNSbU5sQVNYZkliaHVLR3R3ampXd2ZLaE9XY2g5NDNWcFBLOG5FWS1RdTBPMVhuQzZLZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
