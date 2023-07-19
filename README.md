# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Australian sailor speaks about being lost at sea with his dog for months: "I didn't really think I'd make it"

[Read more](https://www.cbsnews.com/news/australian-sailor-lost-dog-rescued-timothy-shaddock-pacific-ocean/)