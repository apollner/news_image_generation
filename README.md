# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Top US general says risk of broader war ‘somewhat’ abated after Israel-Hezbollah clash**

You can read more about it [here](https://news.google.com/rss/articles/CBMitgFBVV95cUxPNEtidXhXTmtlaVZmMkJBMi11ZmZPbUZhaG1SeFhLQnkxOGJBRE5TZHYzS0JnOVJ3WTRJVlB6aTFTVFMySFNIZmRnVF9MaGs5ZXVfaHVuWHJxaGY2bHFlN2hOU0VSclRkMXVnOEVIcWFyWHNoTGpXWE9sOHJ6d3Z1XzhUMDJZeWVVTi1vRVB2Z1FQbkFJWWN4RGJqU0xLcjlFWjdKM0lCWUFyVjdyaDktckFzdWJDZ9IBuwFBVV95cUxORU5nLTFPb2o3WlBMUF9YRDZKTi0tYzBRM09rcVZ0TTBhWXgwaHc0RF9HS0pici1RUGF6bmxzUDVfWmVhTjZ0MnkyVEtlYWNORnFaN19qNEFYeGM2aVprbVVYQVNyMW9fckwyUHZkdmFOU0VWT29Bd0ZxZFM5OUh2VFRRVTJRWFAtUlNnMEZ5RW0tcURvQkxjeXo5M3VWMktGZTItbE9BRS02NkUxTXpSaVFESFZ2bnJoc0Nr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
