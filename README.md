# Random Objects Generator and Processor

This project implements a solution for the software engineering challenge with three parts:

1. **Challenge A**: Generate 10MB of random objects of four different types, separated by commas
2. **Challenge B**: Process the generated file to identify and print each object's type
3. **Challenge C**: Dockerize Challenge B to read the file and save results to the host machine

## Project Overview

### Challenge A: Random Objects Generator

The generator creates a file containing four types of random objects:

1. **Alphabetical strings**: Random strings containing only letters (a-z, A-Z)
2. **Real numbers**: Random floating-point numbers (e.g., -8765.432109)
3. **Integers**: Random whole numbers (e.g., 42, -789)
4. **Alphanumerics with spaces**: Random strings with letters and numbers, with 0-10 spaces before and after

These objects are separated by commas, and the output file is 10MB in size by default.

### Challenge B: Objects Processor

The processor:
- Reads the file generated in Challenge A
- Identifies the type of each object using regex patterns
- Prints each object and its type to the console
- Strips spaces before and after alphanumeric objects as required
- Provides a summary of object type counts and percentages

### Challenge C: Dockerized Processor

A Docker container that:
- Takes the generated file as input through a volume mount
- Runs the processor from Challenge B
- Saves the output to a file accessible from the host machine
- Configurable through environment variables

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Docker and Docker Compose (for Challenge C)

### Project Structure

```
random-objects-challenge/
├── README.md                # This documentation
├── src/
│   ├── generator.py         # Challenge A: Random objects generator
│   └── processor.py         # Challenge B: Object type processor
├── Dockerfile               # Challenge C: Docker configuration
└── docker-compose.yml       # For easier Docker execution
```

### Running Challenge A: Generate Random Objects

```bash
# Create a 10MB file of random objects
python src/generator.py

# Optionally specify filename and size (in MB)
python src/generator.py random_objects.txt 10
```

The generator will create a file with the specified name (default: `random_objects.txt`) containing random objects separated by commas. Progress information will be displayed during generation.

### Running Challenge B: Process the Generated File

```bash
# Process the file and print results to console
python src/processor.py random_objects.txt

# Save results to a file
python src/processor.py random_objects.txt results.txt
```

The processor will:
1. Read the input file
2. Identify the type of each object
3. Print the object and its type
4. Display a summary of object types
5. Save the results to the specified output file (if provided)

### Running Challenge C: Dockerized Processing

1. Create necessary directories:

```bash
mkdir -p data output
```

2. Place the generated file in the data directory:

```bash
cp random_objects.txt data/
```

3. Run the Docker container:

```bash
# Using Docker Compose (recommended)
docker-compose up

# Or directly with Docker
docker build -t random-objects-processor .
docker run -v $(pwd)/data:/app/input -v $(pwd)/output:/app/output random-objects-processor
```

4. Check the results:

```bash
cat output/results.txt
```

## Implementation Details

### Generator (Challenge A)

The generator uses:
- Random string generation with configurable length
- Buffered file writing for efficiency
- Progress tracking during generation
- Consistent distribution of the four object types

### Processor (Challenge B)

The processor uses regex patterns to identify object types:
- `^-?\d+$` identifies Integers
- `^-?\d+\.\d+$` identifies Real Numbers
- `^[a-zA-Z]+$` identifies Alphabetical Strings
- `^\s*[a-zA-Z0-9]+\s*$` identifies Alphanumerics (with spaces that get stripped)

### Docker Container (Challenge C)

The Docker implementation:
- Uses a lightweight Python image
- Maps volumes for input and output
- Provides configurable environment variables
- Processes the input file and saves results to the output volume

## Performance Considerations

- The generator uses buffered writing to improve performance when creating large files
- The processor loads the entire file into memory, which is appropriate for the 10MB file size
- For extremely large files, a streaming approach could be implemented
- Progress tracking is provided for both generation and processing

## Extension Ideas

If you want to extend this project, consider:
1. Adding more object types
2. Implementing streaming processing for very large files
3. Adding a web interface to visualize the results
4. Enhancing statistics and analysis of the generated data
