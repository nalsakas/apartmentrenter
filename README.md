# apartmentrenter
Find minimum distance a renter would walk to reach any given target. In other words
minimize max walking distance for any given target.

## Problem statement:
For a a given blocks of apartments, residents needs to walk to "gmy", "school" and "store" on foot.
If you are lucky resident all that targets can be found in the same block.
You as a renter need to choose one of a given blocks, such that max walking distance
to any target(gym, school or store) will be min among all

## Solution:
- Loop through all apartment blocks to calculate list of min distances one should walk for each target.
- Keeps only max walking distance in result list, discard others
- Loop through result list to find min walking distance block
- Rent apartment from that block