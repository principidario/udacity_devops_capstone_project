## Project Overview

In this project you will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

* Working in AWS
* Using Jenkins or Circle CI to implement Continuous Integration and Continuous Deployment
* Building pipelines
* Working with Ansible and CloudFormation to deploy clusters
* Building Kubernetes clusters
* Building Docker containers in pipelines

As a capstone project, the directions are rather more open-ended than they were in the previous projects in the program. You will also be able to make some of your own choices in this capstone, for the type of deployment you implement, which services you will use, and the nature of the application you develop.

You will develop a CI/CD pipeline for micro services applications with either blue/green deployment or rolling deployment. You will also develop your Continuous Integration steps as you see fit, but must at least include typographical checking (aka “linting”). To make your project stand out, you may also choose to implement other checks such as security scanning, performance testing, integration testing, etc.!

Once you have completed your Continuous Integration you will set up Continuous Deployment, which will include:

* Pushing the built Docker container(s) to the Docker repository (you can use AWS ECR, create your own custom Registry within your cluster, or another 3rd party Docker repository) ; and
* Deploying these Docker container(s) to a small Kubernetes cluster. For your Kubernetes cluster you can either use AWS Kubernetes as a Service, or build your own Kubernetes cluster. To deploy your Kubernetes cluster, use either Ansible or Cloudformation. Preferably, run these from within Jenkins or Circle CI as an independent pipeline.

### Project description

I have created an flask app (app.py) that runs a dummy machine learning model. The model is in working process and the idea is to take a short video from the camera of the mobile phone to the little finger of the right or left hand and to submitted to the model. The model will analize the video and will output an approximation of the level of oxygen saturation in arterial blood.

### Project steps

* Create an app.py
* Create a Dockerfile
* Lint app.py and Dockerfile
* Build docker image from Dockerfile
* Deploy backend infrastructure (EC2 instance)
* Deploy backend (install docker, minikube, kubectl)
* Create kubernetes instance and run cluster
* Smoke test to verify if kubernetes cluster is answering to port 80
* Blue / Green migration (update instance ID in instance targets of the load balancer)

All the steps were made using CircleCI, Ansible, AWS Cloudformation and a bit of bash scripting.  The folder SCREENSHOTS contains screenshots of all the CircleCI jobs.

### Implementation testing

* Upload a file to EC2 instance: curl -X POST -F file=@"file.mp4" http://ec2-44-202-144-154.compute-1.amazonaws.com:8000/run

* Upload a file to load balancer: curl -X POST -F file=@"file.mp4" http://test-Application-Load-Balancer-2096421632.us-east-1.elb.amazonaws.com:80/run 