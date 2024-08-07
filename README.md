# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Slow moving Tropical Storm Debby could bring "catastrophic flooding" to parts of Georgia and the Carolinas, forecasters say**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxPdGwtcno5bmJSZW9lbWxFem05cV81cXpMV2I3aUtLd2JOSTA0d3l5V3FlLVc5Z3FieGVJV0FWaUVOYmV6TFRGOWIyalpSTWJvSUo0bVh4UGFiSmd4Sl9qWHVFT1NGd2d2MzZBNEVfR24tQno1UmVodjY3TUtBM3drS2pGU1Iwc2hSNk9ldjlOX1Z6X1JMczhjSUlCeml3d9IBowFBVV95cUxPSlZ2NVFuUmgwcE5XVWpUVWFKQmU1TmNmWjhvTXRjc2N1X0twMGZrbzhUb2RxN1AtRjlzdnBDaV9CVzlZNVhHeDkzY29uLTV6bU51cmcwOUNGS0FsSnJsekwzSWQzR1l3MmdjMXN3d2FrYTVqWFpQZl9maGNmc2twcHhwbWpDWUprNEFjaFNxZURGeWRHVWpyYUtoYnpKTW1SU05F?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
