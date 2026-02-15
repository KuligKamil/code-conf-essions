# gRPC for Beginners


## Short description
This workshop is designed for those who are new to gRPC and are eager to learn how to build high-performance microservices with it. In this hands-on workshop, you will learn the basics of gRPC, a modern RPC framework, and how to use it with Python. We will start with an introduction to gRPC and where it excels over traditional REST APIs. We will then dive into the specifics of gRPC, including Protocol Buffers, service definition, and the four communication patterns. You will learn how to implement services, define messages, and handle different types of communication. A pre-configured Docker Compose environment with Prometheus, Grafana, and test suite will be provided so you can focus entirely on writing gRPC code and measuring performance in real-time. You will also cover best practices for error handling, authentication, testing, and performance optimization. By the end of this workshop, you will have a solid understanding of gRPC and how to use it in your Python applications. You will be equipped with the knowledge and skills to start building efficient microservices with gRPC. A basic understanding of Python and HTTP/REST is necessary to get the most out of this workshop. Preparation: Participants only need to bring laptops with Docker and Docker Compose installed. All other tools, dependencies, and boilerplate code will be provided pre-configured. Join us in this exciting hands-on workshop and start your journey in the world of high-performance RPC with gRPC!

## Detailed abstract

This workshop, "gRPC for Beginners", is a comprehensive introduction to gRPC, a modern Remote Procedure Call framework, tailored specifically for Python developers who are new to gRPC.

Section 1: Introduction to gRPC and RPC Concepts
We will begin with an overview of RPC concepts and why gRPC is a powerful tool for building microservices. We will compare gRPC with REST APIs and discuss its advantages including performance, type safety, and code generation. This section will provide a solid foundation for understanding gRPC's role in modern distributed systems.

Section 2: Protocol Buffers and Service Definition
Next, we will delve into Protocol Buffers (protobuf), gRPC's serialization format. We will explore how to define messages and services using the .proto syntax. This section will give you a clear understanding of how gRPC structures data and defines service contracts.

Section 3: Implementing gRPC Services
In this section, we will learn how to implement gRPC services using Python. Through hands-on exercises, you will create servers and clients, understanding the four communication patterns: unary, server streaming, client streaming, and bidirectional streaming.

Section 4: Testing, Performance & Monitoring
We will measure real-world performance using pre-configured benchmarking tools, write unit tests for your services, and visualize metrics in Grafana. This hands-on approach ensures you understand not just how to build gRPC services, but how to optimize and monitor them in production.

By the end of this workshop, participants will have a thorough understanding of gRPC and its application in Python microservices. They will be equipped with the knowledge and skills to start building efficient distributed systems with gRPC. This workshop requires a basic understanding of Python and HTTP/REST concepts.

## Proposal agenda

1. **Welcome & Introduction** (10 min)
   - What is gRPC and why it matters
   - RPC concepts overview

2. **gRPC vs REST** (5 min)
   - Quick comparison: performance, type safety
   - Why & when choose gRPC

3. **Protocol Buffers Hands-On** (30 min)
   - 📋 **Task**: Define a simple service in .proto file
   - Message definition, nested types
   - Service definition and RPC methods
   - Code generation walkthrough

4. **Building Your First gRPC Service** (40 min)
   - � **Individual Exercise**: Implement your own server and client
   - Build a user service with CRUD operations
   - Test with provided client
   - Debugging and troubleshooting

5. **Communication Patterns** (30 min)
   - Overview of 4 patterns (unary, server streaming, client streaming, bidirectional)
   - 📋 **Task**: Implement streaming example (chat service)
   - Extend your service to support bidirectional streaming
   - Performance implications of each pattern

6. **Asynchronicity in gRPC** (20 min)
   - async/await patterns in Python
   - 📋 **Task**: Convert your blocking service to async
   - Benefits: handling concurrent requests efficiently
   - Live demo of async performance

7. **Testing, Performance & Monitoring** (35 min)
   - Pre-configured test suite with pytest
   - 📋 **Task**: Write unit tests for your service (templates provided)
   - Running performance benchmarks with ghz
   - Visualizing metrics in Grafana dashboard
   - 📊 Live demo: See your service performance metrics in real-time
   - Using grpcurl for debugging
   - Common issues and solutions

8. **Error Handling & Best Practices** (20 min)
   - gRPC status codes and error handling
   - 📋 **Task**: Add proper error handling to your service
   - Retry strategies and timeouts
   - Performance optimization tips

9. **Real-World Topics** (20 min)
   - Authentication (mTLS, API keys)
   - Interceptors (middleware pattern)
   - Monitoring and logging basics
   - 📋 **Optional Task**: Add interceptor to your service

10. **Deployment Basics** (15 min)
    - Containerizing gRPC services (Docker basics)
    - Environment configuration
    - Cloud deployment overview (brief intro)

11. **Final Review & Next Steps** (10 min)
    - Recap of core concepts learned
    - Common pitfalls to avoid
    - Resources for continuing your gRPC journey
    - Next projects to build
    - Q&A and open discussion

## Pre-Configured Docker Compose Environment

All participants receive a ready-to-use Docker Compose setup that includes:

**Services:**
- **gRPC Services** (Port 50051) - your code runs here
- **Prometheus** (Port 9090) - metrics collection
- **Grafana** (Port 3000) - visualization dashboard with pre-built gRPC dashboards
- **ghz** - performance benchmarking tool (pre-configured benchmark scripts)
- **Redis** (Port 6379) - optional for cache experiments

**Pre-built Components:**
- Test suite templates with pytest fixtures
- Performance benchmark scripts (latency, throughput, concurrent connections)
- Grafana dashboards showing:
  - gRPC latency percentiles (p50, p95, p99)
  - Request throughput (requests/sec)
  - Error rates and status codes
  - Server resource usage
- Docker networking configured for easy service communication

**Your Role:**
Write your gRPC service code in `service.py` - everything else runs automatically. See your metrics update live on Grafana as you code!

**Total Duration: 240 minutes (4 hours)**
**Format**: Mix of lecture (40 min) + individual hands-on exercises (180 min) + testing & discussion (20 min)
**Recommended Structure**: 
- First 90 min: Core concepts + first service (Docker up and running)
- 15 min break
- Next 85 min: Advanced patterns + testing (write tests, run benchmarks)
- Final 20 min: Performance comparison + discussion
