#!/bin/bash

echo "========================================="
echo "OCTOBER 2025 PDF GENERATOR"
echo "========================================="

cd /Users/kjd/09-personal/BrainDumpSessions/sessions/2025-10 || exit 1

# Remove old PDF if exists
rm -f 2025-10_brain_dump_combined.pdf

echo ""
echo "Step 1: Creating combined markdown..."

# Header
cat > /tmp/2025-10_combined.md << 'EOF'
# Daily Brain Dump Sessions - October 2025

**Generated:** $(date '+%Y-%m-%d %H:%M:%S')

**Note:** Month not yet complete - no monthly report included.

---

EOF

# Add all daily files
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
    -o 2025-10_brain_dump_combined.pdf \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V documentclass=article

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS!"
    ls -lh 2025-10_brain_dump_combined.pdf
else
    echo "❌ FAILED"
    exit 1
fi

echo ""
echo "========================================="
echo "COMPLETE!"
echo "========================================="
