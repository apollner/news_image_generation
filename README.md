# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Philadelphia Eagles work to remove bogus political ads purporting to endorse Kamala Harris**

You can read more about it [here](https://news.google.com/rss/articles/CBMitgFBVV95cUxQbUl5MDZhaXR2Mm1vbGE1TlpfMFBvX0JTb0EyX2MtVDUxMGtDc1FjYWVid3BudHh3cndVT2Fzd2x3MlV5QjVzZ29MdEVORjFfNXZUV1dVY0w4YTl5VkNKT1JTRm9OTExLYXRnd3dnRGxmWFZXR0pYSVRQeXBrNTVxT0t3Z2RfV0VXeGZwZlM0dWcwdHlaM0hkd2RrNXlRRy1Rem1wRzAxdURDajN2WUw1MVc5MFUyZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
