# M-CORD Profile

The M-CORD (Mobile CORD) profile is `Official` as of 4.1.

## Service Manifest

M-CORD includes service manifests:

### [mcord-ng40](https://github.com/opencord/platform-install/blob/cord-4.1/profile_manifests/mcord-ng40.yml)

| Service      | Source Code         |
|--------------|---------------|
| epc-service  | https://github.com/opencord/epc-service |
| Fabric       | https://github.com/opencord/fabric |
| ONOS         | https://github.com/opencord/onos-service |
| OpenStack    | https://github.com/opencord/openstack |
| vENB         | https://github.com/opencord/venb |
| vSPGWC       | https://github.com/opencord/vspgwc |
| vSPGWU       | https://github.com/opencord/vspgwu |
| VTN          | https://github.com/opencord/vtn |

## Model Extensions

M-CORD extends CORD's core models with the following model specification
[mcord.xproto](https://github.com/opencord/mcord/blob/master/xos/models/mcord.xproto),
which represents the subscriber that anchors a chain of ServiceInstances:

```proto
message MCordSubscriberInstance (ServiceInstance) {
    option verbose_name = "MCORD Subscriber";
    option description = "This model holds the informations of a Mobile Subscriber in CORD";

    required string imsi_number = 1 [max_length = 30, content_type = "stripped", blank = False, null = False, db_index = False];
    optional string apn_number = 2 [max_length = 30, content_type = "stripped", blank = True, null = True, db_index = False];
    optional int32 ue_status = 3 [max_length = 30, choices = "(('0', 'Detached'), ('1', 'Attached'))", blank = True, null = True, db_index = False];
}
```

## GUI Extensions

M-CORD doesn’t include any GUI extension.
