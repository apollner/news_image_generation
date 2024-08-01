# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Donald Trump falsely suggests Kamala Harris ‘happened to turn Black’**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxPTnk0dnN2cWhtWl8tQml3eWdRdS1IU3VNalVZXzF1aFpDelN5anFUZDFhYlQ4NXhrQ3g2RTZpMkVQWXZuQ0w2cWdWY0l4ekl2azRQdDh6QjlhLUlDSm5WaHEzZjBNV014YnpMRllQMEZDM1BsNDJZemV4ZVNPcGU3enVhMkduU0l5bENURkIxSF9yUdIBiAFBVV95cUxPWUc3blZzX3JTZkpwT1Fad3ZUa1Q5dmtIa1FONVo2Mkcyc196bmV1VTByN2xXSlF1a0hUTEdBeS0xekoteVc5aVZfcGcxNlJ1SEdsektoYUZkNXZvRndESzBjcC1jSXU3UDBaUkFiNGtwMEVhX0dQaUlEREpabmo5WVk0anotMTdS?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
