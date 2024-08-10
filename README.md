# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Japan PM Fumio Kishida cancels trip as scientists urge preparations for possible "megaquake"**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxQYTVZR1FQaS1uU2docE0zN1hqdDNwSFk0SXAwbUNIYmhMT0JmdHhKQ1l2S1B6aTZfeUlUTmhLclhJR0RJbkdkWWp0MHRZUW5DbUFWWDkzVWhfUUxkV1pXM3VBZU9FS0RhV3RFaEFhbk95dnBOTWxrQjJpSU56dS1yQ1NFT0w0TjRSZHhUemVfUC02UdIBlwFBVV95cUxOYjdfVkc5M3doSUpfZjdybXY2aDQxM2JJeGN2azFlbU1rcUU0NVhzb2IxdWp0TzB0VXpfOU1VcU50ZHhOOW13Ujd5WHN6Qlh6NG1KT3hKbUxtNkREcklWdUtlbERqbVhOOGtsSjJYemwwNnVLX2Y4b0s4cTBCbGttY1BiVWlVdkNYekNjR25iMFlxMHZEN3Rj?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
