# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Judge pauses rule that would require Georgia counties to hand-count ballots**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxNX1hVdkFuNXZzcGdRZmFXYXk4bHlPUVBaU3RQTVhjM2pCaEt0OEpHSzg0RnpyMlY4TzR3U3lUQ3RZamNHeGRUOGZBUFlJR0NRTm1hMEM4QVVCMTVZNmo0Yjh6OHUtNUNycEI3ajk2YUpuM0E3T2lMZ0VxZWxZYjB1RkMxZ1A0OS1CMHI4cVZtZzFTakxT0gGLAUFVX3lxTE4xaTEwYU1LY0doQmZtVXhYZ0NGamowUEllXzRUMnBHcjZZSlRtcHJ0eW1wNHJXX1NQRkt2UzJKXzZMakx1MTY5RHFpMXFxMjdHQzdIZGhXbVhrUFNZSkRFLWRMbkJ6SmtfRnlpaldBWWJGVDYtSk5JTnI4QmJVRVdOUGxTNTJZVkhlMlk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
