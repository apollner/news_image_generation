# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**National Hurricane Center tracking 'robust tropical wave.' What will be impact on Florida?**

You can read more about it [here](https://news.google.com/rss/articles/CBMi_AFBVV95cUxQM0tsajgzNGdtd1hpanRZU0F2RDBjVndkRTJ3UXVBTmpCMWI4TElTdVZfQjROX21xUVRQdmk1R1JPX190UWlhakdWVEJ0U2taNV93Y0xLQXpESXE5MVN1R0FNSFIxSERjSEtodlU1a0dDN3RiM2haanZBYnR3TGpLX2hnMTNQYmR6X0pXWDFTUnF0cndfUkRfcDdOa1I3Z3BKUjlGd05yNENaYUdJeW9jVlBEQzdzZVB3STcxblJLbnRuUlpmMnRaNkw5Z3pGaUJEbEx2WU56Z2xjdGRxM2JHNWtGZURoRHpZSjJDckN2ajhndHZtaDlSZXBCOFQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
