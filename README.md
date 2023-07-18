# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Black Sea grain deal expires after Russia quits

[Read more](https://www.reuters.com/world/europe/black-sea-grain-deal-expire-monday-if-russia-quits-2023-07-17/)