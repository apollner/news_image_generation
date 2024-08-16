# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Biden administration releases prices of 10 drugs in Medicare negotiations, says U.S. will save $6 billion in first year**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxPRXhfb0NXZGJlVEFKbndJZmhtQnQ1X2xZY05nLVQxeTZyTXZVby1mWlR6ME1GVW1rQ0hTT0o3dFhPZjlBYVBjaW9zOEFxdFhTU1hPRUJuNXRPenhXd3RBdmJ2SlA3VUVlem9mMHA1eG1YTlY5QUFxUDRqQkpxOFdzWFRaWlR4Qy0taEJXOE1MLXJsZkt6S3VwVDd5YnFOclZmeTB6bU9tb9IBrAFBVV95cUxOdFlaTkUzWnE0Y2tpTzJHT1ZiZUJSVWE1M05oVEYzOWxGX3R6ckI0Z0JCVGM5TUxhZzJoMUdMcVdwbW5aeDAxVTFLZU91X1JQTF9wU1FpYWFvNVpJbC1lWV91WFZ0VnNFRDI2Zm9PMWJ5d3EtMGNaTGk5M09GWkhjRzNMcDFGNFhhZGU0WUVaU2FITkNxTlZMYVFWOEI2RW9HMFM0OXRTamszTG5f?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
