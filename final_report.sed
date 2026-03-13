# FINAL REPORT GENERATION SCRIPT
# Author: Dr. Ozhan Akdag
# Description: Professional log scrubbing and reformatting

# 1. Remove Low Priority Data
/LEVEL: Low/d

# 2. Reformat ID to Issue Tracker Format (using Back-references)
s/ID-([0-9]+)/[ISSUE_#\1]/g

# 3. Label Sensitive Data: Mask SCAN_DATE and add Confidentiality tag
s/^SCAN_DATE: ([0-9\/]+)/\1 (CONFIDENTIAL)/

# 4. Range Processing: Transform text between START and END to UPPERCASE
/--- SCAN START ---/,/--- SCAN END ---/ {
    /--- SCAN (START|END) ---/! s/.*/\U&/
}