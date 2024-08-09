# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump says he has agreed to offer from ABC News to debate Harris**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxPTUZsVmFiZVY3cU5pdWRJYVIwRU5HZjhXUDVaOWxvTV84REh4X0hJRHJMT1l4dnVQZjlVOTJPVWNzamRNbjFrbkdaeXNxWWZUZWJuLVkwcmhRVVJUTDJXUjdlSkphZzhORm5DbzdLeTBaTnpyQnJHeHI3Vjg5OUVhWHY5WEdSVjVnZG5LSFdxd9IBlAFBVV95cUxOOVNFX0hZM0xsOUJzbmNobDdMLVI2NzJ0S2t6RGw4aHJndXd4ZndBS2JqZ19GbEszNmpsaWU0M2ZVbnIyb0tBRTB2ek1yMHhYRGxBSmJlRXNqcDR5czc0TnhNdDctZ1Z3NW9aWU9HWk51U2htS0s1emdkZzZ6MUkyQm8xRXlaVXdiY3RsaWNja1I2Nl9u?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
