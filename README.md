# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Las Vegas police search home in connection with Tupac Shakur murder - KLAS

[Read more](https://www.8newsnow.com/investigators/las-vegas-police-search-home-in-connection-with-tupac-shakur-murder/)