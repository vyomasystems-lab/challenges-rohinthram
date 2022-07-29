# Gray to Binary Code Converter using FSM Design Verification

![](../assets/code_cnvt_1.png)

## Verification Environment
The test drives inputs to the Design Under Test using dut.&lt;input-port-name&gt;.value = &lt;value&gt;

The values are assigned to the input port using 
```
inp = [31]*12

for i in range(len(inp)):
    dut.inp.value = inp[i]
```

The assert statement is used for comparing the output from the Code Converter with the expected value.


```
assert int(dut.out.value) == inp[i], "Incorrect Operation"
```


## Test Scenario 1


## Test Scenario 2

Output mismatches for the above inputs proving that there is a design bug

![](../assets/code_cnvt_fail.png)

## Bug
Based on the above test input and analysing the design, we see the following

![](../assets/code_cnvt_bug.png)


## Design Fix
Updating the design and re-running the test makes the test pass.

![](../assets/code_cnvt_pass.png)

The updated design is checked in as main_corrected.v

## Verification Strategy
 Give few possible 5bit gray codes and check if the output is same as its binary equivalent.

## Is the verification complete ?
 Verification is complete, but there may be certain edge cases that may fail.