# Hashing
For this assignment, I used a couple of techniques to attempt to optimize the hash table.

## Changing the hash function
I tried two different functions:
* The polynomial rolling hash function
* The djb2 hash function
  
These were used with the chaining technique for collision avoidance with only 10000 slots in the table
### Polynomial Rolling Hash
This algorithm added all the characters by multiplying their ASCII value with the power of prime number corresponding with their location. To avoid stupidly large numbers and so that it completes in a reasonable time, the modulus operator is used during intermediate steps.

![](/screenshots/rolling-polynomial-hash.png)

The statistics were not terrible, and there were inevitably going to be collisions. However, it used up quite a bit of the available space
### djb2 Hash
This algorithm works by iterating over every character and then multiplying the previous result by 33 and then adding the ASCII value. 33 seems to have been choosen because it can be done by a shift operator and an addition. The initial value is a prime number, seemingly arbitrarily choosen in the original algorithm by Daniel J. Bernstein.

![](/screenshots/djb2.png)

As yo can see, it performs slightly better than the rolling polynomial hash function in both collisions and unused slots, but not by much.

## Changing the collision resolution
For the actual hash functions, I used the chaining method for resolving collisions.
I also tried using linear probing. For these, there were 20000 slots in the table, so the unused count will be 5000 for all of them since there were only 15000 items in the testing set. All of these methods had more collisions than the above hash functions, mostly because probing makes it more likely for there to be a collision in the first place.

### Linear Probing
Using standard linear probing with the rolling hash function, I got these statistics:

![](/screenshots/linear-probing.png)

As you can see, they filled the exact same ammount of buckets for both hash tables, however they had loads more collisions than any of the above methods. That is because of clustering, where if multiple values get the same hash, it will choose the next available spot. If many get the same hash or a nearby hash that was already taken, finding an available spot runs into many collisions, completely inflating the collision count.

### Double Hashing
This is a method where for collision resolution, you increment by the result of a different hash function. I used the djb2 hash function for the primary hash function and the rolling hash function for collision resolution

![](/screenshots/double-hashing.png)

As you can see, there were way less collisions because it was far less likely to run into the same thing again.

## General thoughts
For some reason, the movie name tables had consistently more collisions and unused buckets than the quote tables. I do not know why that is the case
