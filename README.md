# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**SpaceX kicks off Labor Day weekend with return to Falcon 9 launch from Cape Canaveral**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgJBVV95cUxPckFfR0xOOGFhRTFSV2w3VWRudVplUUIzdmM3S2tzTnlpRmpWVmxDTGt0T0U4cGJCbmFfWmdab0dDU1hfZ0RwczlNLThSazhuYVg1YmtYRElNRGwyVVNaXzNVci13b2ZLSWVxc2RaREpzX1BodG9NZWVUV0dESEl6SkJLNU96SlQtR3VVZzlVa2RKRUhkNVc0U1R1eUQtc050Z0VSNWJYbTdwd1htSnJZNXJObGRZejI2a1FxYXhvc2NpbndpQkprUjJOcXB3VXh6SzgzVHB3YnBXeGVoQV9iT2Rhck95bEVVODZrbE9sWVhlMjJocHRCSEZvM2dfd192aFI4WEN1bXNkejZGeUE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
