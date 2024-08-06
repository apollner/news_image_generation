# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Djokovic defeats Alcaraz for Olympic gold to clinch ‘biggest success in career’**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOSFZhNWpYNDY3UExGemk0UGdYaktGOVhtOTJEaFpxVENsZ1RCX3M0ZDhJLWJsMUZNbjZHYy1kQmtGQnAxSmxlNloxc0d0UGRMcUxJVUNpVmJ0SXMwTFRTRkJSLXJfX0dkenA0WTBnaUNKTW5RSmYtN1czYVltalhaT0hrRGhtdmpZZ3p4TDBSWDNlenVRSS1fbkNsV05DSTFaUkRxbEw2THh2WVVSSVNZbkFtemRLT0o5dDhhcktBN0lHMGphYTNCNWNNV2ltenJl0gHQAUFVX3lxTE5FVUt2dUpKc1RrLWl3Ty13aXMzOEQtelFIR0VGWEhaNmJtN3hsaG9nN1VRcko0SWlXdGlDSmpUWHJySUdtTTYzQUtYRjg1cEVNcVZwSElaQW1aaUhGODRLTkZicWZpODktZWZVS3JYMFRJNFkzcXc5TGdSTkp4S2pXNm15MzUzZm5GNzR4dzM1aEE1TmdMTnZxWDJveEdGbUgtWkZlMkhYYnBhejVja2xnNnk0aTZUVE5YNVRSNExRYnhCWTloS1NIRU9XVUl1N08?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
