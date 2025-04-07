#!/usr/bin/env python3
import re
import sys
import os
import time

def identify_object_type(obj):
    """Identify the type of the given object."""
    original_obj = obj
    obj = obj.strip()  # Strip spaces for identification
    
    # Check if it's an integer
    if re.match(r'^-?\d+$', obj):
        return obj, "Integer"
    
    # Check if it's a real number
    if re.match(r'^-?\d+\.\d+$', obj):
        return obj, "Real Number"
    
    # Check if it's an alphabetical string
    if re.match(r'^[a-zA-Z]+$', obj):
        return obj, "Alphabetical String"
    
    # Check if it's alphanumeric (with possible spaces before/after)
    if re.match(r'^\s*[a-zA-Z0-9]+\s*$', original_obj):
        # Strip spaces for alphanumerics as required
        return obj, "Alphanumeric"
    
    return obj, "Unknown"

def process_file(input_filename, output_filename=None):
    """Process the file, identify object types, and print or save results."""
    if not os.path.exists(input_filename):
        print(f"Error: Input file {input_filename} not found.")
        return
    
    try:
        start_time = time.time()
        
        # Read the file content
        print(f"Reading file {input_filename}...")
        with open(input_filename, 'r') as f:
            content = f.read()
        
        read_time = time.time() - start_time
        print(f"File read in {read_time:.2f} seconds.")
        
        # Split by commas
        objects = content.split(',')
        total_objects = len(objects)
        
        print(f"Processing {total_objects} objects...")
        process_start = time.time()
        
        results = []
        object_counts = {
            "Integer": 0,
            "Real Number": 0,
            "Alphabetical String": 0,
            "Alphanumeric": 0,
            "Unknown": 0
        }
        
        for i, obj in enumerate(objects):
            if not obj:  # Skip empty objects
                continue
            
            processed_obj, obj_type = identify_object_type(obj)
            result_line = f"Object: {processed_obj}, Type: {obj_type}"
            print(result_line)
            results.append(result_line)
            
            # Count object types
            object_counts[obj_type] += 1
            
            # Show progress
            if (i + 1) % 1000 == 0 or i + 1 == total_objects:
                progress = min(100, int((i + 1) * 100 / total_objects))
                elapsed = time.time() - process_start
                sys.stdout.write(f"\rProgress: {progress}% ({i + 1}/{total_objects}) - {elapsed:.1f}s elapsed")
                sys.stdout.flush()
        
        process_time = time.time() - process_start
        total_time = time.time() - start_time
        
        print("\nProcessing complete!")
        print(f"Processing time: {process_time:.2f} seconds")
        print(f"Total execution time: {total_time:.2f} seconds")
        
        # Print summary of object types
        print("\nObject Type Summary:")
        for obj_type, count in object_counts.items():
            percentage = (count / total_objects) * 100 if total_objects > 0 else 0
            print(f"  {obj_type}: {count} ({percentage:.1f}%)")
        
        # Save to output file if specified
        if output_filename:
            print(f"Saving results to {output_filename}...")
            with open(output_filename, 'w') as f:
                f.write('\n'.join(results))
            print(f"Results saved successfully.")
    
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python processor.py input_file [output_file]")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else None
    
    process_file(input_filename, output_filename)
