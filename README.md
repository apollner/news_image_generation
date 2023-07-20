# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Barbie First Reviews: Hysterically Funny, Perfectly Cast, and Affectionately Crafted

[Read more](https://editorial.rottentomatoes.com/article/barbie-first-reviews-hysterically-funny-perfectly-cast-and-affectionately-crafted/)