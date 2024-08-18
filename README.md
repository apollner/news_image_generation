# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Kamala Harris proposes ban on ‘price gouging’ on groceries in economic plan: Live**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxNRXFNTGMyQU1iTi1qN2wwcm9lVWQtcVl5RVRjUUp3WEZoZUVaM3RmYU41RUlYMDlsTVQzTnVtSmVFQUJBUU10N2NGbFpvWC1DT2VLZ1B4ZktVMk9mUUdoZ0FFYWtnam9lUzF1R01EQndlczlobjF1Ry1vcC1tZW9sa3diUlMzZEFfMTc2NjVHb3phVlNJY3U4VnhoOXJvT1gyNmYzNk5mWTBJUnB6QlZCSTZkSzRSYmFMQnJZcg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
