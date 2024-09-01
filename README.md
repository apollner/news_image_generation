# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Family of 18-year-old killed in high-speed Michigan crash wants teen driver's mother charged**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOYTdyWUxYY2xmcENCbVd4anNXTGRSbXh3Mk5vUkNqaXFieGN4S1hsSXpaS0JpV0V4UEdPNHJHaFJHYksyVGM2SjJ4aXFhTE1yTzVocTlObDU1YTFwYm1HclBGYWtjM1VRZFBFcHA4VWJVcXFwNGR2ZEo3ajZkakhQRVJMRDB5TDlsWjJqdFEzNkxwaGV2RV9WWDNHR3FpQkkyMDRCdkZGZnBtVTBQZWJmZkl6eTUzbzA50gG-AUFVX3lxTFBZSWV0LUVJeGpydE91b3lhc19yTDRSX3V5ZFFmNlAxWkthQ2MtUXRhRUtwMGExcHdxbjFjVGNNVnN3aUVTNV9MV1lhdTlLM0RPbUlsaDdlLXZIeEtaTU9wbmdmRVJBSEVuNDZhS3NJSVFQM0h4NTY2b3BtczZmUTV3Vk5ONXQ5UUVQbmZtR2x3Qnh0RWJMRENUbVJ3cGtZMjZzWXh4ZWx0WkxwbVA2NUN4U1NnU2ZiaS1DMEJFdXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
