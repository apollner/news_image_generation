# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Hunter Biden lawyer files ethics complaint against Marjorie Taylor Greene after she flashes his X-rated pics at hearing

[Read more](https://nypost.com/2023/07/22/hunter-bidens-lawyer-files-ethics-complaint-against-marjorie-taylor-greene-after-she-flashes-his-x-rated-pics-at-hearing/)