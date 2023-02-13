# Microservice
This repository contains the code and configuration for a simple microservice, packaged as a Docker image and deployed to a Kubernetes cluster using Helm.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

[Kubernetes](https://kubernetes.io/)

[Python 3.9](https://www.python.org/downloads/)

[Docker](https://www.docker.com/) - Containerization platform

[Helm](https://helm.sh/) - Package manager for Kubernetes

[Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
[ArgoCD](https://argoproj.github.io/argo-cd/)

## Installing Local
1. Clone the repository:
```bash 
git clone https://github.com/lightyear0/microservice.git 
```
2. Build the Docker image:
```bash 
docker build -t microservice .
```
3. Push the Docker image to a registry:
```bash 
docker push microservice
```
4. Install the Helm chart:
```bash 
helm upgrade --install microservice ./microservice -f values.yaml
```
## Setting up GitHub Actions
1. Go to the GitHub Actions tab in your repository.
2. Click the "New workflow" button.
3. Copy the contents of the `.github/workflows/build-and-deploy.yml` file into the workflow file.
4. Update the environment variables in the workflow to match your environment.
5. Save the workflow.

## Deployment
The microservice is deployed to a Kubernetes cluster using Helm. The Helm chart is defined in the microservice directory, and can be customized using the values in the values.yaml file.


## Deployment Automation
The microservice is automatically built and deployed to a Kubernetes cluster using GitHub Actions when changes are pushed to the main branch. The workflow is defined in the `.github/work

