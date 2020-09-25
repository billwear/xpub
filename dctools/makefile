TARGET_DEPS := maas-documentation-25.html
TARGET_DEPS += api-authentication-742.html
TARGET_DEPS += contact-us-743.html
TARGET_DEPS += language-details-contributing-to-maas-docs-745.html
TARGET_DEPS += writing-guide-747.html
TARGET_DEPS += block-devices-749.html
TARGET_DEPS += installation-and-configuration-checklist-750.html
TARGET_DEPS += select-and-import-images-751.html
TARGET_DEPS += local-image-mirror-752.html
TARGET_DEPS += vmware-images-753.html
TARGET_DEPS += images-754.html
TARGET_DEPS += install-with-lxd-757.html
TARGET_DEPS += network-discovery-758.html
TARGET_DEPS += managing-dhcp-759.html
TARGET_DEPS += ip-ranges-760.html
TARGET_DEPS += ipv6-addressing-761.html
TARGET_DEPS += ntp-services-762.html
TARGET_DEPS += proxy-763.html
TARGET_DEPS += configuring-tls-encryption-764.html
TARGET_DEPS += managing-stp-765.html
TARGET_DEPS += subnet-management-766.html
TARGET_DEPS += networking-768.html
TARGET_DEPS += partitions-770.html
TARGET_DEPS += rack-controllers-771.html
TARGET_DEPS += region-controllers-772.html
TARGET_DEPS += maas-installation-from-a-snap-773.html
TARGET_DEPS += disk-erasure-774.html
TARGET_DEPS += storage-775.html
TARGET_DEPS += upgrade-2-3-to-2-4-from-ubuntu-16-04-777.html
TARGET_DEPS += upgrade-from-1-9-to-2-x-778.html
TARGET_DEPS += upgrading-maas-779.html
TARGET_DEPS += vmware-vmfs-datastores-780.html
TARGET_DEPS += configuration-journey-781.html
TARGET_DEPS += maas-communication-783.html
TARGET_DEPS += zone-examples-784.html
TARGET_DEPS += concepts-and-terms-785.html
TARGET_DEPS += introduction-to-controllers-786.html
TARGET_DEPS += explore-maas-787.html
TARGET_DEPS += whats-new-in-2-6-788.html
TARGET_DEPS += maas-requirements-789.html
TARGET_DEPS += user-accounts-790.html
TARGET_DEPS += audit-event-logs-791.html
TARGET_DEPS += backup-792.html
TARGET_DEPS += cli-advanced-tasks-793.html
TARGET_DEPS += common-cli-tasks-794.html
TARGET_DEPS += cli-composable-hardware-795.html
TARGET_DEPS += cli-dhcp-snippet-management-796.html
TARGET_DEPS += cli-image-management-797.html
TARGET_DEPS += cli-interface-management-798.html
TARGET_DEPS += cli-kernel-management-799.html
TARGET_DEPS += cli-resource-pool-management-800.html
TARGET_DEPS += cli-tag-management-801.html
TARGET_DEPS += maas-cli-802.html
TARGET_DEPS += postgresql-ha-hot-standby-803.html
TARGET_DEPS += high-availability-804.html
TARGET_DEPS += creating-and-deleting-vms-806.html
TARGET_DEPS += python-api-client-810.html
TARGET_DEPS += prometheus-metrics-813.html
TARGET_DEPS += package-repositories-814.html
TARGET_DEPS += interactive-search-819.html
TARGET_DEPS += availability-zones-820.html
TARGET_DEPS += add-machines-821.html
TARGET_DEPS += commission-machines-822.html
TARGET_DEPS += custom-machine-setup-824.html
TARGET_DEPS += deploy-machines-825.html
TARGET_DEPS += hardware-testing-826.html
TARGET_DEPS += kernel-boot-options-827.html
TARGET_DEPS += ubuntu-kernels-828.html
TARGET_DEPS += introduction-to-machines-829.html
TARGET_DEPS += power-management-830.html
TARGET_DEPS += resource-pools-831.html
TARGET_DEPS += cli-commissioning-and-hardware-testing-scripts-832.html
TARGET_DEPS += commissioning-and-hardware-testing-scripts-833.html
TARGET_DEPS += maas-tags-834.html
TARGET_DEPS += historical-release-notes-835.html
TARGET_DEPS += maas-2-6-release-notes-836.html
TARGET_DEPS += troubleshooting-837.html
TARGET_DEPS += getting-help-838.html
TARGET_DEPS += about-maas-840.html
TARGET_DEPS += maas-image-builder-1112.html
TARGET_DEPS += network-testing-1267.html
TARGET_DEPS += whats-new-in-maas-2-6-1305.html
TARGET_DEPS += whats-new-in-maas-2-7-1306.html
TARGET_DEPS += give-me-an-example-of-maas-1314.html
TARGET_DEPS += hardening-your-maas-installation-1381.html
TARGET_DEPS += maas-logging-1468.html
TARGET_DEPS += commissioning-logs-1478.html
TARGET_DEPS += tips-tricks-and-traps-1506.html
TARGET_DEPS += introduction-to-vm-hosting-1524.html
TARGET_DEPS += vm-host-storage-pools-1525.html
TARGET_DEPS += vm-host-networking-1526.html
TARGET_DEPS += adding-a-vm-host-1549.html
TARGET_DEPS += creating-a-custom-ubuntu-image-1652.html
TARGET_DEPS += whats-new-in-maas-2-8-1655.html

OVAN = ~/var/www/html/maas-offline/maas-vanilla
OCLI = ~/var/www/html/maas-offline/maas-cli-only
OUI  = ~/var/www/html/maas-offline/maas-ui-only
RVAN = ~/var/www/html/maas-rad/maas-vanilla
RCLI = ~/var/www/html/maas-rad/maas-cli-only
RUI  = ~/var/www/html/maas-rad/maas-ui-only

%.html: %.md
# vanilla version
	cp templates/offline-vanilla-template.html ./template.html
	sed -i 's/zork/$@/g' ./template.html
	xpub convert dc2html -t vanilla $<
	mkdir -p $(OVAN) && cp $@ $(OVAN)
	cp templates/rad-vanilla-template.html ./template.html
	sed -i 's/zork/$@/g' ./template.html
	xpub convert dc2html -t vanilla $<
	mkdir -p $(RVAN) && cp $@ $(RVAN)
# ui-only version
	cp templates/offline-ui-only-template.html ./template.html
	sed -i 's/zork/$@/g' ./template.html
	xpub convert dc2html -t ui $<
	mkdir -p $(OUI) && cp $@ $(OUI)	
	cp templates/rad-ui-only-template.html ./template.html
	sed -i 's/zork/$@/g' ./template.html
	xpub convert dc2html -t ui $<
	mkdir -p $(RUI) && cp $@ $(RUI)	
# cli-only version
	cp templates/offline-cli-only-template.html ./template.html
	sed -i 's/zork/$@/g' ./template.html
	xpub convert dc2html -t cli $<
	mkdir -p $(OCLI) && cp $@ $(OCLI)	
	cp templates/rad-cli-only-template.html ./template.html
	sed -i 's/zork/$@/g' ./template.html
	xpub convert dc2html -t cli $<
	mkdir -p $(RCLI) && cp $@ $(RCLI)	

finale: $(TARGET_DEPS)
	xpub push github
	mkdir -p $(OVAN)/images && cp images/* $(OVAN)/images
	mkdir -p $(RVAN)/images && cp images/* $(RVAN)/images
	mkdir -p $(OCLI)/images && cp images/* $(OCLI)/images
	mkdir -p $(RCLI)/images && cp images/* $(RCLI)/images
	mkdir -p $(OUI)/images && cp images/* $(OUI)/images
	mkdir -p $(RUI)/images && cp images/* $(RUI)/images
	mkdir -p $(OVAN)/css && cp -r css/* $(OVAN)/css
	mkdir -p $(RVAN)/css && cp -r css/* $(RVAN)/css
	mkdir -p $(OCLI)/css && cp -r css/* $(OCLI)/css
	mkdir -p $(RCLI)/css && cp -r css/* $(RCLI)/css
	mkdir -p $(OUI)/css && cp -r css/* $(OUI)/css
	mkdir -p $(RUI)/css && cp -r css/* $(RUI)/css



