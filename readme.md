# Cloudflare Dynamic

## Intro
This tool will automatically update cloudflare dns ip address with your current ip address

## Development
- Develop in Docker enviornment
- `docker compose up`

## Cron Job
- Update `root` file to update the cron job

## Production
1. Building Image - `docker build --tag=cloudflare_dynamic:1.0 .`
    1. Remember to add the . add the end as that will build the whole folder
1. Running Image Container - `docker run -d --env AUTH_EMAIL={email_address} AUTH_TOKEN={api_token} --name {container name} {image:tag}`
    1. Make sure that the container name is not already used before creating the new container

## Required ENV Parameters
- AUTH_EMAIL
- AUTH_TOKEN