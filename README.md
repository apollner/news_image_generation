# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Los Angeles defies Newsom's order to clear homeless camps**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxQQlRHMWNGVGJFWkE5ZWx6d3JPeF9xaFA0eElkX0dlNVpvM3BiQmNhZmc0Y0dYc2YwM2JWNHYzbV9ha3RjOGFpbXNCQUZ5enBva2ZpeGRtSDdvOFl2anF4Rzk0aWc2NHI0enF0VTBnbERiM1puYU83VzBZSHdIRkJNdWt1YWgwd245SjVkRVJ6ZThvMUthWnpYOU5jWXdOT3I2bTlfN01R0gGuAUFVX3lxTE9WcUtXLUFESmFxcnE0N1ZIa3VkNmJDNmJzY1JCRkVUZTZVdmtZbnhLNEYweUExQmxMWUFLcE1yREZQeS1iTXlnTW5nNVlMXzBZbkprMGVpVXBPTy1CVFJYeklrdzZ5Ym9aUW5zX0FvNW5ObGlsWUJmTlpXa3A2R2ZENkdwYU0zb195c2pRTEt5LXh5ZFZuV2tiV2dtWER6NE9iZXNneXhQZ3h6cHNpQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
