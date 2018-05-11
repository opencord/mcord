# M-CORD Profile

M-CORD 5.0 documentation is not ready yet, we are working on it now !

The M-CORD (Mobile CORD) profile is `Official` as of 4.1. This document
describes 5.0.

## Service Manifest

M-CORD includes service manifests: mcord-cavium

| Service      | Source Code         |
|--------------|---------------|
| epc-service  | https://github.com/opencord/epc-service |
| Fabric       | https://github.com/opencord/fabric |
| HSS_DB       | based on Cassandra, will be provided in hss_db image |
| InternetEmulator | based on VLC, will be provided in internetEmulator image |
| ONOS         | https://github.com/opencord/onos-service |
| OpenStack    | https://github.com/opencord/openstack |
| vENB         | https://github.com/opencord/venb |
| vHSS         | https://github.com/opencord/vHSS |
| vMME         | https://github.com/opencord/vMME |
| vSPGWC       | https://github.com/opencord/vspgwc |
| vSPGWU       | https://github.com/opencord/vspgwu |
| VTN          | https://github.com/opencord/vtn |

## Model Extensions

M-CORD extends CORD's core models with the following model specification
[mcord.xproto](https://github.com/opencord/mcord/blob/cord-5.0/xos/models/mcord.xproto),
which represents the subscriber that anchors a chain of ServiceInstances:

```proto
message MCordSubscriberInstance (ServiceInstance) {
    option verbose_name = "MCORD Subscriber";
    option description = "This model holds the informations of a Mobile
    Subscriber in CORD";

    required string imsi_number = 1 [max_length = 30, content_type = "stripped", blank = False, null = False, db_index = False];
    optional string apn_number = 2 [max_length = 30, content_type = "stripped", blank = True, null = True, db_index = False];
    optional int32 ue_status = 3 [default = "0", choices = "(('0', 'Detached'), ('1', 'Attached'))", blank = True, null = True, db_index = False];
    optional string created_by = 4 [null = True, blank = True, gui_hidden = True];
}
```

## GUI Extensions

M-CORD doesn’t include any GUI extension.
