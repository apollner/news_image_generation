# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Martian subsurface harbours oceans of life-giving liquid water**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxQZ1RUZWNyRXBqVE4yNk1BNVJ5WEJDZGdicXU3TmFpcTUtdWItemtLV2lOM01wa21MMHV3Y1ozLVJPMzhpdXNTNk1OM0xVcGtKOVRRUkN4WUd4WUpuSi03Z1lZTy13NFBBNmM2aV9yQ3UtUURfTHhoYXJDd0VpT0VET3BIVm9QNHlWaEhvRzd1UGpwakVxVkpUaWhMS2JUNkN0TW1oZmZn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
