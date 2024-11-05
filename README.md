# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hurricane watch for Caymans, tropical storm warning for Jamaica as system in Caribbean expected to strengthen**

You can read more about it [here](https://news.google.com/rss/articles/CBMikAFBVV95cUxPdzBJV0ZlS0dUSFdYdnZ0RERZS29SdkJaR0dfdnZYNC1WRUdqSl90ZmcwUVpjYTBnMDlBcW1DU05tQ3NteERRdTJfLWk3T1JiWmR1aDNhTUk1NTFMaThRdFk1Q0Jxb3ZPRXJIN1JUM19RU2JPWEI1NHNDMDNnVVRnNUZXVHdmM1dlS1N0Ti05aWjSAZYBQVVfeXFMUDRNOERkOUhUa19oTFRERWZrMHVFSFl5MjAyTWhzNHZmekpBRHQ3UGc2RGpYXzhlWkoyTk9MUjRDR1ExcTJYSXFtWEprTTFLTHF3Wk1rcGlsaFVFRjh0aDdyZlJia1pMNE9GY0Z1TkJTdzJIRWR2VEhWdEN4TFBEZW5mem9uekdfUDBDQ25POWVoTDZTbjdn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
