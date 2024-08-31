# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Zelenskyy fires Ukraine’s air force commander after deadly F-16 crash**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxNeXB1WjBVTXBTUXNzYndPX042c1ZpTVNUUl9VNFdrcXJmZ2RlenA0ZFNMSTRXOWxHcDJDd0hFZVBKYmlKVngtYjhSNHFNNG13ZXV5VFE2WEtnaTBIbENwNFJiemZzVGxrQzQ5NjJZaU1sM2VIX2xtVUFrak9ubDVCRjYtTHhabzFyT3h5UnVpb2dGQTN5ZzVVZlV1MEdFYWRkc3ZOWkdPeVlWNWwzR3fSAbMBQVVfeXFMTk50S1JFd3g5emFGUmUtRWJyYnJNSWdkbjNXVEVETFVGRWZUOUlsWFp1RDVvdXM1X2JSYTQwandkNTlFYW00TncwampMZm1JUjFNMmEwaHJuNmY3dU1xN0RRRXpUcWdkajRpMmt6YVcwcW1WWHZsUHFyZ3ZfVERYYVFCSjR6ZDNuRHV5TEZLSXJkaFNSRzlpQkdZQ1RwLWh6Qy1uVl8yQjNpRjhqa2d3Y3hUV3M?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
