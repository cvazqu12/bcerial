**<center><font color=#018287>Breakfast Cerial</font></center>**

**<center>Project Overview</center>**

Breakfast Cerial (Bcerial) is solving the issue of tediously configuring the IPMI in a bare-metal server by using Python and a Serial connection to drastically reduce provisioning time.

**<center>Problem Statement</center>**


The real problem being addressed is that at the very start of a server's life, it will have no knowledge of how to give and recieve data. The first step done is to give it an address dedicated to the management of the server, or the IPMI address.

Of course, once that address is configured, all else is easy to solve, but that first step is still usually done manually. IPMITool is popular, but this tool implies that you already have an IP on the machine, and that the software supports your specific machine.

Ultimately, technicains are the ones doing this manual job, and at an example rate of $35 an hour, with an average of 220 seconds taken to complete each server, provisioning a cabinet would take more than two hours, thereby costing the employer $85 and wasting the technicians mental capability. Remote Hands rates (if a client requested this) are far in excess of a benchmark $35 an hour, and this work may be even be denied due to the time it takes.  



**<center>ISBA Subfields</center>**

* <font color= lightblue>*Application Software*</font>: Automating a redundant task

* <font color= lightblue>*Networking*</font>: Configuration of a machine to be controlled remotely

* <font color= lightblue>*Cybersecurity*</font>: Ensuring the confidentiality, integrity, and availability of the remote interactions of the remote hardware

**<center>Solution Overview</center>**

* <font color= lightblue>*Programming Languages*</font>: Python
* <font color=lightblue>*APIs*</font>: Ubersmith, Pyserial
* <font color=lightblue>*Hosting*</font>: Local

In short, Breakfast Cerial (Bcerial) is a terminal program that can quickly configure bare-metal servers at the start of its life.

**<center>Solution Overview for Nerds</center>**

Breakfast Cerial implements Pyserial (and Ubersmith's API for Version 1.0) to quickly provision bare-metal IPMIs. 

Prior to execution, the following are prerequisites for the best results:

* A server capable of RS232 communication and use of an EFI shell

* IPMICFG.efi (courtesy of Supermicro) on a USB drive (this is called the MIILK) 

*Version 1.1 Prerequisite:*
* Secrets.py file with Ubersmith login credentials. It is currently left out for security reasons. Login credential changes will come in a future update.

Bcerial instructs the user to input a severname found in their Ubersmith database. 
The API will then return a response, in which it is parsed using JSON for detailling where the IPMI IP is. With the IPMI IP extracted, it is used to create a default gateway. The subnet is only 
available as a /24 at this time. 

Prior to execution, the MIILK must be inserted into the server. Once the input is entered, the IP information is then sent to the server after mapping, finding the filesystem, and initalizing IPMICFG.efi.

Once complete, the program will automatically reboot the server. Throughout the entire process, Bcerial is informing the user at every step. 

**<center>Next Steps / Future Improvements</center>**

* Originally, the plan was to use Excel as a baseline for grabbing IPMI information, but that way can be highly ineffective if the information needs to change. It is not as automatic as going directly to the source.
The other plan was to use a web app interface and Webserial API. After much fustration, it is found that using it as a terminal program is much *much* easier to use, instead of a web browser, which is the whole point.

* Another feature that needs to be added is the ability to automatically +1, as some cabinets have a consecutive sequence of server names. 

* For a production ready release, the JSON parsing needs to focus on different keywords for parsing if the original keywords fail. 

* In order to scale for use, different databases software needs to be implemented, and a way to change credentials quickly. 

* Overall, Bcerial is designed to accomodate a specific clientele, and it needs to be adjusted for more universal adoption.

**<center>Retrospective</center>**

The biggest challenge was getting past the failed methods of implementation, such as trying to implement a web app version when that wasn't entirely nessecary, as the program runs completely fine in the terminal.
Luckily, making the switch has helped us reach deadlines.

In conclusion, simple solutions are better than complicated ones. 

**<center>References</center>**

To protect client confidentiality, slides are restricted to authorized viewers: https://docs.google.com/presentation/d/12QOFc6Q_HL2IbFdIRglw3riid0UQ_UnijndqCht2ATs/edit?usp=sharing
