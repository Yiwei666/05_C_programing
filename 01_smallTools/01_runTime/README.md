


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

































