# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dow jumps 300 points as first of two major inflation reports this week comes in light: Live updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMid0FVX3lxTE8zempVQmRYYkN2TjQ2dHkzMGdhcFJScnZObk41OFp1S2loSUZCUThWRVhoT3gzUHBmOERHWkJLV0hxcXVLMVBNMXltRF9xYmVaV3NYUld3dC13ajBrVlN6LURvUHJKSnZHdlljVkkwNVFnUzl0VFNV0gF8QVVfeXFMTk1zX09BdjIxbFF4cTd6a3Yyd0pvekVSbFlvbWppcXEwMkdIazlFTWdTOXJJdUpTQ2hNXzVsaWFOYlNpcGhiRXVSYjFpd1NMNHM1cXNLeXloWXNTY2JBMkg2ZHBrZnhXOWNkR3FUQlFkWTRfdHJ0Ql9OV3NObQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
