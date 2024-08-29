# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Captain and engineer of Mike Lynch's family yacht both reportedly under investigation over sinking off Italy**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQTi1VdGFEZ0l2WlRyN0Iwc2RvcTV2UWptMFQwd1B1NDQ2eUJZSWRzWEFOQXo2akVxZ2ZjZ3FKd0JXYmJsQjRwZXp5N1FMT2RScFE4SmQtUTIxU3NGenVsdlVsZ2xpNjZ2RDc2Zy1nNVA4aE9lZmpXZV9vX0FGd0o3anJmTWFEVTBfR0w4bk5Sb3V1MUtRblJ3N1RraHdBQ1VwdlhxczhlT2Vnd9IBrwFBVV95cUxNd0xCTHFQQlBmNHFUODEyaGlQYU1NU19GVEhKdllQR2ZVekRHbHRVZmZfN0ZFOGo1Z0tMaVhQcHVrZDVaeFZSUHFlVm43dnp6cHJRQVdVbVloR1lfOXloNzV1WDV1Y1dxOHBfbGlCdzFLRDRITkhUVExZSnpDWk9CRUx4aWxPWUlSWFhvWXVYeU44eUlJNG9UdkdqRTRsclpXSFNmNk9PTU9Nbi1KRUlz?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
