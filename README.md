# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stocks close higher Friday as market comeback lifts S&P 500 to best week of 2024: Live updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxNV3Vnc2MtVmFUanNRNVdTUmluamdFSDRSQWlILUJXMTA5U0xKMm8xN25GM2xhdDgwaS1PV2JuMExTODZaLVV0elVab1FYWXNESlNqdEpZSEdDdUsxM1VLbjdtQkxpdWw4Si1TemI1MTN2YXc0c3pOdFEwM2NWc2FuSzUtNXZJS1kzS0owQkw3VkJNdEZTY2VfNnVaZlVfVF96UmU4TTVIV1JmMm5oZHfSAbMBQVVfeXFMTzdvUWU0aFlmemp2SG1xZ21qX3I1a1NONlBRQkhtVzNYU0pjVVdITkpIeGtrQVNJdmw0RU9rT09WTFZ0anpTbUhaVUtTM3VMOW9EQ3ZycUg2a1ROZ0pRVHRRZWk4WlB4cXgtN3A5NTY5LXNGbHVqT3NMd3FZcFpCSy1hWkZGYVpFdWhiVk9iT0FOdWxQOWZvU1pRQTF6emNlR2I0RThFRVR6eVo1YjEyekVockU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
