# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: South Korea flood death toll rises to 39, Yoon blames botched responses

[Read more](https://www.reuters.com/world/asia-pacific/south-korea-flood-death-toll-rises-39-yoon-orders-all-out-effort-2023-07-17/)