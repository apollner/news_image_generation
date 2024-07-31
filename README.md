# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Richard Gadd Says He “Could and Would” Testify in the ‘Baby Reindeer’ Lawsuit Against Netflix**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxPU0NSSTBLS1FkdFZrYUhJRENJQ0FNal9YTmx2N3d1V0JXc1FBVzN0ZXY1bldDRFBzR0pXcFc3QzFYdl9acnhTRnFkMVhKSWtObm9TWnNtbHZCT2RYN1phVXB0Q2NLSFVwVnh6MGt0UmtqcFpSc1RJaW1iV3VMMHJjajRvMDV6QWJOXzNoejlQb1BpLWY1b3FUREFva2MxSm0tLXExbmlVa0NmejF6eDZzcVlLUnlQMTBVVUNmRNIBwgFBVV95cUxNYzZJV1JmTVRxbm9SOUFvVFNvajdCclBmTnk1T2xTNDlOOTA0OGNBcXlnRkFCdUlGa1ZMMVNUVElIdVdsYlRYa3YwbG1hLTFDcXpTcWFCOXhUMjV0SDM1a3RZTDVqQnRWQzZVMVljQS01MVNHQ1AzVWk5RkRteGdxeUNuRDIzaGJNYVJZbFo4MXM5RjNtQ0VtVkJVZ1NkaTNrRUsxQmpzSnE2TFJXMXJaVkZkZ19VekNKQkVRX1NSZk5MZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
