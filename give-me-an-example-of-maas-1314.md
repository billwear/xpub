An evolving example may be useful to introduce you to MAAS, and it doesn't have to be comprehensive --  just coherent and plausible.  This example will continue to expand and update over time.

![splash-screen|690x406](https://discourse.maas.io/uploads/default/optimized/1X/18456dbd3fbfec14eddd044816fd0719692282da_2_690x406.jpeg) 

So imagine that you're the IT administrator for a new, 100-bed hospital that's under construction, intended to serve a suburban community of 5,000 people.  Call it "Metaphorical General Hospital" (MGH).   Your job is to design a flexible datacentre for this facility.  You've decided to start with MAAS as your tool of choice, and for this planning exercise, you'll use VMs in a VM host.

<h2>Machines</h2>

You'll need to start with a little network thinking (and design).  Talking through requirements with the staff, you come up with a random list of functions:
<table width="100%">
<tr><td>Charts</td><td>Provider orders</td><td>Provider documentation</td></tr>
<tr><td>Pharmacy</td><td>Narcotics control</td><td>Insurance collections</td></tr>
<tr><td>Housekeeping</td><td>Nursing orders</td><td>Med reconciliation</td></tr>
<tr><td>Timeclock</td><td>Patient collections</td><td>Med/surgical supplies</td></tr>
<tr><td>Office supplies</td><td>Patient registration</td><td>Insurance reconciliation</td></tr>
<tr><td>Payroll</td><td>Medication admin</td><td>Continuing education</td></tr>
<tr><td>Food service</td><td>Instrumentation</td><td>Information technology</td></tr>
</table>

You can handle this lowest level with individual [machines](/t/introduction-to-machines/829).  With MAAS, you'll be able to modify how many machines are performing which functions, somewhat on-the-fly, but let's assume that you start by creating (at least) one VM for each function.  Since you can reassign machines at will, you aren't going to name them for their functions; instead, you're just going to use the MAC address of each machine to uniquely identify it.

<details>
<summary>
<em>Try it!</em>
</summary>
<h4>Creating some sample VMs</h4>

Assuming you've [installed libvirt](https://help.ubuntu.com/lts/serverguide/libvirt.html) on the machine where you'll be running MAAS, you can create virtual machines like this:

1. Open the Virtual Machine Manager application.  You'll see a screen that looks something like this:

![vmm|690x330](https://discourse.maas.io/uploads/default/optimized/1X/f66940a21313a27734bcaef6c539d36a720a6834_2_690x330.jpeg) 

2. Choose File --> New Virtual Machine, which brings you to a corresponding dialog:

![kvm-1|465x500](https://discourse.maas.io/uploads/default/original/1X/0702d9f2ab4c3659d13be553449093548a9e2f10.jpeg) 

3. Select the "Network Boot (PXE)" option and click the "Forward" button:

![kvm-2|465x500](https://discourse.maas.io/uploads/default/original/1X/0000fb5f072f2b3668465753ae6a713859d8a444.jpeg)

4.  Choose the "Generic..." operating system by typing the first letters of "Generic" in the text box and selecting the relevant choice when it becomes available, then go Forward:

![kvm-3|465x500](https://discourse.maas.io/uploads/default/original/1X/041914a0718633fce685ac7919e2478da0e62c1b.jpeg) 

5. For CPU and memory, you can usually accept the defaults:

![kvm-4|465x500](https://discourse.maas.io/uploads/default/original/1X/5a46262e3573aae7252951b3331ac9e3f3ef69c4.jpeg) 

6. whereas the storage values have a noticeable effect on local disk usage, so note that, generally, a VM only requires about 5.0 GiB, given an example exercise like this:

![kvm-5|465x500](https://discourse.maas.io/uploads/default/original/1X/15f5e344c03bd1469c00333d466027e403c00ee8.jpeg) 

7. In the next screen, you'll have the chance to set a name; here, we've used a pseudo-MAC address, although you can name the machine whatever you want (and then return later to set the name to match the MAC address, if desired):

![kvm-6|465x500](https://discourse.maas.io/uploads/default/original/1X/d4191b100d963032d47fed1f198aea76e8de273e.jpeg) 

8. Selecting "Finish" will create the virtual machine and attempt to boot it -- which will fail, since no device currently knows about this VM (and hence can't boot it).  Not to worry; you're not done yet:

![kvm-7|625x500](https://discourse.maas.io/uploads/default/original/1X/09b4e50049c2a251d100113e50a241d0c4a06f51.jpeg) 

9. Select the "information" button (blue circle, white lowercase "i") to switch to the VM configuration screens, then select the "Boot Options" choice from the left-hand menu:

![kvm-9|619x500](https://discourse.maas.io/uploads/default/original/1X/7b6cd37f7663db53571845da0159977092898fa4.jpeg) 

10. Turn off the "IDE" item under "Boot device order:"

![kvm-10|619x500](https://discourse.maas.io/uploads/default/original/1X/54a8d6a77d9660e13aa1c0e278048ed1c751d65e.jpeg) 

11. When you select "Apply," a dialog will pop up to remind you that you need to restart this VM for changes to take effect:

![kvm-11|480x183](https://discourse.maas.io/uploads/default/original/1X/6f4ab26216cc2951a202851869f7c7efc5691129.jpeg) 

12. Switch to the "NIC..." option and set the "Network source" and "Device model" as shown, then select "Apply" and respond to the dialog:

![kvm-12|619x500](https://discourse.maas.io/uploads/default/original/1X/26fe981020c03e46c81e2bceed840bea7b2f14d6.jpeg) 

13. You'll next select the dropdown arrow next to the "on/off" menu bar option and select "Force reset," then answer the prompt in the affirmative:

![kvm-13|502x245](https://discourse.maas.io/uploads/default/original/1X/537a485f0ff014aeb82afc71bc09b2988bf5cb56.jpeg) 

You now have a VM that you can add to MAAS.  If you want more than one, you can simply right-click on the one you've just created and select "Clone:"

[Note] **Pro Tip**: Cloned VMs tend to use considerably less host disk space than newly-created ones. [/Note]

![kvm-14|456x468](https://discourse.maas.io/uploads/default/original/1X/2348efd7dbf17ba445e3c4e6b3926fdc8cfbc888.jpeg) 

Another VM will instantiate, using the name of the cloned VM with an added "-clone" suffix:

![kvm-15|690x224](https://discourse.maas.io/uploads/default/original/1X/a14b17602c2ad2465197a77c302080ca2eb59fc8.jpeg) 

You can create VMs as desired, remembering to mind your overall disk usage on your host system.

</details>

Let's assume that once you're done adding VMs, you have around 20 up and ready, all named after their assigned MAC address:

![kvms|517x500](https://discourse.maas.io/uploads/default/optimized/1X/f9f302d8de9344908758a433dae9abfada0b0db3_2_517x500.jpeg) 

No need to create a lot of VMs for this example (unless you just want to do so).  

<h3>Manually adding machines</h3>

Once you've created the necessary VMs, you'll want to [manually add machines](/t/add-machines/821#heading--add-a-node-manually) to MAAS that correspond to your VMs.

![blank-machines|690x440](https://discourse.maas.io/uploads/default/original/1X/91679cd615868eda4654541a68e59de57328ddfa.jpeg) 

<details>
<summary><em>Try it!</em></summary>

Creating a machine from a VM requires about a dozen pieces of information, most of which you can gather from the VM itself:

![add-machine-screen|690x270](https://discourse.maas.io/uploads/default/optimized/1X/bc6c18c0fd31367bd4a9909fb7d954dc06f15c40_2_690x270.jpeg) 

In the left column, you're only required to enter a machine name and the machine's MAC address:  

![left-column|690x481](https://discourse.maas.io/uploads/default/original/1X/1de8d7afae996292d71e9787641bf0317b2327c9.jpeg) 

Here, we've assigned a variant of the MAC address as the machine name.  Note that the machine name cannot include colons (":"), we've substituted dashes.  In the right column, it's necessary to choose the power type.  When enlisting VMs, the correct power type is "Virsh," as shown below:

![right-column|690x271](https://discourse.maas.io/uploads/default/original/1X/aa076ee437ce481808bb5f41320a45e60f3676de.jpeg) 

For default configurations, the Virsh Address is "qemu+ssh://[your-login-id]@192.168.122.1/system;" replace "[your-login-id]" with your username or login ID on the machine where you're hosting MAAS and the Virtual Machine Manager.  Likewise, the password is your normal login password for the same host.  Finally, you can retrieve the Virsh VM ID from the "Overview" screen of the VM itself:

![kvm-16|619x500](https://discourse.maas.io/uploads/default/original/1X/79e135e48576bb6f455dd42fd7a09a2c7448d221.jpeg) 
</details>

As you add machines, they automatically commission:

![auto-commission|639x407](https://discourse.maas.io/uploads/default/original/1X/37f1df9e4072b29c7183d4ae8ec1768504c4f66f.jpeg) 

When finished, the commissioned machines with be at the "Ready" state.

<h2>Tags</h2>

Assigning machines to specific functions is something you can do after you [commission](/t/commission-machines/822) and [deploy](/t/deploy-machines/825) them.  (Later on, we'll discuss ways to load user apps and data onto the machines using the MAAS API.) Once you've got machines running apps, you want to keep up-to-date about which machine is doing what, when you're looking at the machine list.  You'll want to assign [tags](/t/maas-tags/834) to machines.  

![tags|690x422](https://discourse.maas.io/uploads/default/original/1X/2ea0827b9ef327b59ad722215d556969218cc22f.jpeg) 

<details>
<summary><em>Try it!</em></summary>
Adding a tag to a machine is simple.  Just decide which machine you want to tag:

![tags-2|690x204](https://discourse.maas.io/uploads/default/optimized/1X/4f32fb8105ecee30afd0f3ca226b265dffe6e11b_2_690x204.jpeg) 

You'll want to click on the machine name (in this case, the MAC address), and then choose "Configuration" on the next screen that comes up.  This will bring you to a screen from which you can edit some parameters about the machine:

![tags-3|690x256](https://discourse.maas.io/uploads/default/optimized/1X/c31a50cebf68c8c5fbfbbe0115bb5c1daeb84ae8_2_690x256.jpeg) 

Click on "Edit," and then add a tag name to the "Tags" field.  Tags are automatically remembered by MAAS, so the next time you want to enter the same tag, an autocomplete field will appear, as shown below:

![tags-4|690x256](https://discourse.maas.io/uploads/default/optimized/1X/39a0e2f01ba7f3dc141bcf57c09b4e62f737525d_2_690x256.jpeg) 

Select "Save changes" to add the tag(s) to the machine.  When you return to the machine list, you'll note that the tag is now associated with that machine:

![tags-5|690x222](https://discourse.maas.io/uploads/default/optimized/1X/8a21ca291aa800440d9074270ab9d9108cff9be1_2_690x222.jpeg) 

</details>

Tags can will help you keep up with which machine(s) are covering which functions as you apply your apps.  You can search and filter by tags, and you can utilize tags from within the API, as well.

<h2>Resource pools</h2>

As you look at the list of functions you've created, and talk more with the staff, you discover that some of these functions fit together more closely than others.  With some effort, you work out the following update to your network design:

<table width="100%">
<tr><td><strong>Provider services</strong></td><td></td><td></td></tr>
<tr><td>Charts</td><td>Provider orders</td><td>Provider documentation</td></tr>
<tr><td><strong>Nursing services</strong></td><td></td><td></td></tr>
<tr><td>Nursing orders</td><td>Continuing education</td><td></td></tr>
<tr><td><strong>Nursing meds</strong></td><td></td><td></td></tr>
<tr><td>Medication administration</td><td>Narcotics control</td><td></td></tr>
<tr><td><strong>Prescriber controls</strong></td><td></td><td></td></tr>
<tr><td>Pharmacy</td><td>Narcotics control</td><td>Medication reconciliation</td></tr>
<tr><td><strong>Staff compensation</strong></td><td></td><td></td></tr>
<tr><td>Timeclock</td><td>Payroll</td><td></td></tr>
<tr><td><strong>Supplies & services</strong></td><td></td><td></td></tr>
<tr><td>Medical and surgical supplies</td><td>Office and general supplies</td><td></td></tr>
<tr><td><strong>Business office</strong></td><td></td><td></td></tr>
<tr><td>Patient registration</td><td>Insurance reconciliation</td><td></td></tr>
<tr><td><strong>Collections</strong></td><td></td><td></td></tr>
<tr><td>Patient collections</td><td>Insurance collections</td><td></td></tr>
<tr><td><strong>Patient support</strong></td><td></td><td></td></tr>
<tr><td>Housekeeping</td><td>Food service</td><td></td></tr>
<tr><td><strong>Staff support</strong></td><td></td><td></td></tr>
<tr><td>Instrumentation</td><td>Information technology</td><td></td></tr>
</table>

You're aware that the number of machines you'll need use for each of the individual functions with vary according to real-world events in the hospital.  Still, you'd prefer to budget machines for these different functions, so that you know you can meet the needs of each.  The easiest way to handle this?  Creating [resource pools](/t/resource-pools/831) and naming them after the (new) top-level headings in your outline.  That way, you can reserve some number of machines for those functions, learning over time the right number of machines to allocate to each activity.

<details>
<summary><em>Try it!</em></summary>

Notice at the top of the machine list, there is a tab labeled, "Resource pools:"

![pools-1|690x447](https://discourse.maas.io/uploads/default/original/1X/f7d4c52a176f53f29a0c1ac3190e7abb563dc993.jpeg) 

In this example, there are already some resource pools defined to match the different functions above, except for one: Provider services.  Click the "Resource pools" tab to go there:

![pools-2|690x239](https://discourse.maas.io/uploads/default/optimized/1X/c05804c1f1bba45439d8894698b4dcefd64e7a5a_2_690x239.jpeg) 

To add the "Provider services" (ProServ) pool, click on "Add pool:"

![pools-3|690x160](https://discourse.maas.io/uploads/default/optimized/1X/bebf192974683dde6cb21407f6db299f1e407925_2_690x160.jpeg) 

Fill in the fields for "Name" (which is a required field, with no spaces), and for "Description."  In this case, we've filled them in with "ProServ" and "Provider services:"

![pools-4|690x164](upload://mutNbxfTQOVU5JwXBvESQ84iNuN.jpeg) 

Click on "Add pool" to add this resource pool to the list, then click on "Machines" to return to the machine list.  Once there, it's simple to add machines to a particular pool.   In the column marked "POOL/NOTE," you'll see that your machines are in the "default" pool when created.  If you click on "default" there, you'll bring up a dropdown of already-created resource pools:

![pools-5|690x333](https://discourse.maas.io/uploads/default/original/1X/f373606dcd50c96a35af932379830f101d4a77e0.jpeg) 

Just choose the one you want for this machine (in our example, ProServ) and you're done:

![pools-6|690x215](https://discourse.maas.io/uploads/default/original/1X/0cff1cf26f28236dbabc89b14a92c69435934933.jpeg) 

</details>

Here's a snippet of the updated machine list, with all machines added to the appropriate resource pool:

![pools-7|681x500](https://discourse.maas.io/uploads/default/original/1X/704b6d1603f6f90fca42891d98c3bb418458b94a.jpeg) 

Resource pools are mostly for your use, helping you to budget servers within a given category.  Untagged servers can be in a pool, so if you've got five servers in the "Prescriber controls" resource pool, you can tag them with "Pharmacy," "Medication reconciliation," etc., as you use them.  It will also be obvious when you're running low on servers for that pool, and need to either provision more or move some unused ones from another pool.

<h2>Notes</h2>

Another optional identifier for machines is the "Note" field.  While it can be long, a portion of it shows up on the machine list, which makes it useful for adding special identifiers or groupings.  In this example, we've added a vague identifier which might help an IT admin remember server locations or access rights.

![notes-1|690x87](https://discourse.maas.io/uploads/default/optimized/1X/8724395dfe9fc4d3f4a10a05687c33c6a3dded07_2_690x87.jpeg) 

<details>
<summary><em>Try it!</em></summary>

You can edit notes by clicking on a machine name in the machine list, switching to the "Configuration" tab, and selecting the "Edit" button.  These choices will bring you to a screen like this one:

![notes-2|690x348](https://discourse.maas.io/uploads/default/original/1X/a9d61f28a4ada7d97ff6f896d2f1e8e719ad680b.jpeg) 

From here, you can add freeform text into the "Note" field:

![notes-3|690x330](https://discourse.maas.io/uploads/default/original/1X/f8d647daffa9b3210fb99d440107a58e539a6c35.jpeg) 

When you save the changes and return to the machine list, you'll notice that the NOTE field for that machine now contains your changes: 

![notes-4|690x93](https://discourse.maas.io/uploads/default/original/1X/46cf42808ef44829f1c610e479d6dfb62af2d898.jpeg) 

</details>

<h2>VLANs</h2>

Looking over your design, you notice that some of these resource pools must have their network traffic "firewalled" from others -- for example, Provider services and Nursing services shouldn't be readily visible to Staff compensation or Food service.  Likewise, the relevant monitoring agencies require that facilities manage medications as a separate activity. The traditional way to separate these networks (other than creating entirely *separate* networks) would be a VLAN.  Luckily, MAAS supports multiple VLANS.  Adding one higher level to your design, you find yourself with this updated network topology:

<table width="100%">
<tr><td><strong>Caregiver services</strong></td><td></td></tr>
<tr><td>Provider services</td><td>Nursing services</td></tr>
<tr><td><strong>Medication management</strong></td><td></td></tr>
<tr><td>Nursing meds</td><td>Prescriber controls</td></tr>
<tr><td><strong>Accounts payable</strong></td><td></td></tr>
<tr><td>Staff compensation</td><td>Supplies & services</td></tr>
<tr><td><strong>Accounts receivable</strong></td><td></td></tr>
<tr><td>Business office</td><td>Collections</td></tr>
<tr><td><strong>Patient support</strong></td><td></td></tr>
<tr><td>Housekeeping</td><td>Food service</td></tr>
<tr><td><strong>Staff support</strong></td><td></td></tr>
<tr><td>Instrumentation</td><td>Information technology</td></tr>
</table>

Each of these higher-level groupings is ideal for a VLAN, so you create six of them, one for each division:

![vlans-1|690x365](https://discourse.maas.io/uploads/default/original/1X/7245ed378ce0b9000aaf6f15b16ea16dbde2fccf.jpeg) 

<details>
<summary><em>Try it!</em></summary>

Adding a functional VLAN requires some additional (common) networking aspects, which we'll cover later.  In the meantime, though, here's the short version of adding and naming the VLAN itself.  

From anywhere on the MAAS page, select "Subnets" from the top menubar, which brings you to this screen:

![vlans-2|690x281](https://discourse.maas.io/uploads/default/optimized/1X/befd3a3eb5987d412477d0a076d16a50e81dae30_2_690x281.jpeg) 

Using the "Add" dropdown, select "VLAN:"

![vlans-3|690x275](https://discourse.maas.io/uploads/default/optimized/1X/dbdea7bec608d14e89da82cfdea87df3f93855dd_2_690x275.jpeg) 

You'll arrive at this screen, which allows you to specify the VLAN:

![vlans-4|690x141](https://discourse.maas.io/uploads/default/optimized/1X/e371011171ba18839f96788fefa40a04af3e79bb_2_690x141.jpeg) 

Enter the Name and ID of the VLAN, and select the fabric to enclose it (in this case, the "default" fabric):

![vlans-5|690x135](https://discourse.maas.io/uploads/default/optimized/1X/961d5cae7119db1c3fb7e8d6ae6ce7015d9263d1_2_690x135.jpeg) 

When you're satisfied with your choices, select "Add VLAN" to complete the operation.

</details>

Ignoring the networking aspects (for now), these VLANs should help isolate major functions and provide a level of data integrity and access control for your new hospital network.

<h2>Fabrics</h2>

Considering your network design so far, you notice that some of the VLANs need to be able to communicate with each other some of the time.  In fact, you decide on three pairs of VLANs to cover this new networking situation:

<table>
<tr><td><strong>Patient management</strong></td><td></td></tr>
<tr><td>Caregiver services</td><td>Medication management</td></tr>
<tr><td><strong>Accounting</strong></td><td></td></tr>
<tr><td>Accounts payable</td><td>Accounts receivable</td></tr>
<tr><td><strong>Facilities</strong></td><td></td></tr>
<tr><td>Patient support</td><td>Staff support</td></tr>
</table>

You want to incorporate these highest-level groupings into your network, but how?  MAAS provides the answer with fabrics.  A fabric is a set of interconnected VLANs that can communicate, so you simply create three fabrics, each covering one of these top-level categories.

<details>
<summary><em>Try it!</em></summary>

You can add a fabric by selecting the "Subnets" tab, clicking on the "Add" dropdown, and choosing "Fabric:"

![fabrics-1|690x329](https://discourse.maas.io/uploads/default/optimized/1X/509e9696919e69cfc57602a6228425a472b3ac1d_2_690x329.jpeg) 

You'll see the "Add fabric" dialog appear.  Enter the desired fabric name and click "Add fabric:"

![fabrics-2|690x108](https://discourse.maas.io/uploads/default/optimized/1X/7873e6a97212673ab08c8c3c33f9d63d7069b8e8_2_690x108.jpeg) 

Here you'll notice three new fabrics, one for each of the top-level groupings in your example network design:

![fabrics-3|690x304](https://discourse.maas.io/uploads/default/optimized/1X/4f787bc5d57c7f811641e32b42c96bb2a2792356_2_690x304.jpeg) 

Next, you'll want to assign your VLANs to this fabric.  Begin by clicking on any VLAN you want to move, which will bring you to a summary screen for that VLAN:

![fabrics-4|690x234](https://discourse.maas.io/uploads/default/optimized/1X/ecca590663b90106b144c003851732a16acd5220_2_690x234.jpeg) 

You can click "Edit" and choose the desired fabric from the dropdown list:

![fabrics-5|690x293](https://discourse.maas.io/uploads/default/optimized/1X/6f6e2bff0d67dc02d33800e5cc1d60db24fb398a_2_690x293.jpeg) 

Finally, click "Save summary" to move this VLAN to the desired fabric.  The end result of assigning our example VLANs to the three fabrics is shown below.

</details>

![fabrics-6|690x499](https://discourse.maas.io/uploads/default/original/1X/23c214cd6836dd783347f050f2cdba04da7bcaa1.jpeg)