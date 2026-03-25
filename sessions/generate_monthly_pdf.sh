#!/bin/bash

# ============================================================================
# BRAIN DUMP MONTHLY PDF GENERATOR
# Bell Labs Style: Do One Thing Right
# Handles both naming conventions: _monthly_report.md and _monthly_report_text.md
#
# FIRST TIME SETUP:
#   chmod +x generate_monthly_pdf.sh
#
# USAGE:
#   ./generate_monthly_pdf.sh 2025-09
#   ./generate_monthly_pdf.sh 2025-10
#
# OR WITHOUT CHMOD:
#   bash generate_monthly_pdf.sh 2025-09
# ============================================================================

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║           BRAIN DUMP MONTHLY PDF GENERATOR                    ║"
echo "║                                                               ║"
echo "║   Bell Labs Philosophy: Do One Thing, Do It Right            ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Check for month parameter
if [ -z "$1" ]; then
    echo "❌ Error: Month parameter required"
    echo ""
    echo "Usage: $0 YYYY-MM"
    echo "Example: $0 2025-10"
    echo ""
    exit 1
fi

MONTH=$1
BASE_DIR="/Users/kjd/09-personal/BrainDumpSessions/sessions"
WORK_DIR="$BASE_DIR/${MONTH}-clean"

echo "📅 Processing month: $MONTH"
echo "📁 Working directory: $WORK_DIR"
echo ""

# Step 1: Create clean working copy
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 1: Creating clean working copy"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

cd "$BASE_DIR" || exit 1
rm -rf "${MONTH}-clean"
cp -r "$MONTH" "${MONTH}-clean"
cd "$WORK_DIR" || exit 1

echo "✓ Clean copy created"
echo ""

# Step 2: Find and strip all emojis
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 2: Stripping all emojis"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Comprehensive emoji list from all testing
for file in *.md; do 
    sed 's/🎨//g; s/🧠//g; s/💰//g; s/💥//g; s/📈//g; s/📊//g; s/👥//g; s/✅//g; s/≈//g; s/↔//g; s/🌊//g; s/🎓//g; s/🎯//g; s/🏠//g; s/💡//g; s/💼//g; s/📄//g; s/📍//g; s/📝//g; s/🔗//g; s/🚧//g; s/🔮//g; s/🎤//g; s/🔥//g; s/🔄//g; s/🐉//g; s/🚀//g; s/≠//g; s/✓//g; s/❌//g; s/📅//g' "$file" > temp.md && mv temp.md "$file"
done

EMOJI_COUNT=$(cat *.md | hexdump -C | grep "f0 9f" | wc -l | tr -d ' ')

if [ "$EMOJI_COUNT" -eq 0 ]; then
    echo "✓ All emojis removed (verified: 0 remaining)"
else
    echo "⚠️  Warning: $EMOJI_COUNT emoji bytes still detected"
fi
echo ""

# Step 3: Combine files
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 3: Combining markdown files"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Find the monthly report file (handle both naming conventions)
if [ -f "${MONTH}_monthly_report.md" ]; then
    REPORT_FILE="${MONTH}_monthly_report.md"
    echo "  → Found standard format: ${REPORT_FILE}"
elif [ -f "${MONTH}_monthly_report_text.md" ]; then
    REPORT_FILE="${MONTH}_monthly_report_text.md"
    echo "  → Found alternate format: ${REPORT_FILE}"
else
    echo "❌ Error: No monthly report found"
    echo "   Expected: ${MONTH}_monthly_report.md or ${MONTH}_monthly_report_text.md"
    exit 1
fi

# Start with monthly report
cat "$REPORT_FILE" > ${MONTH}_combined.md
echo "" >> ${MONTH}_combined.md
echo "---" >> ${MONTH}_combined.md
echo "" >> ${MONTH}_combined.md
echo "# Daily Brain Dump Sessions - $(date -j -f "%Y-%m" "$MONTH" "+%B %Y")" >> ${MONTH}_combined.md
echo "" >> ${MONTH}_combined.md

echo "  → Monthly report added first (executive summary)"

# Append all daily files chronologically
for file in ${MONTH}-*_brain_dump_archive.md; do
    if [ -f "$file" ]; then
        echo "  → Adding: $file"
        echo "" >> ${MONTH}_combined.md
        echo "\\newpage" >> ${MONTH}_combined.md
        echo "" >> ${MONTH}_combined.md
        cat "$file" >> ${MONTH}_combined.md
    fi
done

echo "✓ All files combined"
echo ""

# Step 4: Convert to PDF
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 4: Converting to PDF with XeLaTeX"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

pandoc ${MONTH}_combined.md \
    -o ${MONTH}_brain_dump_combined.pdf \
    --pdf-engine=xelatex \
    -V geometry:margin=1in \
    -V fontsize=11pt \
    -V documentclass=article 2>&1 | grep -v "WARNING"

if [ -f "${MONTH}_brain_dump_combined.pdf" ]; then
    SIZE=$(ls -lh ${MONTH}_brain_dump_combined.pdf | awk '{print $5}')
    echo "✓ PDF generated successfully: $SIZE"
else
    echo "❌ PDF generation failed"
    exit 1
fi

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║                    ✓ MISSION ACCOMPLISHED                     ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "📄 Output: ${MONTH}_brain_dump_combined.pdf"
echo "📁 Location: $WORK_DIR"
echo ""

# EOF
# To make this script executable, run once: chmod +x generate_monthly_pdf.sh
