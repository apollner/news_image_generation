# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Colin Farrell ‘burst into tears’ when son James took first steps at age 3 after Angelman syndrome diagnosis**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxOZTVHSFZDbWhZZ1NLUW1sRFBEWEp5TnlrS09BdkNuQW9BbWduMDcyaGRfS2I4S0VURUJNNnBXS2VjWnRGVXNoU1lTMG5sVkN6enJiYktfR1g4Y054Z0pLLVFSQzBWOHd2ZURzSERBWFNLWGRFMnAtWWswMDhDYmRMRTRjM3JDclN2Nm8tVzAzQ256YUhsNTFERFVJZDVTRENnX1NZYkduaUNfcEtOY1ktMTAtRzlQenREbVE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
