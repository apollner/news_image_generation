# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel-Hamas ceasefire talks: A timeline of obstruction**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxPRHZpMGFxNk5UWFU3bGdpb2tvLWlIRm5JVjlJdjYxeVZ6U1p2XzV1bG9wWk1tOTV3WEF6TGc0NUZKRU5nUEZtcklNeEpqdjhsRFdFaWo4SHlYbjJOeVU5R1E5TE5kV1E2RHluV2pKUzJyM1luMG9XNUxnUTdXVEliNFhVTlNmMHRvUXdyaDdNNnhnYnlWUG1PWi1iMNIBoAFBVV95cUxOUHh2OUlnZ2pXS3I5al9MWXN3ZVpwNVdTNEUzWmp0RVlZTjZnUElUWS1VOUtBWkpOVFlubFFYQjdCa3Z2eVVmTFJTMjRCanYtNmNuUHJuRGRWbHQ2bGllNHFTOGlVeTd2TDkyalczV0JGTDU4a3NNclgyQnFTZ1hqTHpqLU43bmJYUGNwMjFaMXlLWkF1WTRpMmlKZVZDZ0NN?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
