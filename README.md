# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**United Airlines flight from Cancun to Chicago diverted after passenger hurt during severe turbulence**

You can read more about it [here](https://news.google.com/rss/articles/CBMi5wFBVV95cUxPZTY0RUlKQjR4YkxoYko0VGU2cEs4OGFCd05STEpzdEtEM1A0ZDFlbUtYX2F2TDRhZXRLS0hrekp6QWdDNm5tX1Q5WHN1UG9ST3ZrU2IxN1JiYjRIVG1rVXdpYnRkRVRWVTdmSHQ4WER3WDZsLUtkdTdjNF9GUEdYZGQxYnM1d1ZFZU5KdDZhMU9Tbm9uLU1xMEZ1WC1KM0dUS2kyNXJZeDU3cDdHTE1zTlkwUERMeEp2dUpaQmNucmlUSTlSN05JdF93Mm9UN2hfclQ5VUFjcG15T1p3RjNPc3RxQ1dTY28?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
