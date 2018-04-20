# Troubleshooting

Sometimes, components may not come up in a clean state. In this case, following
paragraph may help you to debug, and fix the issues.

Most of the times, debug means do the procedure that the automated process
would do, manually. Here are few manual configuration examples.

Before reading this paragraph, make sure you’ve already covered the general
CORD troubleshooting guide, at in the main [troubleshooting
section](/troubleshooting.md).

## See the status and the IP addresses of your VNFs

You may often need to check the status of your M-CORD VNFs, or access them to
apply some extra configurations or to debug. To check the status or to know the
IP of your VNF, do the following:

* SSH into the head node
* Type following commands:

```shell
source /opt/cord_profile/admin-openrc.sh
nova list --all-tenants
```

## View interface details for a specific VNF

* SSH into the head node
* List your VNF VMs, following the procedure at
  <troubleshooting.md#see-the-status-and-the-ip-addresses-of-your-vnfs>
* Find the ID of the specific instance (i.e.
  `92dff317-732f-4a6a-aa0d-56a225e9efae`)
* To get the interfaces details of the VNF, do

```shell
nova interface-list ID_YOU_FOUND_ABOVE
```

## View an interface name, inside a VNF

In the troubleshooting steps below you’ll be often asked to provide a specific
VNF name. To do that, follow the steps below:

* From the head node, find the IP address of the VNF interface attached to a
  specific network. To do that, refer to the steps reported
  [here](troubleshooting.md#see-the-status-and-the-ip-addresses-of-your-vnfs).
* SSH into the VNF, following the steps
  [here](troubleshooting.md#how-to-log-into-a-vnf-vm).
* Run ifconfig inside the VNF. Look for the interface IP you discovered at the
  steps above. You should see listed on the side the interface name.

## Understand the M-CORD Synchronizers logs

Synchronizers are XOS components responsible to synchronize
the VNFs status with the configuration input by the Operator. More informations
about what synchronizers are and how they work, can be found
[here](/xos/dev/synchronizers.md).

In case of issues, users may need to check the XOS synchronizers logs.
Synchronizers are no more than Docker containers running on the head node.
Users can access their logs simply using standard Docker commands:

* SSH into the head node
* Type the following

```shell
docker logs -f NAME_OF_THE_SYNCHRONIZER
```

> NOTE: to list the containers running on the head node (including the ones
> operating as synchronizers), use the command `docker ps`.

It may happen that some error messages appear in the logs of your M-CORD VNF synchronizers.

Following, is a list of the most common cases.

* **Case 1**: “Exception: defer object `<something>_instance<#>` due to waiting
  on instance” It means a VNF cannot come up correctly.  To check the overall
  instances status, follow the procedure described
  [here](troubleshooting.md#see-the-status-and-the-ip-addresses-of-your-vnfs).
  If your instances are in any status other than `ACTIVE` or `BUILD` there’s an
  issue. This might happen simply because something temporarily failed during
  the provisioning process (so you should try to rebuild your VNFs again,
  following [these
  instructions](troubleshooting.md#configure-build-and-run-the-spgw-c-and-the-spgw-u),
  or because there are more serious issues.

* **Case 2**: “Exception: IP of SSH proxy not available. Synchronization
  deferred” It means that the Ansible playbook wasn’t able to access some
  images, since SSH proxy wasn’t available yet. The SSH proxy usually need some
  time to become available, and the error message automatically disappear when
  this happens, so you shouldn’t worry about it, as long as the message doesn’t
  keep showing up.

* **Case 3**: Any failed message of ansible playbook Finding errors related to
  Ansible is quite common. While it may be possible to fix the issue manually,
  it’s generally desirable to build and deploy again the VNFs. This will run
  the entire Ansible playbook again. See
  [here](troubleshooting.md#configure-build-and-run-the-spgw-c-and-the-spgw-u)
  for more details.

* **Any other issue?** Please report it to us at <cord-dev@opencord.org>. We
  will try to fix it as soon as possible.
