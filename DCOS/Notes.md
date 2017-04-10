# DC/OS Notes

## What is?

### Distributed System

As a distributed system, DC/OS includes a group of agent nodes that are coordinated by a group of master nodes. Like other distributed systems, several of the components running on the master nodes perform leader election with their peers.

### Cluster Manager

As a cluster manager, DC/OS manages both resources and tasks running on the agent nodes. The agent nodes provide resources to the cluster. Those resources are then bundled into resource offers and made available to registered schedulers. The schedulers then accept these offers and allocate their resources to specific tasks, indirectly placing tasks on specific agent nodes. The agent nodes then spawn executors to manage each task type and the executors run and manage the tasks assigned to them. Unlike external cluster provisioners, DC/OS runs in the cluster and manages the lifecycle of the tasks it launches. This cluster management functionality is provided primarily by Apache Mesos.

### Container Platform

As a container platform, DC/OS includes two built-in task schedulers (Marathon and DC/OS Jobs (Metronome)) and two container runtimes (Docker and Mesos). Combined, this functionality is commonly referred to as container orchestration. In addition to the built-in schedulers for services and jobs, DC/OS also supports custom schedulers for handling more complex application-specific operational logic. Stateful services like databases and message queues often take advantage of these custom schedulers to handle advanced scenerios (e.g. setup, tear down, backup, restore, migration, synchronization, rebalancing, etc).

All tasks on DC/OS are containerized. Containers can be started from images downloaded from a container repository (e.g. Docker Hub) or they can be native executables (e.g. binaries or scripts) containerized at runtime. While Docker is currently required on every node, it may become optional in the future, as components and packages migrate to using the Mesos Universal Container Runtime for imaged and native workloads.

### Operating System

As an operating system, DC/OS abstracts the cluster hardware and software resources and provides common services to applications. On top of cluster management and container orchestration functionality, these common services additionally provide package management, networking, logging and metrics, storage and volumes, and identity management.

Similar to Linux, DC/OS has both system space (aka kernel space) and user space. The system space is a protected area that is not accessible to users and involves low-level operations such as resource allocation, security, and process isolation. The user space is where the user applications, jobs, and services live. The built-in package manager can be used to install services into the user space.

Unlike Linux, DC/OS is not a host operating system. DC/OS spans multiple machines, but relies on each machine to have its own host operating system and host kernel.

## Architecture

### Software Layer

At the software layer, DC/OS provides package management and a package repository to easily install and manage multiple types of services: databases, message queues, stream processors, artifact repositories, monitoring solutions, continuous integration tools, source control management, log aggregators, etc. In addition to these packaged apps and services, the user may install their own custom apps, services, and scheduled jobs.

### Platform Layer

At the platform layer there are dozens of components grouped into the following categories:

* Cluster Management
* Container Orchestration
* Container Runtimes
* Logging and Metrics
* Networking
* Package Management
* IAM and Security
* Storage

These components are divided across multiple node types:

* Master Nodes
* Private Agent Nodes
* Public Agent Nodes

For DC/OS to be installed, each node must already be provisioned with one of the supported host operating systems.

### Infrastructure Layer

At the infrastructure layer, DC/OS can be installed on public clouds, private clouds, or on-premises hardware. Some of these install targets have automated provisioning tools, but almost any infrastructure can be used, as long as it includes multiple x86 machines on a shared IPv4 network.

### External Components

In addition to the software that runs in the datacenter, DC/OS includes and integrates with several external components: the GUI, CLI, package repository, and container registry.