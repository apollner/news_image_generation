# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Xbox Live Gold, Games With Gold Finally Being Phased Out In Favor Of Xbox Game Pass Core

[Read more](https://www.gamespot.com/articles/xbox-live-gold-games-with-gold-finally-being-phased-out-in-favor-of-xbox-game-pass-core/1100-6516013/)