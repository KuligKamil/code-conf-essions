---
title: Get DB & Connect to it
---
# Get DB
To connect to a database, you need to have a database instance running. How to have are a few options to set up a MongoDB database:

* Atlas Free Tier
  
  Sign up for an account on the [MongoDB Atlas website](https://www.mongodb.com/cloud/atlas). Follow the instructions to create a new cluster.

* Install on Localhost
  
    Go to [MongoDB installation page](https://docs.mongodb.com/manual/installation/). 
    Follow the installation instructions for your operating system.

* Docker Installation
    Use the following command to pull and run the MongoDB Docker image:
     ```sh
     docker run --name mongodb -d -p 27017:27017 mongo
     ```

<!--   *  MongoDB Atlas offers a free tier that allows you to create a cloud-based MongoDB instance.
  *   Install MongoDB directly on your local machine.
  *   Run a MongoDB instance in a Docker container.
 -->