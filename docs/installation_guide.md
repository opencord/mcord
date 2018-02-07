# Installation Guide

The following describes how to install and configure an M-CORD physical POD.

## Hardware Requirements

M-CORD by default uses the NG40 software emulator including the RAN, an MME,
and a traffic generator. For this reason, it does not require any additional
hardware, other than the ones listed for a “traditional” [CORD
POD](/install_physical.md#bill-of-materials-bom--hardware-requirements).

> Warning: The NG40 vTester requires a compute node with Intel XEON CPU with
> [Westmere microarchitecture or
> better](https://en.wikipedia.org/wiki/List_of_Intel_CPU_microarchitectures).

## NG40 vTester M-CORD License

As mentioned above, ng4T provides a limited version of its NG40 software, which
requires a free license in order to work. The specific NG40 installation steps
described in the next paragraph assume the Operator has obtained the license
and saved it into  a specific location on the development server.

In order to download a free M-CORD trial license, go to the [NG40 M-CORD
website](https://mcord.ng40.com/) and register. You will be asked for your
company name and your company email. After successful authentication of your
email and acknowledgment of the free M-CORD NG40 License, you can download the
license file called `ng40-license`.

## M-CORD POD Installation

To install the local node you should follow the steps described in the main
[physical POD installation](/install_physical.md).

As soon as you have the CORD repository on your development machine, transfer
the downloaded M-CORD NG40 license file, to:

`$CORD_ROOT/orchestration/xos_services/venb/xos/synchronizer/files/ng40-license`

When it’s time to write your pod configuration, use the [physical-example.yml
file as a
template](https://github.com/opencord/cord/blob/master/podconfig/physical-example.yml).
Either modify it or make a copy of it in the same directory. Fill in the
configuration with your own head node data.

As cord_scenario, use `cord`.

As cord_profile, use `mcord-ng40`.

> Warning: After you’ve finished the basic installation, configure the fabric
> and your computes, as described [here](/appendix_basic_config.md).

## Create an EPC instance

The EPC is the only component that needs to be manually configured, after the
fabric gets properly setup. An EPC instance can be created in two ways.

### Create an EPC instance using the XOS-UI

Open in your browser the XOS UI : `http://<your head node>/xos`

* Log in
* From the left panel, select `vEPC`
* Click on `Virtual Evolved Packet Core ServiceInstances`
* On the top right, press `Add`
* Set `blueprint` to `MCORD 4.1`
* Set `Owner id` to `vepc`
* Set `Site id` to `MySite`
* Press `Save`

### Create an EPC instance using the XOS northbound API

```shell
curl -u xosadmin@opencord.org:<password> -X POST http://<ip address of pod>/xosapi/v1/vepc/vepcserviceinstances -H "Content-Type: application/json" -d '{"blueprint":"build", "site_id": 1}'
```

## Verify a Successful Installation

To verify if the installation was successful, ssh into the head node and follow
these steps:

Verify that the service synchronizers are running.  Use the `docker ps` command
on head node, you should be able to see the following M-CORD synchronizers:

* mcordng40_venb-synchronizer_1
* mcordng40_vspgwc-synchronizer_1
* mcordng40_vspgwu-synchronizer_1
* mcordng40_vepc-synchronizer_1

Check that the ServiceInstances are running on the head node. Run these
commands on the head node:

```shell
source /opt/cord_profile/admin-openrc.sh
nova list --all-tenants
```

You should see three VMs like this:

```shell
+--------------------------------------+-----------------+--------+------------+-------------+---------------------------------------------------------------------------------------------+
| ID                                   | Name            | Status | Task State | Power State | Networks                                                                                    |
+--------------------------------------+-----------------+--------+------------+-------------+---------------------------------------------------------------------------------------------+
| 9d5d1d45-2ad8-48d5-84c5-b1dd02458f81 | mysite_venb-3   | ACTIVE | -          | Running     | s1u_network=111.0.0.2; sgi_network=115.0.0.2; management=172.27.0.4; s11_network=112.0.0.3  |
| 797ec8e8-d456-405f-a656-194f5748902a | mysite_vspgwc-2 | ACTIVE | -          | Running     | management=172.27.0.2; spgw_network=117.0.0.2; s11_network=112.0.0.2                        |
| 050393a3-ec25-4548-b02a-2d7b02b16943 | mysite_vspgwu-1 | ACTIVE | -          | Running     | s1u_network=111.0.0.3; sgi_network=115.0.0.3; management=172.27.0.3; spgw_network=117.0.0.3 |
+--------------------------------------+-----------------+--------+------------+-------------+---------------------------------------------------------------------------------------------+
```

> Note: It may take a few minutes to provision the instances. If you don’t see
> them immediately, try again after some time.

Check that the service synchronizers have run successfully:

* Log into the XOS GUI on the head node
* In left panel, click on each item listed below and verify that there is a
  check mark sign under “backend status”
    * Vspgwc, then Virtual Serving PDN Gateway -- Control Plane Service
      Instances
    * Vspgwu, then Virtual Serving Gateway User Plane Service Instances
    * Venb, then Virtual eNodeB Service Instances

> NOTE: It may take a few minutes to run the synchronizers.  If you don’t see a
> check mark immediately, try again after some time.

## Using the NG40 vTester Software

You’re now ready to generate some traffic and test M-CORD. To proceed, do the
following.

* SSH into the NG40 VNF VM with username and password ng40/ng40. To understand
  how to access your VNFs look
  [here](troubleshooting.md#how-to-log-into-a-vnf-vm).
* Run `~/verify_quick.sh`

You should see the following output:

```shell
**** Load Profile Settings ****
$pps = 1000
$bps = 500000000
……
Signaling Table
           AttUE     ActCTXT   BrReq     BrAct     RelRq     RelAc     ActS1
ng40_ran_1 1         1         1         1         0         0         1
User Plane Downlink Table
           AS_PktTx      AS_EthTx      S1uEthRx      S1uPktRx
ng40_ran_1 132           132           144           133
User Plane Uplink Table
           S1uPktTx      S1uEthTx      AS_EthRx      AS_PktRx
ng40_ran_1 49            50            48            48
Watchtime: 9 Timeout: 1800
```

Both the downlink and uplink should show packets counters increasing. The
downlink shows packets flowing from the AS (Application Server) to the UE. The
uplink shows packets going from the UE to the AS.

The result for all commands should look like:

```shell
Verdict(tc_attach_www) = VERDICT_PASS
**** Packet Loss ****
DL Loss= AS_PktTx-S1uPktRx=     0(pkts); 0.00(%)
UL Loss= S1uPktTx-AS_PktRx=     0(pkts); 0.00(%)
```

The verdict is configured to check the control plane only.

For the user plane verification you see the absolute number and percentage of
lost packets.

There are multiple test commands available (You can get the parameter
description with the flags -h or -?):

* **verify_attach.sh**

```shell
Usage: ./verify_attach.sh [<UEs> [<rate>]]
       UEs: Number of UEs 1..10, default 1
       rate: Attach rate 1..10, default 1
```

Send only attach and detach.

Used to verify basic control plane functionality.

* **verify_attach_data.sh**

```shell
Usage: ./verify_attach_data.sh [<UEs> [<rate>]]
       UEs: Number of UEs 1..10, default 1
       rate: Attach rate 1..10, default 1
```

Send attach, detach and a few user plane packets.

Used to verify basic user plane functionality.

Downlink traffic will be sent without waiting for uplink traffic to arrive at
the Application Server.

* **verify_quick.sh**

```shell
Usage: ./verify_quick.sh [<UEs> [<rate> [<pps>]]]
       UEs: Number of UEs 1..10, default 2
       rate: Attach rate 1..10, default 1
       pps: Packets per Second 1000..60000, default 1000
```

Send attach, detach and 1000 pps user plane. Userplane ramp up and down ~20
seconds and total userplane transfer time ~70 seconds.

500.000.000 bps (maximum bit rate to calculate packet size from pps setting,
MTU 1450).

Used for control plane and userplane verification with low load for a short
time.

Downlink traffic will only be send when uplink traffic arrives at the
Application Server.

* **verify_short.sh**

```shell
Usage: ./verify_short.sh [<UEs> [<rate> [<pps>]]]
       UEs: Number of UEs 1..10, default 10
       rate: Attach rate 1..10, default 5
       pps: Packets per Second 1000..60000, default 60000
```

Send attach, detach and 60000 pps user plane. Userplane ramp up and down ~20
seconds and total userplane transfer time ~70 seconds.

500.000.000 bps (maximum bit rate to calculate packet size from pps setting,
MTU 1450). Used for control plane and userplane verification with medium load
for a short time. Downlink traffic will only be send when uplink traffic
  arrives at the Application Server.

* **verify_long.sh**

```shell
Usage: ./verify_long.sh [<UEs> [<rate> [<pps>]]]
       UEs: Number of UEs 1..10, default 10
       rate: Attach rate 1..10, default 5
       pps: Packets per Second 1000..60000, default 60000
```

Send attach, detach and 60000 pps user plane. Userplane ramp up and down ~200
seconds and total userplane transfer time ~700 seconds.

500.000.000 bps (maximum bit rate to calculate packet size from pps setting,
MTU 1450).

Used for control plane and userplane verification with medium load for a longer
time.

Downlink traffic will only be send when uplink traffic arrives at the
Application Server.

### Request / Update the NG40 vTester Software License

If you forgot to request an NG40 license at the beginning of the installation,
or if you would like to extend it, you can input your updated license once the
NG40 VM is up, following the steps below:

SSH into the NG40 VNF VM with username and password ng40/ng40. To understand
how to access your VNFs, look
[here](/troubleshooting.md#how-to-log-into-a-vnf-vm).

Add the license file with named `ng40-license` to the folder: `~/install/`
Run the command `~/install/ng40init`.

