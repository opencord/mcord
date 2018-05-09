# Installation Guide

The following describes how to install and configure an M-CORD physical POD.

## Hardware Requirements

Beside  the ones listed for a “traditional” [CORD
POD](/install_physical.md#bill-of-materials-bom--hardware-requirements).
M-CORD 5.0 by default uses UE and standalone eNodeB hardware.

> Warning: The NGIC requires a compute node with Intel XEON CPU with
> [Haswell microarchitecture or
> better](https://en.wikipedia.org/wiki/List_of_Intel_CPU_microarchitectures).
> Note that 4.1 recommends at least `Westmere` microarchitecture but 5.0
> highly recommend to use at least `Haswell` microarchitecture.

## M-CORD POD Installation

To install the local node you should follow the steps described in the main
[physical POD installation](/install_physical.md).

When it’s time to write your pod configuration, use the [physical-example.yml
file as a
template](https://github.com/opencord/cord/blob/master/podconfig/physical-example.yml).
Either modify it or make a copy of it in the same directory. Fill in the
configuration with your own head node data.

As cord_scenario, use `cord`.

As cord_profile, use `mcord-cavium`.

> Warning: After you’ve finished the basic installation, configure the fabric
> and your computes, as described [here](/appendix_basic_config.md).

## Create an EPC instance

The EPC is the only component that needs to be manually configured, after the
fabric gets properly setup. An EPC instance can be created inside XOS-UI.

### Create an EPC instance using the XOS-UI

Open in your browser the XOS UI : `http://<your head node>/xos`

* Log in
* From the left panel, select `vEPC`
* Click on `Virtual Evolved Packet Core ServiceInstances`
* On the top right, press `Add`
* Set `blueprint` to `MCORD 5.0`
* ......
* Press `Save`

## Verify a Successful Installation

To verify if the installation was successful, ssh into the head node and follow
these steps:

Verify that the service synchronizers are running.  Use the `docker ps` command
on head node, you should be able to see the following M-CORD synchronizers:

* mcordcavium_vspgwc-synchronizer_1
* mcordcavium_vspgwu-synchronizer_1
* mcordcavium_hssdb-synchronizer_1
* mcordcavium_vhss-synchronizer_1
* mcordcavium_vmme-synchronizer_1
* mcordcavium_internetemulator-synchronizer_1
* mcordcavium_vepc-synchronizer_1

Check that the ServiceInstances are running on the head node. Run these
commands on the head node:

```shell
source /opt/cord_profile/admin-openrc.sh
nova list --all-tenants
```

You should see three VMs like this:

```shell
+--------------------------------------+---------------------------+---------+------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ID                                   | Name                      | Status  | Task State | Power State | Networks                                                                                                                            |
+--------------------------------------+---------------------------+---------+------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------+
| c9dc354f-e1b4-4900-9ccb-3d77dd4bdf45 | mysite_hssdb-12           | ACTIVE  | -          | Running     | management=172.27.0.9; db_network=121.0.0.2                                                                                         |
| 82200b77-37d6-4fea-b98e-89f74646a90d | mysite_internetemulator-7 | ACTIVE  | -          | Running     | sgi_network=115.0.0.8; management=172.27.0.8                                                                                        |
| 6b92f216-89b2-4e7e-8b49-277f1e92e448 | mysite_vhss-13            | ACTIVE  | -          | Running     | s6a_network=120.0.0.4; management=172.27.0.16; db_network=121.0.0.5                                                                 |
| 1710892c-d5c5-4d65-9d7e-5b1aae435831 | mysite_vmme-15            | ACTIVE  | -          | Running     | s6a_network=120.0.0.5; flat_network_s1mme=118.0.0.3; management=172.27.0.17; s11_network=112.0.0.5; flat_network_s1mme_p4=122.0.0.2 |
| 2e2c21d9-1e66-4425-b0ef-da90a204b7d5 | mysite_vspgwc-8           | ACTIVE  | -          | Running     | management=172.27.0.10; spgw_network=117.0.0.2; s11_network=112.0.0.2                                                               |
| 70ebeb85-13c9-474d-97d0-ec40ad621281 | mysite_vspgwu-10          | ACTIVE  | -          | Running     | management=172.27.0.12; sgi_network=115.0.0.9; spgw_network=117.0.0.3; flat_network_s1u=119.0.0.2                                   |
+--------------------------------------+---------------------------+---------+------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------+

```

> Note: It may take a few minutes to provision the instances. If you don’t see
> them immediately, try again after some time.

Check that the service synchronizers have run successfully:

* Log into the XOS GUI on the head node
* In left panel, click on each item listed below and verify that there is a
  check mark sign under “backend status”
    * Vspgwc, the Virtual Serving PDN Gateway -- Control Plane Service Instances
    * Vspgwu, the Virtual Serving Gateway User Plane Service Instances
    * Hssdb, the HSS Database ServiceInstances
    * Vhss, the Virtual Home Subscriber Server Tenants
    * Vmme, the Virtual Mobility Management Entity Service Instances
    * Internetemulator, the Internet Emulator Service Instances

> NOTE: It may take a few minutes to run the synchronizers.  If you don’t see a
> check mark immediately, try again after some time.
