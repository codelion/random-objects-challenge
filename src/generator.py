#!/usr/bin/env python3
import random
import string
import os
import sys
import time

def generate_alphabetical_string(min_length=1, max_length=20):
    """Generate a random alphabetical string with length between min_length and max_length."""
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_real_number():
    """Generate a random real number."""
    return f"{random.uniform(-10000, 10000):.6f}"

def generate_integer():
    """Generate a random integer."""
    return str(random.randint(-10000, 10000))

def generate_alphanumeric_with_spaces(min_length=1, max_length=20):
    """Generate a random alphanumeric string with random spaces before and after."""
    length = random.randint(min_length, max_length)
    alphanumeric = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    spaces_before = ' ' * random.randint(0, 10)
    spaces_after = ' ' * random.randint(0, 10)
    return f"{spaces_before}{alphanumeric}{spaces_after}"

def generate_file(filename, target_size_mb=10):
    """Generate a file with random objects separated by commas, aiming for the target size."""
    target_size_bytes = target_size_mb * 1024 * 1024
    buffer_size = 1024 * 1024  # 1MB buffer
    
    start_time = time.time()
    
    with open(filename, 'w') as f:
        current_size = 0
        objects_generated = 0
        buffer = ""
        
        while current_size < target_size_bytes:
            # Generate a random object
            object_type = random.randint(1, 4)
            
            if object_type == 1:
                obj = generate_alphabetical_string()
            elif object_type == 2:
                obj = generate_real_number()
            elif object_type == 3:
                obj = generate_integer()
            else:
                obj = generate_alphanumeric_with_spaces()
            
            # Add comma if not the first object
            if objects_generated > 0:
                buffer += ","
                current_size += 1
            
            buffer += obj
            current_size += len(obj.encode('utf-8'))
            objects_generated += 1
            
            # Write buffer to file if it's large enough
            if len(buffer) >= buffer_size:
                f.write(buffer)
                buffer = ""
            
            # Print progress
            if objects_generated % 10000 == 0:
                progress = min(100, int(current_size * 100 / target_size_bytes))
                elapsed_time = time.time() - start_time
                sys.stdout.write(f"\rGenerating... {progress}% complete ({current_size / (1024 * 1024):.2f} MB) - {objects_generated} objects - {elapsed_time:.1f}s elapsed")
                sys.stdout.flush()
        
        # Write any remaining buffer
        if buffer:
            f.write(buffer)
    
    # Get final file size
    final_size = os.path.getsize(filename)
    elapsed_time = time.time() - start_time
    print(f"\nGenerated file {filename} with size {final_size / (1024 * 1024):.6f} MB in {elapsed_time:.2f} seconds")
    print(f"Total objects generated: {objects_generated}")

if __name__ == "__main__":
    output_file = "random_objects.txt"
    
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    
    size_mb = 10
    if len(sys.argv) > 2:
        size_mb = float(sys.argv[2])
    
    generate_file(output_file, size_mb)
