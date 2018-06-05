# M-CORD tests

This directory contains a simple playbook for creating an M-CORD EPC and
verifying that it comes up correctly.  It can be run on any node with Ansible
installed and SSH connectivity to the master node of the openstack-helm
installation.

Invoke the playbook as follows, where "masternode" is the DNS name of the
master node:

```
ansible-playbook -i masternode, mcord-cavium-test-playbook.yml
```

The comma after "masternode" is important; it allows Ansible to run the
playbook on the remote node without having to specify an inventory file.