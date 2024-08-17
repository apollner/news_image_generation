# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hurricane Ernesto turns its attention to Bermuda, will churn up dangerous beach conditions for East Coast**

You can read more about it [here](https://news.google.com/rss/articles/CBMiogFBVV95cUxQd3hSZjktbGJCY2x0bV93Ty10bXlYdWJXU3pkVGNjVmU3U1JQdmlSUFQyUmtxLXpuN2R0N1dzUDZBMFota255X290QVZQUjZqYmc1WWFraVc3My1KWWFtLWpiM1ptVjhyZmRaRURZb1ZTYnFkSU5iM3ZkWmFFOXBsYUJJd0ZlX2p2aXkyVk5ram9wWElTR05WUVNqTGFPMWxlWVHSAZgBQVVfeXFMT3BuQkhUMW1nczVtOVhsdnBheFVodGM1a2hoNVBKbEZxZHc5cnY1akVuemtzOFhKVGZqbmszbEpYeVYwby1fT2p2WUphZ0s2T0dMc2VkdlhVMENOQ1VJUHRwTE0zblNnTW54bzNWSUF3azc0TUJJNGFWS25sUVJsOVhITTF6ejlyY2xUZmJ0eUZMOERhNVo2VUs?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
