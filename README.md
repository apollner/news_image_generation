# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Former national security adviser says Trump can be manipulated with flattery**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxQN2JxdFRWT2ZVNlQwRkI3dXlNNmZLb2owd3FqT0RfaWE0d3dzTHJxQ0F4b2pETDNlUWROam1IVklIYXhMNVlmdnN4UUFNWEp5MXVycldoQ0w1azFFWFBBTmk1ZGxQSXdLSlFOMGg3cnpsYUw5ZUw0R2VRV2ZGcUVlb2l3RFpId3k4ajdMN1EzRDBBUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
