# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**No-confidence vote could topple the French government for the first time since 1962**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxQR01QYmdRaHNBOUxmMFdueGg2MHY3b2pCRGc2dm0xd3dqVjQ4Ql9qN2t0MlotSFFUS1l4Si1SOFIzV0k1MmlNV3FrM0lqWkdSQmdVb2RITC1uYWQxTFZTQkJ2WGR2SU04dExJc3hSLUxsN3d2d3Y2VmhnMlQ5ZEJDUE9tMVNIRzcwaTVfRFptUEtDZzB4LUtocFRwSF9YRFZqcW1wdDVtRE95NkJv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
