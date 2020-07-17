MAAS is an open-source tool that lets you build a data centre from bare-metal servers. You can discover, commission, deploy, and dynamically reconfigure a large network of individual units.  MAAS converts your hardware investment into a cohesive, flexible, distributed data centre, with a minimum of time and effort.

#### Quick questions you might have:

* [What is MAAS?](#heading--what-is-maas)
* [What does MAAS offer me?](/t/about-maas/840#heading--what-maas-offers)
* [Can MAAS colocate key components to conserve my resources?](/t/about-maas/840#heading--colocation-of-key-components)
* [How does MAAS work?](/t/about-maas/840#heading--how-maas-works)

<h2 id="heading--what-is-maas">What is MAAS?</h2>

MAAS expands to "Metal As A Service". It converts bare-metal servers into cloud instances of virtual machines. There is no need to manage individual units. You can quickly provision or destroy machines, as if they were instances hosted in a public cloud like Amazon AWS, Google GCE, or Microsoft Azure.

MAAS can act as a standalone PXE/preseed service or integrate with other technologies. It works exceptionally well with [Juju](https://jaas.ai/docs/maas-cloud), the service and model management tool. MAAS manages the machines and Juju manages the services running on those machines -- a perfect arrangement.  Virtual machines (VMs) can even act as MAAS machines if they boot from the network via PXE.

![deploying|690x385](upload://tUorx2JPUx7lJyuYK9fzvpbAekv.jpeg)  

<details><summary>Tell me about PXE booting</summary>

PXE stands for "Preboot Execution Environment," usually pronounced "pixie."  The term refers to a way of booting an OS image (or other software assembly) downloaded to a client via a NIC.  The NIC must be PXE-capable for this to work.  Many NICs can be configured to support PXE boot with a software switch.

</details>

<h2 id="heading--what-maas-offers">What MAAS offers</h2>

MAAS can manage a large number of physical machines by merging them into user-defined resource pools. MAAS automatically provisions participating machines and makes them available for use. You can return unused machines to the assigned pool at any time. 

MAAS integrates all the tools you need into a smooth system-management experience. It includes:

- web UI (optimised for mobile devices)
- Ubuntu, CentOS, Windows, and RHEL installation support
- open-source IP address management (IPAM)
- full API/CLI support
- high availability (optional)
- IPv6 support
- inventory of components
- DHCP and DNS for other devices on the network
- DHCP relay integration
- VLAN and fabric support
- NTP for the entire infrastructure
- hardware testing
- composable hardware support

These tools can be controlled from a responsive [web UI](/t/web-ui/782) or a [CLI](/t/maas-cli/802) driven by a REST API.  You can easily (re)configure and scale your data centre with MAAS.

![mixed-states|690x438](upload://5cwZFoAljFf5nKDD0bDf5OJ55t.jpeg)  

MAAS works with any system configuration tools. Both the [Chef](https://www.chef.io/chef) and [Juju](https://jaas.ai/) teams recommend MAAS as a physical provisioning system.

[note]
Please note that Windows and RHEL images require [Ubuntu Advantage](https://www.ubuntu.com/support) to work correctly with MAAS.
[/note]

<h3 id="heading--colocation-of-key-components">Colocation of key components</h3>

MAAS relies on two key components: the *region controller* and the *rack controller*. The region controller handles operator requests; the rack controller provides high-bandwidth services to multiple racks. In essence, rack controllers manage racks, while the region controller manages the data centre.  See [Concepts and terms](/t/concepts-and-terms/785#heading--controllers) for a deeper understanding of these components.

We generally recommended installing both controllers on the same system.  The default MAAS install delivers this colocated configuration automatically. This all-in-one solution also provides [DHCP](/t/dhcp/759). 

In special cases, such as [high availability or load balancing](/t/high-availability/804), you will want to install multiple region and rack controllers.  You should also review your existing network design to determine whether [MAAS-managed DHCP](/t/dhcp/759) will cause problems.

![intro-arch-overview](https://discourse.maas.io/uploads/default/original/1X/5fc8edb2243aa4d4ac6ba7981a7b917fec27c480.png)

<h2 id="heading--how-maas-works">How MAAS works</h2>

When you [add a new machine](/t/add-machines/821#heading--add-a-node-manually) to MAAS, or elect to add a machine that MAAS has [enlisted](/t/add-machines/821#heading--enlistment), MAAS [commissions](/t/commission-machines/822) it for service and adds it to the pool.  At that point, the machine is ready for use. MAAS keeps things simple, marking machines as "New," "Commissioning," "Ready," and so on.

<details><summary>Tell me, quickly, about enlistment and commissioning.</summary>

There are two ways to add a machine to MAAS.  Assuming it's on the network and capable of PXE-booting, you can add it explicitly -- or MAAS can simply discover it when you turn it on.

Enlistment just means that MAAS discovers a machine when you turn it on, and presents it to the MAAS administrator, so that they can choose whether or not to commission it.  Machines that have only been enlisted will show up in the machine list as "New."

Commissioning means that MAAS has successfully booted the machine, scanned and recorded its resources, and prepared it for eventual deployment.  Machines that you explicitly add are automatically commissioned.  MAAS marks a successfully-commissioned machine as "Ready" in the machine list.

</details>

![commissioning|606x400](upload://dK1s4OaSl7oPzXDpE9Cgcxrqi40.jpeg) 

MAAS controls machines through IPMI (or another BMC). It can also manage machines through a converged chassis controller, such as Cisco UCS.  You can choose how you want to control power on your machines based on what is available.  MAAS overwrites the machine's disk space with your chosen, pre-cached OS images.

[note type="negative" status="Warning"]
*The above comment about disk space bears repeating: MAAS will overwrite the disk space of all machines it enlists. All pool machines are under the control of MAAS; you should provision them using other methods.*
[/note]

MAAS users allocate ("acquire") machines for use when needed. The web UI also allows you to acquire machines manually, such as when you are reserving specific hardware for certain users. You can remotely access and customise the installed operating system via SSH.

![acquire|690x363](upload://ipfwOGPPFapA83rrvdJe12zgaZd.jpeg) 

When acquiring machines from the API/CLI, you can specify requirements ("constraints"). Common constraints are memory, CPU cores, connected networks, and assigned physical zone.

An acquired MAAS machine is more flexible than a virtual instance in a cloud. You have complete control, including hardware drivers and root access. If you want to upgrade the BIOS, for example, you can allocate a machine to yourself and complete the upgrade.  Once you have completed the upgrade, you can send the machine back to the pool.

Note that [Juju](https://jaas.ai/docs/maas-cloud) is designed to work with MAAS. MAAS becomes a backend Juju resource pool with all functionality fully available. For instance, if Juju removes a machine, then MAAS will release that machine to the pool.  With Juju, MAAS can become an integral part of your data centre strategy and operations.
<!-- zork-out -->
