# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hamas names Oct 7 mastermind Sinwar as leader after Haniyeh assassination**

You can read more about it [here](https://news.google.com/rss/articles/CBMizAFBVV95cUxOcVJXMm56ZnNlcWpCV2xyVzBXc01nS19XM1J3SW5xTHhGRTVtUGZhMTAwV21iemN0c1pMTlRjZkh5OV92dEpnaHpWUEhuZVdxMWsxZ2NDejBSX3ZET0IxZUh0bGJjZkhMVVBMOUdaRU9UVmVxb1hVT1AtSTlKdkJ6d0hNTllVX2tpeURPOXEtbmJjMkljWXVtSi1SbS11d0t3WnhMODd4a21lTGZVYkpwS0FETlVvc1R4Y2VyOWZKb2RaaURMRmlyZjd6SjA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
