"""
Author: Gabriel Viana

Desenvolvido com ajuda de LLM (copilot)
"""

class Bucket:
   
    def __init__(self, bucket_size: int, local_depth: int = 1):
        
        self.bucket_size = bucket_size
        self.local_depth = local_depth
        self.entries = {}
    
    def is_full(self) -> bool:
        """Check if the bucket is full."""
        return len(self.entries) >= self.bucket_size
    
    def insert(self, key: int, value: int) -> bool:
        """
        Insert a key-value pair into the bucket.
        """
        if self.is_full() and key not in self.entries:
            return False
        self.entries[key] = value
        return True
    
    def search(self, key: int) -> int:
        """
        Search for a value by key in the bucket.
        """
        return self.entries.get(key)
    
    def remove(self, key: int) -> bool:
        """
        Remove a key-value pair from the bucket.
        """
        if key in self.entries:
            del self.entries[key]
            return True
        return False
    
    def get_all_entries(self) -> dict:
        """Return all entries in the bucket."""
        return self.entries.copy()
    
    def is_empty(self) -> bool:
        """Check if the bucket is empty."""
        return len(self.entries) == 0


class ExtensibleHash:
    
    def __init__(self, bucket_size: int):
        """
        Initialize the extensible hash with the specified bucket size.
        """
        self.bucket_size = bucket_size
        self.global_depth = 1
        # Initialize directory with 2^global_depth entries
        self.directory = [Bucket(bucket_size, 1) for _ in range(2)]
    
    def _hash(self, key: int) -> int:
        return key
    
    def _get_bucket_index(self, key: int) -> int:
        hash_value = self._hash(key)
        # Use only the last global_depth bits
        mask = (1 << self.global_depth) - 1
        return hash_value & mask
    
    def _split_bucket(self, bucket: Bucket, bucket_idx: int):
        if bucket.local_depth == self.global_depth:
            self._double_directory()
        
        # Get all entries from the old bucket
        old_entries = bucket.get_all_entries()
        
        # Increase local depth
        old_local_depth = bucket.local_depth
        new_local_depth = old_local_depth + 1
        
        # Create two new buckets with increased local depth
        bucket0 = Bucket(self.bucket_size, new_local_depth)
        bucket1 = Bucket(self.bucket_size, new_local_depth)
        
        # Redistribute entries based on the new bit
        for key, value in old_entries.items():
            hash_value = self._hash(key)
            # Check the bit at position old_local_depth
            bit = (hash_value >> old_local_depth) & 1
            if bit == 0:
                bucket0.insert(key, value)
            else:
                bucket1.insert(key, value)
        
        # Update directory pointers
        # Find all directory entries pointing to the old bucket
        step = 1 << new_local_depth
        for i in range(len(self.directory)):
            if self.directory[i] is bucket:
                # Check which new bucket this directory entry should point to
                bit = (i >> old_local_depth) & 1
                if bit == 0:
                    self.directory[i] = bucket0
                else:
                    self.directory[i] = bucket1
    
    def _double_directory(self):
        """Double the size of the directory by duplicating all pointers."""
        self.global_depth += 1
        # Duplicate the directory
        self.directory = self.directory + self.directory.copy()
    
    def insert(self, key: int, value: int):
        bucket_idx = self._get_bucket_index(key)
        bucket = self.directory[bucket_idx]
        
        # Try to insert
        if bucket.insert(key, value):
            return  # Insertion successful
        
        # Bucket is full, need to split
        self._split_bucket(bucket, bucket_idx)
        
        # Retry insertion after split
        self.insert(key, value)
    
    def search(self, key: int) -> int:
        bucket_idx = self._get_bucket_index(key)
        bucket = self.directory[bucket_idx]
        return bucket.search(key)
    
    def remove(self, key: int) -> bool:
        bucket_idx = self._get_bucket_index(key)
        bucket = self.directory[bucket_idx]
        
        result = bucket.remove(key)
        
        if result:
            # Try to merge buckets if they're underfull
            self._try_merge(bucket_idx)
        
        return result
    
    def _try_merge(self, bucket_idx: int):
        bucket = self.directory[bucket_idx]
        
        # Can't merge if local depth is already at minimum
        if bucket.local_depth <= 1:
            return
        
        # Find sibling bucket index (flip the bit at position local_depth-1)
        sibling_idx = bucket_idx ^ (1 << (bucket.local_depth - 1))
        
        # Check if sibling exists and is within directory bounds
        if sibling_idx >= len(self.directory):
            return
        
        sibling = self.directory[sibling_idx]
        
        # Can only merge if both buckets have same local depth
        if bucket.local_depth != sibling.local_depth:
            return
        
        # Check if merged bucket would fit in one bucket
        total_entries = len(bucket.entries) + len(sibling.entries)
        if total_entries > self.bucket_size:
            return
        
        # Merge: create new bucket with decreased local depth
        merged_bucket = Bucket(self.bucket_size, bucket.local_depth - 1)
        
        # Copy all entries
        for key, value in bucket.get_all_entries().items():
            merged_bucket.insert(key, value)
        for key, value in sibling.get_all_entries().items():
            merged_bucket.insert(key, value)
        
        # Update all directory pointers that pointed to either bucket
        for i in range(len(self.directory)):
            if self.directory[i] is bucket or self.directory[i] is sibling:
                self.directory[i] = merged_bucket
    
    def display(self):
        print(f"\n{'='*60}")
        print(f"Extensible Hash Structure")
        print(f"{'='*60}")
        print(f"Global Depth: {self.global_depth}")
        print(f"Directory Size: {len(self.directory)}")
        print(f"Bucket Size: {self.bucket_size}")
        print(f"{'='*60}\n")
        
        # Track unique buckets to avoid displaying duplicates
        displayed_buckets = set()
        
        print("Directory Mapping:")
        print(f"{'Index':<10} {'Binary':<15} {'Bucket ID':<12} {'Local Depth':<15} {'Entries'}")
        print("-" * 80)
        
        for i, bucket in enumerate(self.directory):
            bucket_id = id(bucket)
            binary = format(i, f'0{self.global_depth}b')
            
            # Show directory entry
            entries_str = str(dict(list(bucket.entries.items())[:3]))
            if len(bucket.entries) > 3:
                entries_str = entries_str[:-1] + ", ...}"
            
            marker = " *" if bucket_id not in displayed_buckets else ""
            print(f"{i:<10} {binary:<15} {bucket_id:<12} {bucket.local_depth:<15} {entries_str}{marker}")
            
            displayed_buckets.add(bucket_id)
        
        print("\n" + "="*60)
        print(f"Unique Buckets: {len(displayed_buckets)}")
        print("="*60 + "\n")
        
        # Display detailed bucket information
        displayed_buckets_detail = set()
        bucket_num = 0
        
        print("\nDetailed Bucket Contents:")
        print("="*60)
        
        for i, bucket in enumerate(self.directory):
            bucket_id = id(bucket)
            if bucket_id not in displayed_buckets_detail:
                print(f"\nBucket #{bucket_num} (ID: {bucket_id})")
                print(f"  Local Depth: {bucket.local_depth}")
                print(f"  Capacity: {len(bucket.entries)}/{self.bucket_size}")
                print(f"  Entries: {bucket.entries if bucket.entries else 'Empty'}")
                
                # Show which directory indices point to this bucket
                indices = [idx for idx, b in enumerate(self.directory) if id(b) == bucket_id]
                indices_str = ", ".join([f"{idx}({format(idx, f'0{self.global_depth}b')})" for idx in indices])
                print(f"  Directory Indices: {indices_str}")
                
                displayed_buckets_detail.add(bucket_id)
                bucket_num += 1
        
        print("\n" + "="*60 + "\n")