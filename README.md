# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Florida residents may hear sonic booms during Falcon 9 rocket launch on Thursday**

You can read more about it [here](https://news.google.com/rss/articles/CBMitgFBVV95cUxQRVRNMU44eGZBa2JJVGpqODQ2dmRQMkMwS3VydjlhdWt1bDlZNlZ3WmpTcFBBZVB1cGJqcUdwZmxIdk1kWWJkNTAxODcwWkI5Yk4tYzZJYWtzc01MS29PMi1QZEJUWm8zV2w2SEZsUlJRbHNaa1hwS0xDcm5HaU9TTFZIeFl5MWpXOHFidzhFRVdMR0tCRXBCZ0ZNY0h5dDlfSF82anA2RXcyTk5XNDFPaFhHanJhZ9IBuwFBVV95cUxPZm51a3BmOTkyeGtGWm1jTGctMGkxaFc4dEhMZS1nN2xrZjBXczlmek9CT19jeURmQkxjX1dNMFppX3ItUU8zbzhTSklTWVRGYmswY2FaYUZLT3NHci1MYUhyZkVpNHBjM0JJSkJKaW1DaFl5NTlCT3E1UFVfMktjRmVwZjJhRDNHbVFDY1ZlMDVYWGlHa1o3RmEzWVhuaWU4WW96N1NRZHpfVm16UGRFcDNvLVNkb0QtcE9R?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
