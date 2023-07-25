# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Boat smashes into a house in wild crash that left 8 people hurt at Lake of the Ozarks

[Read more](https://nypost.com/2023/07/24/8-people-hurt-after-boat-runs-aground-smashes-into-home-at-lake-of-the-ozarks/)