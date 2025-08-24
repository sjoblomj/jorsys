# Jorsys
Content for the website [jorsys.org](https://jorsys.org).

This repository contains the Markdown-esque content for the Jorsys website, which is built using [Incunable](https://github.com/sjoblom/incunable).

## Building the Site

First, pre-generate content with the `generate_content` script, then build the site using Incunable.

### Building when Incunable is installed locally

```bash
./generate_content
rm -rf output
incunable content output resources templates
```

### Building with Docker

```bash
./generate_content
rm -rf output
mkdir output # If the output directory does not exist, Docker will create it but it will be owned by root
docker run --rm --user $(id -u):$(id -g) -v $(pwd)/content:/content -v $(pwd)/output:/output -v $(pwd)/resources:/resources -v $(pwd)/templates:/templates incunable:v1.7 /content /output /resources /templates
```
