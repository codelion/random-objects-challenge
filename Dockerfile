FROM python:3.9-slim

WORKDIR /app

# Copy the processor script
COPY src/processor.py .

# Create volumes for input and output
VOLUME ["/app/input", "/app/output"]

# Set environment variables with defaults that can be overridden
ENV INPUT_FILE=/app/input/random_objects.txt
ENV OUTPUT_FILE=/app/output/results.txt

# Run the processor script when the container starts
CMD ["sh", "-c", "python processor.py ${INPUT_FILE} ${OUTPUT_FILE}"]
