# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Woman nearly bitten by tiger after climbing over fence at New Jersey zoo**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxPN1RPUWNtZkFyZWVxdllfUVdic0tkbDE5WnBmNFBqRmlPTkE2c29fREM3M3praXkxemQtYlpLZFk0WlR6NnkwLXVzcG9iVnA1T3YwNTBIOGJUUDJTNW9iS0IyWDlWWDFzM2hUeDFVZGdjYlVxWFotanJ0aWNHQ1VCMzhEM01TMV93QXdFN3B4MHNPU25TZEM1bzRfV2hXUFJXd2ptTl9R0gFWQVVfeXFMTXhoUVB1RGhrbWFyZVJwNDE1ZElDVjllQjRObFdVXzFGTnJlN3U5SF9mcXhEUGdWRjg0SXI2QjFTNXg2OV9ST3hIVF9mTXgwaDNIeXJyQVE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
