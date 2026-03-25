#!/bin/bash
# Concatenate all January 2026 brain dump archives into one file

OUTPUT_FILE="/Users/kjd/09-personal/BrainDumpSessions/sessions/2026-01/january_2026_concatenated.md"

# Clear/create output file
echo "# January 2026 - All Brain Dump Sessions" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Generated: $(date)" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Concatenate all archives in chronological order
for file in /Users/kjd/09-personal/BrainDumpSessions/sessions/2026-01/2026-01-*.md; do
    if [ -f "$file" ]; then
        echo "" >> "$OUTPUT_FILE"
        echo "---" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
        cat "$file" >> "$OUTPUT_FILE"
    fi
done

echo "Concatenation complete: $OUTPUT_FILE"
