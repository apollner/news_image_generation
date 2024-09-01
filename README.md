# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Georgia vs. Clemson live stream, where to watch, TV channel, game odds, spread, prediction, picks**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNa0NrQTZ4bUJPdDNDczVKcmc4a3VBQjM3bFF0Nk93YUswbHgxY1FSdTlIT2NhbFhPOWh3UEdlQVFaa1dNdXhwM1VIbEU0R1NFa2c0VnpjeHpYNUg1bzV0TWxodXVtNHlkUVp4aGhDU3ZNdDIzNHBQa0VNTEw0NFdzTG1lOS1DTV9nUWUtZFBDcUg3SE8xRFJ4Z3RBU3JDTnFQclFMQWhXeFcxeF9pVzF0akJDaXlKVXdyYVVGXzRNMUptRFNCWjEwNnZnYThzT3B0SEpvSFRn0gHbAUFVX3lxTFBQWUp1U0dYckNmZC1KTzZ4TllXTllTcm1SeWNEZ3EzTnl0RmZ5LWp3T0Z0YzJ0N21FeFlOWko5WEFkU0VTanR3M0FTMUQ5T0F5cnNFdE9FaW9qMWZmUFQ1U2FKalB5ZXlZZDRvS0xXNFdLVVVtTi1LWk9KMVRtbXdSMG9PVmJlVS1uZy1JbDd3V0JpNEY2bzdPTHBUWFBEUlBaWmt2bm5PN2ZJN293T3NaMW45ZS1VbUNXLVVoeFVRVVhLSFVzVWFWRG51ZERRQndqRzNwZGFIYmdOQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
