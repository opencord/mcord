# Developer Guide

The paragraph described general guidelines for developers who want to download
and work on the M-CORD source code, or need to to mock special development
environments.

## Download the M-CORD source code

M-CORD is part of the default CORD code base. To know how you can [download the
cord source code, go here](/getting_the_code.md}.

Each M-CORD service lives in a specific repository. A list of M-CORD services
and links to their repositories is available in the [main page of this
guide](/profiles/mcord/).

> Note: M-CORD source code is available from the 4.1 release (branch) of CORD.

## Developer environments

As for other CORD profiles, M-CORD can also be deployed in environments other
than physical PODs. This creates a more convenient environment for developers,
using less resources and providing a faster development life-cycle.

Two environments are available, depending on your needs:

* **Mock/Local Developer Machine**: a development environment running directly
  on your laptop
* **CORD-in-a-Box**

### Mock/local Machine Development Environment

To understand what a local development environment is, what it can help you
with, and how to build it, [see here](/xos/dev/workflow_mock_single.md).

When it’s time to specify the PODCONFIG file, use mcord-cavium-mock.yml, instead
of the default value (rcord-mock.yml)

### CORD-in-a-Box (CiaB) Development

To understand what CiaB is and what it can help you with, [see
here](/xos/dev/workflow_pod.html).  Note that, in general, CiaB is useful for
validating basic functionality and not for testing performance.

To build M-CORD CiaB, follow the [virtual install steps](/install_virtual.md).

> Note: If you are building on CloudLab, specify the profile `MCORD-in-a-Box`
> rather than `OnePC-Ubuntu14.04.5`.  This will select a machine with enough
> resources to run M-CORD.

When it’s time to specify the PODCONFIG file, use `mcord-cavium-virtual.yml`,
instead of the default value, `rcord-virtual.yml`.

> Warning: At today, given the number of VNFs that M-CORD provides, it requires
> more resources than what other CORD use-cases do. For this reason, in order
> to experiment with M-CORD-in-a-Box you’ll need a bigger physical server than
> the ones required to build other [physical
> PODs](/install_physical.md#bill-of-materials-bom--hardware-requirements).
> Specifically, you'll need to have processors with at least a total of 24
> physical cores.

More detailed instructions on how to develop and deploy using CiaB can be found
in the general [CORD troubleshooting guide](/troubleshooting.md).

