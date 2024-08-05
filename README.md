# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Box Office: ‘Deadpool & Wolverine’ Scores $97 Million in Massive Second Weekend**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxPbjI5c2puV1hBZC1HRGt6QmhuTllXVkFJdl94Q0JOMHVoei1qa0NDTnZtdGF2M1lBYm80eGhaLUVPN3VTd251R1h0S0l5NEJDRm43WHRVOHN2d0NHUG1XYWY1V1ItcEFYSjZLQUJuRi1zSlhrZWlmNlgxZVZ2YkUzM0Y1NWJ0d2hQclJLQ09kYWxRc2NqSkZmSzhwdjdFd9IBowFBVV95cUxQSVhSZ3pQWVZIU2h1UC16cTZKb2NIaUtVU0E2cTNudkZKUmxBeWNVQW1kdVV3TGE2aUxMR0U3T0VUazJmVE1qeGU4bkpxUFVnNlFrbzdkaU4tREFvMFpnSHNXelhtQUVoRkx3eWRPTGpSUzY3bmk2bnhxdkF3NTE1cEM0RWVuN1R4T2xuZFlLbUFncjdZUmdKZXFQSlBMeThMWU1v?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
