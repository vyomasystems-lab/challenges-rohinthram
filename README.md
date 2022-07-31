# Capture the Bug - A Design Verification Hackathon

![](/assets/ctb_banner.png)
 
*Final Report* 

The verification of design is done using **Vyoma's UpTickPro**

![](assets/gitpod_workspace.png)

# Verification using Python

The verification of the design is done using CoCoTb module which is a Co-routine based Co-simulation Testbench for verifying digital design.

The HDL simulator used here is the **icarus-verilog** and the HDL language is **verilog**
The following is a sample Makefile to run the verification on the Device Under Test (DUT).
![](assets/sample_makefile.png)

Running make command runs the test for the module specified, hence we can verify the correctness of the design by passing various test vectors by specifying in the python testbench file and checking for proper functionality.

A sample python script for verification using CoCoTb is as shown
![](assets/sample_tb.png)

The verification and bug details for the different designs are provided in the respective directory's README.md file
- [Multiplexer](/level1_design1/README.md)
- [Sequence Detector](/level1_design2/README.md)
- [Bit Manipulation Co-processor](/level2_design/README.md)
- [Gray to Binary Code Converter using FSM](/level3_design/README.md)

---

# Author
-  R.V.Rohinth Ram

# Acknowledments
- Lavanya J, CEO/Founder, Vyoma Systems - lavanya@vyomasystems.com
- Kunal Ghosh, Co-founder, VLSI System Design (VSD) Corp. Pvt. Ltd. - kunalpghosh@gmail.com
- All other contributors

---
