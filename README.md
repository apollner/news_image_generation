# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Free on National Chocolate Chip Cookie Day: Here's how to get your own delicious treat**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNaGo2SU9OYmlNNXNNT1ZfRHNOZzg3aXNEZ2NxYzM5eHdxY3B2NDAxOWY1NmN4bTh5NE9FdHh1bUE1Vl9WZEw1bVFScGxFLWFnck5xdGw0alZWWkZNYTRBWmcyZXBQM0M2MVdRVGlMRVBNaXFLYk5udElnOTVjVVBtRXpSWmJ6UlFheVA2WUJGLS04Qm1BQ3BIRDZFT0haVkJvam16UUN0d0FSck3SAbABQVVfeXFMTk1wYmNKc1lJT0V3dG05OGlRaXhXLXcwN0tGd3hXQzhNQXo1TU9mdGNIYlk1WWJVMmszUS11dXNFd3BBVW8zcHZOTlpSWEFFSWd1aWJtRm1jS1FXNkVhdVdmczdPNjlPWURVUERMc2tncFpRaVI3eXlVU3VTSDVxT3ZCMmx0Unk5bDFkZ3hFbk0zUE81d1VPdndfdk1EeUpFNHc0emFFdmVTN3RCakdBekw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
