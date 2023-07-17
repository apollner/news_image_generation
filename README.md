# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Stocks are riding a wave of optimism as U.S. inflation recedes, but there are dangers lurking

[Read more](https://www.marketwatch.com/story/stocks-are-riding-a-wave-of-optimism-as-u-s-inflation-recedes-but-there-are-dangers-lurking-8b3ba511)