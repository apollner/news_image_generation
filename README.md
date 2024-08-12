# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Jordan Chiles stripped of bronze medal in floor exercise, US to appeal**

You can read more about it [here](https://news.google.com/rss/articles/CBMivwFBVV95cUxNbHJDWnRORTZDb05zSzd5NExIWWRSUElRNS1acm1LUnZOLXFmeFhrT0x4eWNTbHNqZklHMHBhM0FrM09XV1prb2ZmM0xxSWlzYVFzenhLWnpYcnJsbmpBdVppQkh5TlNyUldzcnNJYlVkMTBFWXJUbXExMktuQjhTc3JNY1FlTFZ1djRTanotSE45U1o2eThfc2ZkZm1kZDNod2JsZnZiUDd2YUZSMkJ3ekxoU29OOVRqXzdid0kyc9IBtgFBVV95cUxNSG43OWFQbm1Dc0JyVkZVZ2JfWU1IUk94VWF0TDZEQXJPQVZNZF9BMjRUVWdtX094R3VsTy1OLURHQnJFSnBuQW5henc0RHhHTDFVVVp6RnNBdTMyUEpiTk02ekFYU3dyU0w4ZHZvNnNnTUduZDBNNHJIOUVaMk42c0UwVjdWbm16bXNvUVBHREV3X2VhQk4zMm1NdTNoVVRFV1M0cFN4cFRZbTcxS0RvQWViOG1mUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
