MAAS is **Metal As A Service**, a service that lets you treat physical servers like virtual machines -- instances -- in the cloud.  No need to manage servers individually: MAAS turns your bare metal into an elastic, cloud-like resource.

#### Quick questions you might have:

* [What is MAAS -- and what does it really do for me?](/t/what-is-maas/840)
* [Can you show me an example datacentre using MAAS?](/t/give-me-an-example-of-maas/1314)
* [How does MAAS work, in detail?](/t/what-is-maas/840#heading--how-maas-works)
* [What concepts might I need to understand before starting?](/t/concepts-and-terms/785)
* [Can I just install it and try it for myself?](/t/explore-maas/787)

![splash-screen|690x406](https://discourse.maas.io/uploads/default/original/1X/18456dbd3fbfec14eddd044816fd0719692282da.jpeg)

*Part of the machine list from [Metaphorical General Hospital](/t/give-me-an-example-of-maas/1314), our example datacentre.*

---

<h2 id="heading--whats-new">New version of MAAS</h2>

- [What's new in 2.8 ›](https://discourse.maas.io/t/whats-new-in-maas-2-8/1655)

---

<h2 id="heading--getting-support">Getting support</h2>

- [Professional support](https://maas.io/contact-us)
- [Ask a question](http://askubuntu.com/questions/tagged/maas)
- [IRC](http://webchat.freenode.net/?channels=maas)
- [MAAS 2.5 (and earlier) documentation](https://old-docs.maas.io/2.5/en/)

---

<h2 id="heading--contribute">Contribute</h2>

- [Guide to contributing](/t/writing-guide/747)
- [Push some code](https://launchpad.net/maas)
- [File an issue](https://bugs.launchpad.net/maas/+filebug)

## Navigation

### [Introduction](/t/maas-documentation/25)

- [About MAAS](/t/what-is-maas/840)
- ["Give me an example"](/t/give-me-an-example-of-maas/1314)
- [Explore MAAS](/t/explore-maas/787)
- [What's new in 2.8](https://discourse.maas.io/t/whats-new-in-maas-2-8/1655)
- [Quick start](https://maas.io/install)

### Installing MAAS

- [Requirements](/t/what-is-maas/789)
- [Installation](https://maas.io/docs/install-from-a-snap)
- [Configuration journey](https://maas.io/docs/configuration-journey)
- [Setup checklist](/t/installation-and-configuration-checklist/750)

### [Controllers](/t/introduction-to-controllers/786)

- [Communication](/t/maas-communication/783)
- [Rack controllers](/t/rack-controller/771)
- [Region controllers](/t/region-controller/772)
- [High availability](/t/high-availability/804)

### [Machines](/t/node-overview/829)

- [Add machines](/t/add-nodes/821)
- [Power management](/t/bmc-power-types/830)
- [Commission machines](/t/commission-nodes/822)
- Testing
  - [Hardware testing](/t/hardware-testing/826)
  - [Network testing](/t/network-testing/1267)
  - [Commissioning and hardware testing scripts](/t/commissioning-and-hardware-testing-scripts/833)
- [Deploy machines](/t/deploy-nodes/825)
- [Tags](/t/tags/834)
- [Custom machine setup](/t/custom-node-setup-preseed/824)
- [Kernel boot options](/t/kernel-boot-options/827)
- [Resource pools](/t/resource-pools/831)
- [Storage](/t/storage/775)
- [VMware VMFS datastores](/t/vmware-vmfs-datastores/780)
- [Ubuntu kernels](/t/ubuntu-kernels/828)

### [Images](/t/images/754)

- [Select and import images](/t/select-and-import-images/751)
- [Local image mirror](/t/local-image-mirror/752)
- [VMWare images](/t/vmware-images/753)

### [Networking](/t/networking/768)

- [Subnet management](/t/subnet-management/766)
- [DHCP](/t/dhcp/759)
- [IP ranges](/t/ip-ranges/760)
- [Proxy](/t/proxy/763)
- [NTP](/t/ntp/762)
- [Network discovery](/t/network-discovery/758)
- [IPv6](/t/ipv6/761)
- [SSL](/t/ssl/764)
- [STP](/t/stp/765)
- [Availability zones (AZs)](/t/availability-zones/820)

### [VM hosting](/t/introduction-to-vm-hosting/1524)

- [VM host networking](/t/vm-host-networking/1526)
- [Add a VM host](https://discourse.maas.io/t/adding-a-vm-host/1549)
- [VM host storage pools](/t/vm-host-storage-pools/1525)
- [Creating and deleting VMs](/t/creating-and-deleting-new-vms/806)

### Operations

- [Prometheus metrics](/t/prometheus-metrics/813)
- [Backup](/t/backup/792)
- [MAAS security](/t/hardening-your-maas-installation/1381)
- [Logging](/t/maas-logging/1468)
  - [Commissioning logs](/t/commissioning-logs/1478)
- [User accounts](/t/user-accounts/790)
- [Interactive search](/t/interactive-search/819)

### [Concepts & terms](/t/concepts-and-terms/785)

- [Brief network tutorial](/t/concepts-and-terms/785#heading--network-tutorial)

### [CLI](/t/maas-cli/802)

- [Common tasks](/t/common-cli-tasks/794)
- [Audit event logs](/t/audit-event-logs/791)
- [Kernel management](/t/cli-kernel-management/799)
- [Image management](/t/cli-image-management/797)
- [Interface management](/t/cli-interface-management/798)
- [Tag management](/t/cli-tag-management/801)
- [Resource pool management](/t/cli-resource-pool-management/800)
- [DHCP snippet management](/t/cli-dhcp-snippet-management/796)
- [Commissioning and hardware testing scripts](/t/cli-commissioning-and-hardware-testing-scripts/832)
- [Advanced tasks](/t/advanced-cli-tasks/793)
- [Composable hardware](/t/cli-composable-machines-management/795)
- [API client](/t/api-client/810)

### [API documentation](https://maas.io/docs/api)

- [API authentication](/t/api-authentication/742)

### [Troubleshoot](/t/troubleshooting/837)

- [Getting help](/t/getting-help/838)
- [Tips, tricks, and traps](/t/tips-tricks-and-traps/1506)
- [Non-snap MAAS installs](/t/non-snap-maas-installs/1308)
- [MAAS 2.5 (and earlier) documentation](https://old-docs.maas.io/2.5/en/)
- [Upgrading MAAS](/t/upgrading-maas/779)
  - [Upgrade from 2.3 to 2.4](/t/upgrade-2-3-to-2-4-from-ubuntu-16-04/777)
  - [Upgrade from 1.9 to 2.x](/t/upgrade-from-1-9-to-2-x/778)

### [Release notes](https://discourse.maas.io/t/whats-new-in-maas-2-8/1655)

### [Help improve these docs](/t/writing-guide/747)

### [Contact us](/t/contact-us/743)

## URLs

[details=Mapping table]
| TOPIC | PATH |
| -- | -- |
| https://discourse.maas.io/t/adding-a-vm-host/1549 | /docs/add-a-vm-host |
| https://discourse.maas.io/t/vm-host-storage-pools/1525 | /docs/vm-host-storage-pools |
| https://discourse.maas.io/t/vm-host-networking/1526 | /docs/vm-host-networking |
| https://discourse.maas.io/t/give-me-an-example-of-maas/1314 | /docs/maas-example-config |
| https://discourse.maas.io/t/non-snap-maas-installs/1308 | /docs/non-snap-maas-installs |
| https://discourse.maas.io/t/concepts-and-terms/785#heading--network-tutorial | /docs/network-tutorial |
| https://discourse.maas.io/t/maas-documentation/25/ | /docs |
| https://discourse.maas.io/t/api-authentication/742/ | /docs/api-authentication |
| https://discourse.maas.io/t/contact-us/743/ | /docs/contact-us |
| https://discourse.maas.io/t/tips-tricks-and-traps/1506 | /docs/tips-tricks-and-traps |
| https://discourse.maas.io/t/writing-guide/747/ | /docs/writing-guide |
| https://discourse.maas.io/t/block-devices/749/ | /docs/block-devices |
| https://discourse.maas.io/t/installation-and-configuration-checklist/750/ | /docs/installation-and-configuration-checklist |
| https://discourse.maas.io/t/select-and-import-images/751/ | /docs/select-and-import-images |
| https://discourse.maas.io/t/local-image-mirror/752/ | /docs/local-image-mirror |
| https://discourse.maas.io/t/vmware-images/753/ | /docs/vmware-images |
| https://discourse.maas.io/t/images/754/ | /docs/images |
| https://discourse.maas.io/t/installation/755/ | /docs/install-from-a-snap  |
| https://discourse.maas.io/t/install-from-iso/756/ | /docs/install-from-iso |
| https://discourse.maas.io/t/install-with-lxd/757/ | /docs/install-with-lxd |
| https://discourse.maas.io/t/network-discovery/758/ | /docs/network-discovery |
| https://discourse.maas.io/t/dhcp/759/ | /docs/dhcp |
| https://discourse.maas.io/t/ip-ranges/760/ | /docs/ip-ranges |
| https://discourse.maas.io/t/ipv6/761/ | /docs/ipv6 |
| https://discourse.maas.io/t/ntp/762/ | /docs/ntp |
| https://discourse.maas.io/t/proxy/763/ | /docs/proxy |
| https://discourse.maas.io/t/ssl/764/ | /docs/ssl |
| https://discourse.maas.io/t/stp/765/ | /docs/stp |
| https://discourse.maas.io/t/subnet-management/766/ | /docs/subnet-management |
| https://discourse.maas.io/t/configure-networking/767/ | /docs/networking |
| https://discourse.maas.io/t/networking/768/ | /docs/networking |
| https://discourse.maas.io/t/install-from-packages/769/ | /docs/install-from-packages |
| https://discourse.maas.io/t/partitions/770/ | /docs/partitions |
| https://discourse.maas.io/t/rack-controller/771/ | /docs/rack-controller |
| https://discourse.maas.io/t/region-controller/772/ | /docs/region-controller |
| https://discourse.maas.io/t/install-from-a-snap/773/ | /docs/install-from-a-snap |
| https://discourse.maas.io/t/disk-erasure/774/ | /docs/disk-erasure |
| https://discourse.maas.io/t/storage/775/ | /docs/storage |
| https://discourse.maas.io/t/maas-logging/1468 | /docs/logging |
| https://discourse.maas.io/t/commissioning-logs/1478 | /docs/commissioning-logs |
| https://discourse.maas.io/t/upgrade-2-3-to-2-4-from-ubuntu-16-04/777/ | /docs/upgrade-2-3-to-2-4-from-ubuntu-16-04 |
| https://discourse.maas.io/t/upgrade-from-1-9-to-2-x/778/ | /docs/upgrade-from-1-9-to-2-x |
| https://discourse.maas.io/t/upgrading-maas/779/ | /docs/upgrading-maas |
| https://discourse.maas.io/t/vmware-vmfs-datastores/780/ | /docs/vmware-vmfs-datastores |
| https://discourse.maas.io/t/configuration-journey/781/ | /docs/configuration-journey |
| https://discourse.maas.io/t/web-ui/782/ | /docs/web-ui |
| https://discourse.maas.io/t/maas-communcation/783/ | /docs/maas-communication |
| https://discourse.maas.io/t/zone-examples/784/ | /docs/zone-examples |
| https://discourse.maas.io/t/concepts-and-terms/785/ | /docs/concepts-and-terms |
| https://discourse.maas.io/t/introduction-to-controllers/786/ | /docs/introduction-to-controllers |
| https://discourse.maas.io/t/explore-maas/787/ | /docs/explore-maas |
| https://discourse.maas.io/t/whats-new-in-2-6/788/ | /docs/whats-new-in-2-6 |
| https://discourse.maas.io/t/maas-requirements/789/ | /docs/maas-requirements |
| https://discourse.maas.io/t/what-is-maas/840/ | /docs/what-is-maas |
| https://discourse.maas.io/t/user-accounts/790/ | /docs/user-accounts |
| https://discourse.maas.io/t/audit-event-logs/791/ | /docs/audit-event-logs |
| https://discourse.maas.io/t/backup/792/ | /docs/backup |
| https://discourse.maas.io/t/advanced-cli-tasks/793/ | /docs/advanced-cli-tasks |
| https://discourse.maas.io/t/common-cli-tasks/794/ | /docs/common-cli-tasks |
| https://discourse.maas.io/t/cli-composable-machines-management/795/ | /docs/composable-hardware |
| https://discourse.maas.io/t/cli-dhcp-snippet-management/796/ | /docs/cli-dhcp-snippet-management |
| https://discourse.maas.io/t/cli-image-management/797/ | /docs/cli-image-management |
| https://discourse.maas.io/t/cli-interface-management/798/ | /docs/cli-interface-management |
| https://discourse.maas.io/t/cli-kernel-management/799/ | /docs/cli-kernel-management |
| https://discourse.maas.io/t/cli-resource-pool-management/800/ | /docs/cli-resource-pool-management |
| https://discourse.maas.io/t/cli-tag-management/801/ | /docs/cli-tag-management |
| https://discourse.maas.io/t/maas-cli/802/ | /docs/maas-cli |
| https://discourse.maas.io/t/postgresql-ha-hot-standby/803/ | /docs/postgresql-ha-hot-standby |
| https://discourse.maas.io/t/high-availability/804/ | /docs/high-availability |
| https://discourse.maas.io/t/creating-and-deleting-new-vms/806/ | /docs/creating-and-deleting-new-vms |
| https://discourse.maas.io/t/introduction-to-vm-hosting/1524 | /docs/intro-to-vm-hosting |
| https://discourse.maas.io/t/api-client/810/ | /docs/api-client |
| https://discourse.maas.io/t/hardening-your-maas-installation/1381 | /docs/security |
| https://discourse.maas.io/t/prometheus-metrics/813/ | /docs/prometheus-metrics |
| https://discourse.maas.io/t/package-repositories/814/ | /docs/package-repositories |
| https://discourse.maas.io/t/add-an-rsd-host/815/ | /docs/add-an-rsd-host |
| https://discourse.maas.io/t/creating-and-deleting-machines/816/ | /docs/creating-and-deleting-machines |
| https://discourse.maas.io/t/intel-rack-scale-design-rsd-introduction/817/ | /docs/intel-rack-scale-design-rsd-introduction |
| https://discourse.maas.io/t/rsd-storage/818/ | /docs/rsd-storage |
| https://discourse.maas.io/t/interactive-search/819/ | /docs/interactive-search |
| https://discourse.maas.io/t/availability-zones/820/ | /docs/availability-zones |
| https://discourse.maas.io/t/documentation-index/839/ | /docs/documentation-index |
| https://discourse.maas.io/t/add-nodes/821/ | /docs/add-nodes |
| https://discourse.maas.io/t/commission-nodes/822/ | /docs/commission-nodes |
| https://discourse.maas.io/t/custom-node-setup-preseed/824/ | /docs/custom-node-setup-preseed |
| https://discourse.maas.io/t/deploy-nodes/825/ | /docs/deploy-nodes |
| https://discourse.maas.io/t/hardware-testing/826/ | /docs/hardware-testing |
| https://discourse.maas.io/t/kernel-boot-options/827/ | /docs/kernel-boot-options |
| https://discourse.maas.io/t/ubuntu-kernels/828/ | /docs/ubuntu-kernels |
| https://discourse.maas.io/t/node-overview/829/ | /docs/machine-overview |
| https://discourse.maas.io/t/bmc-power-types/830/ | /docs/bmc-power-types |
| https://discourse.maas.io/t/resource-pools/831/ | /docs/resource-pools |
| https://discourse.maas.io/t/cli-testing-scripts/832/ | /docs/cli-testing-scripts |
| /t/cli-commissioning-and-hardware-testing-scripts/832 | /docs/cli-testing-scripts |
| https://discourse.maas.io/t/commissioning-and-hardware-testing-scripts/833/ | /docs/commissioning-and-hardware-testing-scripts |
| https://discourse.maas.io/t/tags/834/ | /docs/tags |
| https://discourse.maas.io/t/historical-release-notes/835/ | /docs/historical-release-notes |
| https://discourse.maas.io/t/troubleshooting/837/ | /docs/troubleshooting |
| https://discourse.maas.io/t/getting-help/838/ | /docs/getting-help |
| https://discourse.maas.io/t/historical-release-notes/835/  | /docs/whats-new-in-2-6 |
| https://discourse.maas.io/t/historical-release-notes/835/  | /docs/whats-new-in-2-7 |
| https://discourse.maas.io/t/historical-release-notes/835/  | /docs/maas-2-7-release-notes |
| https://discourse.maas.io/t/whats-new-in-maas-2-8/1655 | /docs/release-notes |
| https://discourse.maas.io/t/network-testing/1267 | /docs/network-testing |
| https://discourse.maas.io/t/markdown-test/1561 | /docs/markdown-test |
| https://discourse.maas.io/t/maas-image-builder/1112 | /docs/image-builder |
| -- | -- |
| POTENTIALLY ORPHANED TOPIC (NEEDS CHECKING) | PATH |
| -- | -- |
| https://discourse.maas.io/t/language-details-contributing-to-maas-docs/745/ | /docs/language-details-contributing-to-maas-docs |
| -- | -- |
| DEPRECATED TOPIC (MAY NEED MARKING AS SUCH) | PRESERVED PATH |
| -- | -- |
| https://discourse.maas.io/t/building-the-docs/744/ | /docs/building-the-docs |
| https://discourse.maas.io/t/working-with-git-and-github/746/ | /docs/working-with-git-and-github |
[/details]

## Redirects

[details=Mapping table]
| PATH                                   | LOCATION                                  |
| -------------------------------------- | ----------------------------------------- |
| /docs/pods                             | /docs/intro-to-vm-hosting                 |
|/docs/manage-composable-machines |/docs/intro-to-vm-hosting |
| /docs/kvm-introduction                 | /docs/intro-to-vm-hosting                 |
| /docs/manage-kvm-intro                 | /docs/intro-to-vm-hosting                 |
| /docs/add-a-kvm-host                   | /docs/add-a-vm-host                       |
| /docs/manage-kvm-add-host              | /docs/add-a-vm-host                       |
| /docs/manage-kvm-storage               | /docs/vm-host-storage-pools               |
| /docs/kvm-host-storage-pools           | /docs/vm-host-storage-pools               |
| /docs/kvm-host-networking              | /docs/vm-host-networking                  |
| /docs/manage-kvm-host-networking       | /docs/vm-host-networking                  |
| -------------------------------------- | ----------------------------------------- |
| /docs/language-details-contributing-to-juju-docs  | /docs/language-details-contributing-to-maas-docs  |
| /docs/contributing-build | /docs/building-the-docs |
| /docs/contributing-en-GB | /docs/language-details-contributing-to-juju-docs |
| /docs/contributing-git | /docs/working-with-git-and-github |
| /docs/contributing-writing | /docs/writing-guide |
| /docs/installconfig-block | /docs/block-devices |
| /docs/installconfig-checklist | /docs/installation-and-configuration-checklist |
| /docs/installconfig-images-import | /docs/select-and-import-images |
| /docs/installconfig-images-mirror | /docs/local-image-mirror |
| /docs/installconfig-images-vmware | /docs/vmware-images |
| /docs/installconfig-images | /docs/images |
| /docs/installconfig-install | /docs/install-from-a-snap  |
| /docs/installation | /docs/install-from-a-snap |
| /docs/installconfig-iso-install | /docs/install-from-iso |
| /docs/installconfig-lxd-install | /docs/install-with-lxd |
| /docs/installconfig-network-dev-discovery | /docs/network-discovery |
| /docs/installconfig-network-dhcp | /docs/dhcp |
| /docs/installconfig-network-ipranges | /docs/ip-ranges |
| /docs/installconfig-network-ipv6 | /docs/ipv6 |
| /docs/installconfig-network-ntp | /docs/ntp |
| /docs/installconfig-network-proxy | /docs/proxy |
| /docs/installconfig-network-ssl | /docs/ssl |
| /docs/installconfig-network-stp | /docs/stp |
| /docs/installconfig-network-subnet-management | /docs/subnet-management |
| /docs/installconfig-networking-config | /docs/networking |
| /docs/configure-networking | /docs/networking |
| /docs/installconfig-networking | /docs/networking |
| /docs/installconfig-package-install | /docs/install-from-packages |
| /docs/installconfig-partitions | /docs/partitions |
| /docs/installconfig-rack | /docs/rack-controller |
| /docs/installconfig-region | /docs/region-controller |
| /docs/installconfig-snap-install | /docs/install-from-a-snap |
| /docs/installconfig-storage-erasure | /docs/disk-erasure |
| /docs/installconfig-storage | /docs/storage |
| /docs/installconfig-syslog | /docs/syslog |
| /docs/installconfig-upgrade-postgres | /docs/upgrade-2-3-to-2-4-from-ubuntu-16-04 |
| /docs/installconfig-upgrade-to-2 | /docs/upgrade-from-1-9-to-2-x |
| /docs/installconfig-upgrade | /docs/upgrading-maas |
| /docs/installconfig-vmfs-datastores | /docs/vmware-vmfs-datastores |
| /docs/installconfig-webui-conf-journey | /docs/configuration-journey |
| /docs/installconfig-webui | /docs/web-ui |
| /docs/intro-communication | /docs/maas-communication |
| /docs/maas-communcation | /docs/maas-communication |
| /docs/intro-concepts-zones | /docs/zone-examples |
| /docs/intro-concepts | /docs/concepts-and-terms |
| /docs/intro-controllers | /docs/introduction-to-controllers |
| /docs/intro-explore | /docs/explore-maas |
| /docs/intro-new | /docs/whats-new-in-maas-2-7 |
| /docs/intro-requirements | /docs/what-is-maas |
| /docs/intro-what-is-maas | /docs/what-is-maas |
|/docs/maas-security|/docs/security|
| /docs/manage-account | /docs/user-accounts |
| /docs/manage-audit-events | /docs/audit-event-logs |
| /docs/manage-backup | /docs/backup |
| /docs/manage-cli-advanced | /docs/advanced-cli-tasks |
| /docs/manage-cli-common | /docs/common-cli-tasks |
| /docs/manage-cli-comp-hw | /docs/cli-composable-machines-management |
| /docs/manage-cli-dhcp-snippets | /docs/cli-dhcp-snippet-management |
| /docs/manage-cli-images | /docs/cli-image-management |
| /docs/manage-cli-interfaces | /docs/cli-interface-management |
| /docs/manage-cli-kernels | /docs/cli-kernel-management |
| /docs/manage-cli-resource-pools | /docs/cli-resource-pool-management |
| /docs/manage-cli-tags | /docs/cli-tag-management |
| /docs/manage-cli | /docs/maas-cli |
| /docs/manage-ha-postgresql | /docs/postgresql-ha-hot-standby |
| /docs/manage-ha | /docs/high-availability |
| /docs/manage-kvm-create-vms | /docs/creating-and-deleting-new-vms |
| /docs/manage-libmaas | /docs/api-client |
| /docs/manage-maas-security | /docs/security |
| /docs/manage-pods-webui | /docs/manage-composable-machines |
| /docs/manage-prometheus-metrics | /docs/prometheus-metrics |
| /docs/manage-repos | /docs/package-repositories |
| /docs/manage-rsd-add | /docs/add-an-rsd-host |
| /docs/manage-rsd-create | /docs/creating-and-deleting-machines |
| /docs/manage-rsd-intro | /docs/intel-rack-scale-design-rsd-introduction |
| /docs/manage-rsd-storage | /docs/rsd-storage |
| /docs/manage-search | /docs/interactive-search |
| /docs/manage-zones | /docs/availability-zones |
| /docs/metadata.y | /docs/documentation-index |
| /docs/nodes-add | /docs/add-nodes |
| /docs/nodes-commission | /docs/commission-nodes |
| /docs/nodes-comp-hw | /docs/intro-to-vm-hosting |
| /docs/nodes-custom | /docs/custom-node-setup-preseed |
| /docs/nodes-deploy | /docs/deploy-nodes |
| /docs/nodes-hw-testing | /docs/hardware-testing |
| /docs/nodes-kernel-options | /docs/kernel-boot-options |
| /docs/nodes-kernels | /docs/ubuntu-kernels |
| /docs/nodes-overview | /docs/machine-overview |
| /docs/node-overview | /docs/machine-overview |
| /docs/nodes-power-types | /docs/bmc-power-types |
| /docs/nodes-resource-pools | /docs/resource-pools |
| /docs/nodes-scripts-cli | /docs/cli-testing-scripts |
| /docs/nodes-scripts | /docs/commissioning-and-hardware-testing-scripts |
| /docs/syslog | /docs/logging |
| /docs/nodes-tags | /docs/tags |
| /docs/release-notes-all | /docs/historical-release-notes |
| /docs/release-notes | /docs/maas-2-7-release-notes |
| /docs/troubleshoot-faq | /docs/troubleshooting |
| /docs/troubleshoot-getting-help | /docs/getting-help |
[/details]