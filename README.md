# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: 2023 British Open odds, favorites: Rory McIlroy easily ahead of Scottie Scheffler, Jon Rahm at Royal Liverpool

[Read more](https://www.cbssports.com/golf/news/2023-british-open-odds-favorites-rory-mcilroy-easily-ahead-of-scottie-scheffler-jon-rahm-at-royal-liverpool/)