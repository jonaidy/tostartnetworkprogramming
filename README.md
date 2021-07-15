# tostartnetworkprogramming

There are few steps that I need you to follow before we can start lesson or further discussion.

1. Are you using Windows or Linux?
   It is not advisable to mix the working environment when your test environment. In testing or developing codes sometimes you need to install libraries, and you need to have control on your OS. Recommendation is to install Linux VM over your Hyper-V, or Virtualbox or VMware player. My personal preference for linux distribution for this purpose is Ubuntu. You can download the ISO image here... https://ubuntu.com/download/desktop/thank-you?version=20.04.2.0&architecture=amd64
   
2. Preparing your development environment.
   First step after installing your linux VM is to update the software. You can follow the steps in this website https://www.itzgeek.com/post/how-to-update-ubuntu-20-04-lts/
   
3. Install your preferred Python Development Environment.
   We have options from Atom, Visual Studio Code, or Pycharm Community Edition. All are equally good,they have their pros and cons. My personal preference is Pycharm Community Edition. So if you have no preference, you can follow by installing pycharm community edition. Make sure you download the 'community" version.
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC

4. Connect your lab to your development environment.
   Assuming you have lab environment with CML2 or GNS. You can configure your lab to be accessible to your development VM network by attaching them to the same network adapter. For example, I have GNS attached to host network, then you have to attached your VM to host network as well.
   ![image](https://user-images.githubusercontent.com/22738494/125716384-1f560240-77ac-44e7-b6a4-52e9070f312e.png)
I attached my VM to both bridge to get to internet and to host-only network to reach my GNS lab.
   ![image](https://user-images.githubusercontent.com/22738494/125716531-08ce89c9-8c30-44c5-a808-9f2bb809ff33.png)

Plan for your lab network IP address scheme, and preferably very much different from your physical network. In this example, I have my lab network in 172.16.16.0, and my GNS VM IP address is 192.168.88.51/24 (ens38). I configured my linux VM to connect host-only interface with DHCP. As depicted in below capture, you can see ens38 is the interface connected to my GNS LAB.
   ![image](https://user-images.githubusercontent.com/22738494/125717169-5c0c749d-26e8-4260-9f80-4919079ccfdf.png)

Next, please configure static route to reach 172.16.16.0 (your lab network), you can use terminal and key in the command below. This is not permanent, and everytime the OS restart, the static route will be deleted from system.

sudo ip route add 172.16.16.0/24 via 192.168.88.51 ens38

For permanent static route, you can go to your ubuntu utility to add the config (easy mode).
![image](https://user-images.githubusercontent.com/22738494/125717490-8d81b62e-1d94-4ae1-9a43-470759e40465.png)
![image](https://user-images.githubusercontent.com/22738494/125717532-3d6bb3a9-6dea-4d32-bf3e-077c2f9c6901.png)
![image](https://user-images.githubusercontent.com/22738494/125717590-002fba29-336f-49c8-bbf1-3da8f2287fb1.png)

Add the static route here..
![image](https://user-images.githubusercontent.com/22738494/125717644-6b718979-8f6d-4e0a-be70-ec2fa4c1a42c.png)

To activate your static route configuration, turn off and on the switch for interface ens38 (or what ever interface name you have)
![image](https://user-images.githubusercontent.com/22738494/125717760-430dd9b9-10a6-4d74-b307-c3f382129a24.png)

By now, you can ping your lab equipment from the Ubuntu VM...


