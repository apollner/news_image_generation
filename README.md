# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: 1 dead, 1 critically injured after being knocked from gondola at Quebec resort

[Read more](https://abcnews.go.com/International/wireStory/1-dead-1-critically-injured-after-knocked-gondola-101326714)