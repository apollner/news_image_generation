# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Former YouTube CEO and Silicon Valley trailblazer Susan Wojcicki has died at age 56**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxOeWw3TEpmdE9KUzBjanNwOEtEeVNCaUhPNG1GcTVtZS0ycDg0MExMX0tFVnRWcTBNNEdkX2s0azFGeVp6bmNIZDVBN3JSV0k0cTlfSHpsR3ByS2ozaTN0dGhqM3pvSU9KMHFFYlVVZkxRc1dqUC10aHdLREIybDl5TzhHbjlfdzA5d3NPTjVlejdFRmxZYUJsazhpdEhZVjhHU2hQTEZuRFFhSXJFMFo3R0pVOHhiM3NaM3JWVNIBwgFBVV95cUxPQzRhZ0pkdG95bWJyVnVGcC00OGM1WURENlN3cVJHS014SUFZRWdSN2RLeU1zeG9Tak9rNEZPQnFJUWlsQ2stMW52cU9ySFh2U2lQdWpCZHQzd1lyVFFGUk1FWm00a3VTM09BU25uSUZFN3YzaXMyOGdSVUt0azlEUWlUelNUZjF0Vmp0RlVWTWFKZ2NCNkZiMjRDU0xiWXRmRjVBS3kwU3dqMVFENzBid2t6WHB5S3JDWkU3S1E1ZE5SUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
