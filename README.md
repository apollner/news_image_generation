# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**USC vs. LSU live stream, where to watch, TV channel, prediction, pick, spread, football game odds**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1gFBVV95cUxPYUlzQVQ1OWxJV01BeThLQkduTndSemJLR1ZzVkRGMmhwS2JYSGFVMkhnZ0s1dUhEQWNveXcwV0hncUY2ZVNkU2Q3NEVNNHBIWDV6emc2X1NvcUkyQ2lJeExZVWliWVN3dGg4dHNlRVJob2g5R0dzWDVid3lncGtiN2xfd2dZVG4wdmJUdWlYaFQxYmxyTUNjMkJKZW9VWUNHRGJlR3dZZzNfbzlQQzVQOHNnRVZhcU1TOVpSTld1aVpjbElYYWdJblpfZHdGSTlDd3Q3UzdB0gHbAUFVX3lxTE1HdHhMUnMwVUtpVU5idktBNFVlUzBQMmwwcDhaZDU0MjFtMTNDWVFMN2VvWXRrNDBFeURWQnRFQ2JBaTR2NGMwTEJYekJEUFBJbDVyWlI1VHp3UXhCV0dWT01Fb0tNc0NvRTA2Y3ItSUh6UVdHczNsSVdldTQxTkkwd2lISHRrTEFQQnZLN0tsOThSOGhoYXRUcFhuWUl2LWxzU2tZU1doUGxCS3UwNFh5RXh0S1JEamVBS09NMmNpX3B2Y1JiWllkWGZScXZkNWl4a3oyek5MMjMyRQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
