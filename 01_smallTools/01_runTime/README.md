# 1. 项目功能

对比不同编程语言计算0到1亿累加和的时间

# 2. 文件结构

# 3. 环境配置

### 1. c

```c
#include <stdio.h>
#include <time.h>

int main() {
    clock_t start_time, end_time;
    double cpu_time_used;

    start_time = clock();

    // Calculate the sum of the first billion integers
    long long sum = 0;
    for (int i = 0; i < 1000000000; ++i) {
        sum += i;
    }

    end_time = clock();
    cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Sum: %lld\n", sum);
    printf("Time taken: %f seconds\n", cpu_time_used);

    return 0;
}
```

Sum: 499999999500000000    
Time taken: 1.890000 seconds



### 2. java

```java
public class DisplayStringsExample {
    public static void main(String[] args) {
        long startTime = System.nanoTime();

        // 执行一些计算任务，例如循环计算
        long sum = 0;
        for (int i = 0; i < 1000000000; ++i) {
            sum += i;
        }

        long endTime = System.nanoTime();
        double cpuTimeUsed = (endTime - startTime) / 1e9; // 将纳秒转换为秒

        System.out.printf("Sum: %d\n", sum);
        System.out.printf("Time taken: %f seconds\n", cpuTimeUsed);
    }
}
```

Sum: 499999999500000000     
Time taken: 0.250375 seconds



### 3. go

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	startTime := time.Now()

	// 执行一些计算任务，例如循环计算
	sum := 0
	for i := 0; i < 1000000000; i++ {
		sum += i
	}

	endTime := time.Now()
	cpuTimeUsed := endTime.Sub(startTime).Seconds()

	fmt.Printf("Sum: %d\n", sum)
	fmt.Printf("Time taken: %f seconds\n", cpuTimeUsed)
}
```

Sum: 499999999500000000   
Time taken: 0.475343 seconds



### 4. python

```py
import time

start_time = time.time()

# 执行一些计算任务，例如循环计算
sum_val = 0
for i in range(1000000000):
    sum_val += i

end_time = time.time()
time_taken = end_time - start_time

print("Sum:", sum_val)
print("Time taken:", time_taken, "seconds")
```

Sum: 499999999500000000          
Time taken: 83.71781826019287 seconds


### 5. php

```php
<?php
$start_time = microtime(true);

// 执行一些计算任务，例如循环计算
$sum = 0;
for ($i = 0; $i < 1000000000; ++$i) {
    $sum += $i;
}

$end_time = microtime(true);
$cpu_time_used = $end_time - $start_time;

echo "Sum: $sum\n";
echo "Time taken: $cpu_time_used seconds\n";
?>
```

Sum: 499999999500000000            
Time taken: 13.030443906784 seconds


### 6. javascript

```js
let startTime = new Date().getTime();

// 执行一些计算任务，例如循环计算
let sum = BigInt(0);
for (let i = 0; i < 1000000000; ++i) {
    sum += BigInt(i);
}

let endTime = new Date().getTime();
let cpuTimeUsed = (endTime - startTime) / 1000; // 将毫秒转换为秒

console.log(`Sum: ${sum}`);
console.log(`Time taken: ${cpuTimeUsed} seconds`);
```

Sum: 499999999500000000   
Time taken: 53.768 seconds


### 7. C++

```c++
#include <iostream>
#include <chrono>

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();

    // 执行一些计算任务，例如循环计算
    unsigned long long sum = 0;
    for (int i = 0; i < 1000000000; ++i) {
        sum += i;
    }

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_time = end_time - start_time;

    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Time taken: " << elapsed_time.count() << " seconds" << std::endl;

    return 0;
}
```

Sum: 499999999500000000         
Time taken: 1.96354 seconds































