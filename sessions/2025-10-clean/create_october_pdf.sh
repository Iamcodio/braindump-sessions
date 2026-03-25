#!/bin/bash

# October 2025 Brain Dump Combined PDF Generator
# (No monthly report yet - month not complete)

echo "==================================="
echo "October 2025 PDF Generator"
echo "Daily sessions only (no monthly report)"
echo "==================================="

OUTPUT_DIR="/Users/kjd/09-personal/BrainDumpSessions/sessions/2025-10"
cd "$OUTPUT_DIR" || exit 1

# Remove old combined file if exists
rm -f 2025-10_brain_dump_combined.pdf

echo ""
echo "Step 1: Concatenating markdown files..."

# Start with header
echo "# Daily Brain Dump Sessions - October 2025" > /tmp/2025-10_combined.md
echo "" >> /tmp/2025-10_combined.md
echo "_Generated: $(date '+%Y-%m-%d %H:%M:%S')_" >> /tmp/2025-10_combined.md
echo "" >> /tmp/2025-10_combined.md
echo "**Note:** Monthly report will be added when October is complete." >> /tmp/2025-10_combined.md
echo "" >> /tmp/2025-10_combined.md

# Add all daily files in chronological order
for file in 2025-10-*_brain_dump_archive.md; do
    if [ -f "$file" ]; then
        echo "  - Adding: $file"
        echo "" >> /tmp/2025-10_combined.md
        echo "\\newpage" >> /tmp/2025-10_combined.md
        echo "" >> /tmp/2025-10_combined.md
        cat "$file" >> /tmp/2025-10_combined.md
    fi
done

echo ""
echo "Step 2: Converting to PDF with XeLaTeX..."
pandoc /tmp/2025-10_combined.md \
    -o "$OUTPUT_DIR/2025-10_brain_dump_combined.pdf" \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V documentclass=article

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS!"
    echo "Output: $OUTPUT_DIR/2025-10_brain_dump_combined.pdf"
    ls -lh "$OUTPUT_DIR/2025-10_brain_dump_combined.pdf"
else
    echo ""
    echo "❌ FAILED - check error messages above"
    exit 1
fi

echo ""
echo "==================================="
echo "COMPLETE!"
echo "==================================="
