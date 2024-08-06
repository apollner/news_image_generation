# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**U.S. fugitive known as "The Devil" captured while working as cop in Mexico 20 years after Ohio murder**

You can read more about it [here](https://news.google.com/rss/articles/CBMirgFBVV95cUxQRWV4MnNZejFpdjhGV2c2a2xEMThBWlF4dVZPVFdSN1ZYelhmcmRvd3c5M2FPX1YySVZOelNPcXRQSVlSQUJ2RzVZc3RWaWR5R3Fta0RpRFY0UjhkbnVMU0xDVGNXRGVYeWoxTnJVby1aTVR5b0dFeF9QRjJmSjJLZWxkdWZTSEg4SXVERzd2aTkyWUl1ZE9RUEFYRHZsRGJXRmFwdWh3bFZsaS1VVFHSAbMBQVVfeXFMUG1vb0FOMFREMDVuLXNUMEtRTVpwRDlJdEpndkp3dHgycHhMZDdtQ0dxLUlCWEMtc1pDYTVEaUIxZ0hVQ1FFckdVQVctaGdvTWlFSXJRYjNJR3B6Z0tvdGhoUTZUWEV3ejdBM054TnJKNTlUd1dSa25RUXd3MjBZVHVkaGtmUThBVzJDZjNla2JFQjZpQUk5QlRYTUJDUTVPa05TcGtxSTVCTkxnZDVUcThNTTA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
