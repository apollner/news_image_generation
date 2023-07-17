# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Steph Curry wins 2023 American Century Championship with eagle on 18

[Read more](https://www.usatoday.com/story/sports/golf/2023/07/16/steph-curry-wins-2023-american-century-championship-eagle/70418780007/)