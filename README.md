# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Notre Dame vs. Texas A&M live stream, where to watch, TV channel, prediction, pick, spread, football game odds**

You can read more about it [here](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNSWpvakQ5RzdjRDN6RV92WENpWU1zWGhpUHRhY3ptVkh5dU95eUJ5MlNoTk5NOE9Ja25GVnNrck5GNTZZTnhDVXd2VEhnaTkyWm1jNnVTV29mNnAtYV83YlZNYkNIbTVQWVNIZTN3ZlpZWk93alFoQ25NMXVBNnlxOFVCX0k2SFpJNmFSSnlBTzJNdXNHVE5UZzBVWHc5VVhrUnc0d2FMa1RUQlZqWlMxci1KU2J2SjRrUVlaZU5tcjNCZGJxREo5a0FBMnJYSzBLcDRwZUJXMVRvcVRTbTY4UWxac19mRUnSAewBQVVfeXFMTkRqVmZVcTlGLUVMVzJDZzRMX2c4LWd6dlFicWxpdThEcURQRUliR3hzU3ItdFlNS0F0YWpFaGRXOVFETktJRnpyUFBMMGQ2OFh4Z3V0djB6dVJxa281QkNBM3QxZDl0Wm5PWlFSdHZDRDVYOTIwSEZqSUd5eDFVcnJPdkI2V2VqSlNUOEpsNU5CancyWEJmUnNReko2Sk10NFk2UlFSVDg1Ylk0YUowT05oVUZXWnY2bktNR1JxbThCSExtYmpidGxDUVBsUE92Y3J5NlhPSGQxeHlRUEc5NDJuVDFtNlRRWHJsVkQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
