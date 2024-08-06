# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hostage talks on hold until after Iran response, replacement of Haniyeh — officials**

You can read more about it [here](https://news.google.com/rss/articles/CBMisAFBVV95cUxPcE9HWTJXNUkybnpGWW5vYmF4X1h5azBNa2VEWFVzOG56UnRyRkpVX3ZqU0dLT0ZyYXYxcjVrTF9qVEwxdEljSkdMdXhZZlBCM1dnU1BOaFN2YTZLc0VfRF80YnR1bGNtSTBqWENpSUhzMTNfVFhTQ1VnbWFfRmczalFOOFNyVmtWX3ZMMUg3LXFPRGIxX04xNUs5WVZzVS1JdmttdXo2eDVMaThJeFc4QtIBtgFBVV95cUxPYnN1UXMxWnZ5T0xKeGVsY1l4WnNJM2I5VlhqQUdiblRackVYSnFjS0s0RWlMekJsZ3JhSzZYT1pfY3gxREZzWU1UbnBxVEQ0Rk45ZGVqSDk4UXZTaWRGZjJJeDg0b19BMlhrMmxfV2kyeFVlQm9mN1k2Wm1DQXBKUU1GS0NobTRMWXRnT2VUUFpQZkk0czBlMUhZZ3R6ZTBuTFRmczNZeHpoSmQ1QTFMQ2VZLWRrdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
