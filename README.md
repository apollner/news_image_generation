# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fed Meeting Today: Investors Await FOMC Interest-Rate Decision, Powell Speech -- Live Updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxQQ1JlSlZtM0o0Z2JoRGZqdUtyZzRhYW4xbjlkN0tudFp5SGRvTFBZSGNmMDdHVm5wTFdUYUNxbDdYWXh3SWVmRjdYck4tN0NzT0NOdDFlZ0lwRTNCYUF2WElXelpBa2E4Ym55NFV6bEVQLVdmbTdYc1VSNVA1TnRMYl9VU2I0LTFSNkU0MUladGdRdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
