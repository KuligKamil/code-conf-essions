# Microserivces


## What are microservices?

Microservices are a software development technique —a variant of the service-oriented architecture (SOA) architectural style that structures an application as a collection of loosely coupled services. In a microservices architecture, services are fine-grained and the protocols are lightweight. The benefit of decomposing an application into different smaller services is that it improves modularity and makes the application easier to understand, develop, test, and more resilient to architecture erosion. It parallelizes development by enabling small autonomous teams to develop, deploy and scale their respective services independently. It also allows the architecture of an individual service to emerge through continuous refactoring. Microservices-based architectures enable continuous delivery and deployment.


## Why use microservices?

Microservices are a way of breaking large software projects into loosely coupled modules, which communicate with each other through simple Application Programming Interfaces (APIs). The goal of microservices is to increase the speed of software development and deployment. This is achieved by building a software application as a collection of small services, each of which accomplishes a single function. These services are built around business capabilities and independently deployable by fully automated deployment machinery. This approach allows for faster deployment times, more frequent updates, and more resilient software.



## Communication between microservices

* API Calls
* Message Brokers
* gRPC
* Service Mesh

## Pub/Sub

Pub/Sub is a messaging pattern where senders of messages, called publishers, do not program the messages to be sent directly to specific receivers, called subscribers. Instead, the programmer "publishes" messages (events), without any knowledge of any subscribers there may be. Similarly, subscribers express interest in one or more classes and only receive messages that are of interest, without any knowledge of any publishers.



## Service Mesh

A service mesh is a dedicated infrastructure layer for handling service-to-service communication. It’s responsible for the reliable delivery of requests through the complex topology of services that comprise a modern, cloud-native application. In practice, the service mesh is typically implemented as an array of lightweight network proxies that are deployed alongside application code, without the application needing to be aware. These proxies intercept and control all communication between microservices, handling service discovery, load balancing, encryption, authentication and authorization, circuit breaking, and other cross-cutting concerns.


## Microservices Issues

* Complexity - distributed system
* Data Management


Poly repo not mono repo