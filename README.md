# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Angry Steelers fans blast Russell Wilson for dismal preseason performance against the Bills: 'Starting to thin**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxPRHlnQ0R6a2QxOWZCdENKcUF3SW94M2R6THBfNmJVVEZjc3FKMUpSRERVaW1GZHgzNWZTRVNIMFBFM2w5RHpwX21lSDIwa1hBN1BScnpqQkxjOXJsajBad2l3dVRqNEJ5U3pqNkttdGFGMU9Md3NaUHhLTmpmbXJ2NHRReTVKUnBFcm5WUm1aMGRrVm0xcnlJRkYteDVEX2g1ZWU3NE0ybmp0dzRBVTJPcU5YTVU3M3PSAbwBQVVfeXFMT0ltVktYMkk3UlM4dnItN2RCQkZkV0Y4UDcxWmFsaHltLUttTWFGenduSndzNXVISmQ4U2UybHBiZ2NfUGRPTFJOaFc5ZXpBYzFpVEE2NHRGVFVqd2JxS3ljMFU3cFRWUXFzc0t0SFV3SHNRc3Mzbl9iWERuRHFEV0RUY3JOVkZxOEQ4d25QR20yM1NnazJ0eGxIaWNCR1ltSGczc1otX0xIUnROaHJ1akwtLTRCOFpCTVNUelM?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
