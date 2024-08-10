# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Special Counsel requests delay in response to scheduling order in Trump Jan. 6 case**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOanR4TXl5R2haUXJqOUhzUVJsZEh0Y211VXlCV1B3dmtkcWJuQUtFNVVaeGpUdFpFaENLcW5NUWFNRHdoWE5rRmdOaV9rVDZGbEpKWVAyYVRXcnI0cWItVEJRTi1kVmRJRFZUR1RNZDk3RWM3eGRFRnprSnBocW1KTm5yVEN5bjU3bUJqM1FmR1YxSFJqMGFCXzRxMllKMzlncUVNOTV2ZVVsd1HSAbABQVVfeXFMT3Y2a3pCVV9heHp6MkRTdTVESXFYeWtHbXBlbW1meEh5dFdmRkVFNmJ0ZF9iczI0T3lJNl9YbVQ4OEpxT0Y3UjlCVnJWZ285Z0xiUFJ4ZmswTmlBb1JfVEw1SDRtd1R0R3FkVVpGUXUyLUh5REFTTnZWemFfV0J0d3p4ZE9qQnR3MWpfWTZXcXNPNnI1aExCaThKQW51aVVKWktXbF9qYjU3SERqWVEzNlU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
