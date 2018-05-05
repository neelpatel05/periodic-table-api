# periodic-table-api
API to fetch elements of the periodic table in JSON format. Uses Pandas for dumping .csv data to .json and Flask for API Integration. Deployed on "pythonanywhere.com".

## Overview
The following document will specify how to use the API to fetch the periodic elements in JSON. Also it will state different methods throught which the elements can be fetch.

|     **Data Object**    |
|------------------------|
| symbol                 |
| name                   |
| atomicMass             |
| atomicNumber           |
| atomicRadius           |
| boilingPoint           |
| bondingType            |
| cpkHexColor            |
| density                |
| electronAffinity       |
| electronegativity      |
| electronicConfiguration|
| groupBlock             |
| ionRadius              |
| ionizationEnergy       |
| meltingPoint           |
| oxidationStates        |
| standardState          |
| vanDelWaalsRadius      |
| yearDiscovered         |


## Methods
There are total of 6 methods by which you can fetch the data : 

### All

```R
- [http://neelpatel05.pythonanywhere.com/] (http://neelpatel05.pythonanywhere.com/)
```
This will fetch all the 119 elements from periodic table.

### Atomic Number

```R
- [http://neelpatel05.pythonanywhere.com/elements/atomicnumber?atomicnumber=20] (http://neelpatel05.pythonanywhere.com/elements/atomicnumber?atomicnumber=20)
```
This will fetch element from periodic table having atomic number 20. Relace 20 with any other atomic number to fetch that element from 119.

### Atomic Name

```R
- [http://neelpatel05.pythonanywhere.com/elements/atomicname?atomicname=Mercury] (http://neelpatel05.pythonanywhere.com/elements/atomicname?atomicname=Mercury)
```
This will fetch element from periodic table having atomic name "Mercury". Relace "Mercury" with any other atomic name to fetch that element.

### Atomic Symbol

```R
- [http://neelpatel05.pythonanywhere.com/elements/symbol?symbol=H] (http://neelpatel05.pythonanywhere.com/elements/symbol?symbol=H)
```
This will fetch element from periodic table having atomic symbol "H" i.e. Hydrogen. Relace "H" with any other atomic symbol to fetch that element.

### Bonding Type

```R
- [http://neelpatel05.pythonanywhere.com/element/bondingtype?bondingtype=metallic] (http://neelpatel05.pythonanywhere.com/element/bondingtype?bondingtype=metallic)
```
This will fetch all elements from periodic table having  Metallic bonding. Relace metallic with any other bonding type to fetch elements.

### Group Block

```R
- [http://neelpatel05.pythonanywhere.com/element/groupblock?groupblock=metal] (http://neelpatel05.pythonanywhere.com/element/groupblock?groupblock=metal)
```
This will fetch all elements from periodic table belongs to metal group. Relace metal with any other bonding type to fetch elements.

### State

```R
- [http://neelpatel05.pythonanywhere.com/element/state?state=gas] (http://neelpatel05.pythonanywhere.com/element/state?state=gas)
```
This will fetch all elements from periodic table belongs to gas state. Relace gas with any other state to fetch elements.


