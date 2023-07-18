# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: SEC Media Days 2023: Greg Sankey stumps for federal NIL help, updates conference's stance on expansion

[Read more](https://www.cbssports.com/college-football/news/sec-media-days-2023-greg-sankey-stumps-for-federal-nil-help-updates-conferences-stance-on-expansion/)