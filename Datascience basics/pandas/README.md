# Pandas: 

## DataFrame:
**Code:**

```
import pandas as pd
print("DataFrame 1: ");
fruits = pd.DataFrame({"Apples":[30], "Bananas":[21]})
print(fruits);
print("\n");

print("DataFrame 2: ");
fruits = pd.DataFrame({"Apples":[30,29], "Bananas":[21, 21]})
print(fruits);
print("\n");
```

**Output:**

DataFrame 1: 

   Apples  Bananas

0      30       21

DataFrame 2: 

   Apples  Bananas

0      30       21

1      29       21
