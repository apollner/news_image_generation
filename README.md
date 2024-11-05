# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 NFL Playoff Picture, Week 9: Surprising Cardinals Lead the NFC West**

You can read more about it [here](https://news.google.com/rss/articles/CBMikwFBVV95cUxNNDRVeFpRYUFuR0d5V3Y2SEI5dmNKLWFQeEo0Q05fNzM5b1FLX0wwYkNfNFBmc3ptS3NXLWIxUkU0Q1dwZjVnTFhYNzB1aFNGWXpFOXo3SkNWVTh6dzYweEN6dnQ1aC1aa0JDc1I0VWJQT3RLVWhNdWJMdW8xUEplaE9TWFJMOUJFM3JPLW1va2VjVkk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
