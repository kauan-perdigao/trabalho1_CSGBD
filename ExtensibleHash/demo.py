"""
Author: Gabriel Viana

Desenvolvido com ajuda de LLM (copilot)
"""

from ExtensibleHash import ExtensibleHash


def test_basic_operations():
    """Test basic insert, search, and display operations."""
    print("\n" + "="*70)
    print("TEST 1: Basic Operations (Insert and Search)")
    print("="*70)
    
    # Create hash with bucket size of 2
    eh = ExtensibleHash(bucket_size=2)
    
    # Insert some key-value pairs
    print("\nInserting keys: 1, 2, 3, 4...")
    eh.insert(1, 100)
    eh.insert(2, 200)
    eh.insert(3, 300)
    eh.insert(4, 400)
    
    eh.display()
    
    # Search for keys
    print("\nSearching for keys:")
    for key in [1, 2, 3, 4, 5]:
        result = eh.search(key)
        print(f"  Key {key}: {result if result is not None else 'Not found'}")


def test_bucket_split():
    """Test bucket splitting and directory doubling."""
    print("\n" + "="*70)
    print("TEST 2: Bucket Split and Directory Doubling")
    print("="*70)
    
    eh = ExtensibleHash(bucket_size=2)
    
    print("\nInserting keys to trigger splits: 0, 2, 4, 6, 8, 10...")
    keys = [0, 2, 4, 6, 8, 10]
    for key in keys:
        print(f"\n--- Inserting key {key} ---")
        eh.insert(key, key * 10)
        eh.display()


def test_removal_and_merge():
    """Test removal operations and bucket merging."""
    print("\n" + "="*70)
    print("TEST 3: Removal and Bucket Merging")
    print("="*70)
    
    eh = ExtensibleHash(bucket_size=3)
    
    # Insert keys
    print("\nInserting keys: 1-10...")
    for i in range(1, 11):
        eh.insert(i, i * 100)
    
    eh.display()
    
    # Remove some keys
    print("\nRemoving keys: 2, 4, 6, 8...")
    for key in [2, 4, 6, 8]:
        result = eh.remove(key)
        print(f"  Removed key {key}: {result}")
    
    eh.display()
    
    # Search after removal
    print("\nSearching after removal:")
    for key in [1, 2, 3, 4, 5]:
        result = eh.search(key)
        print(f"  Key {key}: {result if result is not None else 'Not found'}")


def test_random_sequence():
    """Test with a more complex random-like sequence."""
    print("\n" + "="*70)
    print("TEST 4: Complex Sequence (Simulating Real Usage)")
    print("="*70)
    
    eh = ExtensibleHash(bucket_size=2)
    
    # Insert sequence suggested in requirements (1-50 in some order)
    test_keys = [15, 7, 23, 4, 11, 30, 19, 2, 45, 8, 
                 33, 12, 27, 50, 6, 41, 18, 3, 36, 25]
    
    print(f"\nInserting keys: {test_keys[:10]}...")
    for key in test_keys[:10]:
        eh.insert(key, key * 10)
    
    eh.display()
    
    print(f"\nInserting more keys: {test_keys[10:]}...")
    for key in test_keys[10:]:
        eh.insert(key, key * 10)
    
    eh.display()
    
    # Test searches
    print("\nSearching for some keys:")
    search_keys = [15, 7, 100, 23, 99, 45]
    for key in search_keys:
        result = eh.search(key)
        status = f"Found: {result}" if result is not None else "Not found"
        print(f"  Key {key}: {status}")
    
    # Remove some keys
    print("\nRemoving keys: [15, 7, 23, 4, 11]...")
    for key in [15, 7, 23, 4, 11]:
        eh.remove(key)
    
    eh.display()


def test_update_values():
    """Test updating existing keys."""
    print("\n" + "="*70)
    print("TEST 5: Updating Values")
    print("="*70)
    
    eh = ExtensibleHash(bucket_size=3)
    
    print("\nInserting keys 1-5...")
    for i in range(1, 6):
        eh.insert(i, i * 100)
    
    print("\nBefore update:")
    for i in range(1, 6):
        print(f"  Key {i}: {eh.search(i)}")
    
    print("\nUpdating key 3 to new value 999...")
    eh.insert(3, 999)  # Update existing key
    
    print("\nAfter update:")
    for i in range(1, 6):
        print(f"  Key {i}: {eh.search(i)}")
    
    eh.display()


def main():
    """Run all tests."""
    print("\n" + "#"*70)
    print("# EXTENSIBLE HASH - DEMONSTRATION AND TESTS")
    print("# Author: Gabriel Viana")
    print("# Course: CSGBD - UFC")
    print("#"*70)
    
    test_basic_operations()
    test_bucket_split()
    test_removal_and_merge()
    test_random_sequence()
    test_update_values()
    
    print("\n" + "#"*70)
    print("# ALL TESTS COMPLETED")
    print("#"*70 + "\n")


if __name__ == "__main__":
    main()
