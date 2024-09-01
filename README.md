# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NASA plans to send 2 astronauts instead of 4 to ISS so pair stranded by troubled Boeing Starliner can return**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPY091QXFwaEhPM3dhSGJHcnc4Y1JhRzJKZVZGb184WEtpSjUwckNMbGp5Ym5BLU5ZZDRpYkl0RllqX0ZvcWNfUG1ZSkw1WnJpR3g1bDU3cHRBdEFtMjVROEU2N1FoYmxGM2gxZFgtLWdQZkFKYkpxNC1RajlWaGNKa0x5QXM4Rk9reWVKMlotZFdoUlBzVlUzYVZNLVM0bjhuSE1aZGNNUWFkUdIBrwFBVV95cUxOWVd5Xy02eDZCTG5jc2JBaHdUdW1FTXRCRGVBdlc4Q2NDRUZUUU5NNFZONEFFS0hwWm5HN3NsYUM3NUpydGU0N19idzB5TndIcjJGb3NNMVQ1d0xvbjR5bHdHcHZrN1JGYjF6TXZQREQ0XzR2am1uVEhTX2phdTF5NTBkelczZjNGU0ZTRFhrVkxST2t2R2lQVE4yc0tEY3lYSFp1cmdwSG5BUzVaWk1Z?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
