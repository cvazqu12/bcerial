*Breakfast Cerial*

Project Overview
   
Your project's elevator pitch
Answer the following questions in a single sentence:

Breakfast Cerial (Bcerial) is solving the issue of tediously configuring the IPMI in a bare-metal server by using Python and a Serial connection to drastically reduce provisioning time.



Problem Statement
   
What is the real problem being addressed?
Brief summary of past attempts to solve this problem. Competitors?
How does this problem affect the customer, and how do they currently solve it?
Quantify wasted time, money, or other resources.

ISBA Subfields

List the 3 ISBA subfields involved.
Provide a short description of how each subfield is implemented.

**Solution Overview**
Programming Languages: Python
APIs: Ubersmith, Pyserial
Hosting: Local

Breakfast Cerial (Bcerial) is a terminal program that can quickly configure bare-metal servers.

*Solution Overview for Nerds*

Breakfast Cerial implements Pyserial (and Ubersmith's API for Version 1.0) to quickly provision bare-metal IPMIs. 

Prior to execution, the following are prerequisites for the best results:

A server capable of RS232 communication and use of an EFI shell
IPMICFG.efi (courtesy of Supermicro) on a USB drive (this is called the MIILK) 

Version 1.0 Prerequisite:
Secrets.py file with Ubersmith login credentials. It is currently left out for security reasons. Login credential changes will come in a future update.

It instructs the user to input a severname found in their Ubersmith database. 
The API will then return a response, in which it is parsed using JSON for detailling where the IPMI IP is. With the IPMI IP extracted, it is used to create a default gateway. The subnet is only 
available as a /24 at this time. 

Prior to execution, the MIILK must be inserted into the server. Once the input is entered, the IP information is then sent to the server after mapping, finding the filesystem, and initalizing IPMICFG.efi.

Once complete, the program will automatically reboot the server. Throughout the entire process, Bcerial is informing the user at every step. 

Next Steps / Future Improvements
Features that were planned but abandoned or scaled down.

Originally, the plan was to use Excel as a baseline for grabbing IPMI information, but that way can be highly ineffective if the information needs to change. It is not as automatic as going directly to the source.
The other plan was to use a web app interface and Webserial API. After much fustration, it is found that using it as a terminal program is much *much* easier to use, instead of a web browser, which is the whole point.

Another feature that needs to be added is the ability to automatically +1, as some cabinets have a consecutive sequence of server names. 

For a production ready release, the JSON parsing needs to focus on different keywords for parsing if the original keywords fail. 

How can the project be deployed into production if the project still needs to be in production?

What aspects can be scaled (e.g., throughput, adoption).

In order to scale for use, different databases software needs to be implemented, and a way to change credentials quickly. 

Areas for improvement or what could be done differently in the future.

Overall, Bcerial is designed to accomodate a specific clientele, and it needs to be adjusted for more universal adoption.

Retrospective

Specific challenges encountered during the project and how they were addressed.

The biggest challenge was getting past the failed methods of implementation, such as trying to implement a web app version when that wasn't entirely nessecary, as the program runs completely fine in the terminal.
Luckily, making the switch has helped us reach deadlines.

New skills or insights gained throughout the project.

Simple solutions are better than complicated ones. It doesn't need to complicated, and less code needed means it's easier to fix and improve. 

References
To protect client confidentiality, slides are restricted to authorized viewers: https://docs.google.com/presentation/d/12QOFc6Q_HL2IbFdIRglw3riid0UQ_UnijndqCht2ATs/edit?usp=sharing
