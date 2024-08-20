# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Latest home washed out to sea in Outer Banks was owned by Pa. residents: report**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxPLUxpRG5ZQXFuNVVmN2FrMXl0WXdoMlNZV0IxbExJZ0JxSWNFT1hqWGw1OU5BSkh3MTZXQ0F0aEJ4QktLSDdCR2pER2d1QkdpLTVxZnctRG5EMHYwMFVENW1uek96czg0R1RWcDhoeWVWNjJ3U1QxZnRXeFUzbTJmWHhuODhYSmlVcGExRXhNMFdOOXpfSXZpMlRQWThWb0d3Z3VVQmlzaE5UUkNzV2Jtcl96U3YtWGIyREhNSNIB0AFBVV95cUxOblhvcDRiM3E5Vnc0SlVNdVRxWC1wWnJVU0pZUE1aSlJNZkJsUExqZmZSaFNzbUwxbUM5RmVzUHF2bzVQLTFfTGw3UDRJT3JBRkRXQ2lXLVFNd3p4TzhBOHJLZGZ2M1NncS1fRzFnb19lMjhDbUM4MEFMalpvYVpnNVF3OWlEQWhXSzB6bDRvdVdBRFlPQ3ZpbzBMRFRvdl9ucG9iNmEydDd4ZnB3RDlwZGFqVGZoWS12NDZOa2V0aVJTd2I1TWdIUE1mNW1DY0xh?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
