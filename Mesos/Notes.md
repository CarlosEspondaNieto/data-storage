# Mesos Notes

## Architecture

The above figure shows the main components of Mesos. Mesos consists of a master daemon that manages agent daemons running on each cluster node, and Mesos frameworks that run tasks on these agents.

The master enables fine-grained sharing of resources (CPU, RAM, …) across frameworks by making them resource offers. Each resource offer contains a list of <agent ID, resource1: amount1, resource2: amount2, ...> (NOTE: as keyword ‘slave’ is deprecated in favor of ‘agent’, driver-based frameworks will still receive offers with slave ID, whereas frameworks using the v1 HTTP API receive offers with agent ID). The master decides how many resources to offer to each framework according to a given organizational policy, such as fair sharing or strict priority. To support a diverse set of policies, the master employs a modular architecture that makes it easy to add new allocation modules via a plugin mechanism.

A framework running on top of Mesos consists of two components: a scheduler that registers with the master to be offered resources, and an executor process that is launched on agent nodes to run the framework’s tasks (see the App/Framework development guide for more details about framework schedulers and executors). While the master determines how many resources are offered to each framework, the frameworks' schedulers select which of the offered resources to use. When a framework accepts offered resources, it passes to Mesos a description of the tasks it wants to run on them. In turn, Mesos launches the tasks on the corresponding agents.

[Source](http://mesos.apache.org/documentation/latest/architecture/)
[Quickstart Source](http://iankent.uk/blog/a-quick-introduction-to-apache-mesos/)