import docker
import os
import time

def list_container_images():
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    print("---- Docker Container Image Report ----")
    for container in client.containers.list(all=True):
        image = container.image
        tags = image.tags if image.tags else ["<none>:<none>"]
        print(f"Container: {container.name}")
        print(f"  Image ID: {image.id}")
        print(f"  Tags: {tags}")
        print("--------------------------------------")

if __name__ == "__main__":
    list_container_images()
