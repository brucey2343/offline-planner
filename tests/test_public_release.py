"""Verify public release privacy, offline operation and identical app copies."""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
html=(root/"planner.html").read_bytes()
copy=(root/"dist"/"Offline_Planner_Email_as_TXT.txt").read_bytes()
assert html==copy, "HTML/TXT application mismatch"
source=html.decode("utf-8")
assert len(html)>100_000 and source.lstrip().startswith("<!DOCTYPE html>")
assert source.rstrip().endswith("</html>")
for phrase in ("<title>Offline Planner</title>", "How to use Offline Planner", "offline_planner_", "work-life-planner-transfer", "WORK_LIFE_OFFLINE_PLANNER_V1", "WLP-BASE64-V1", "LOW PRIORITY", "LOW ENERGY"):
    assert phrase in source, "Required generic branding or compatibility marker missing"
assert not re.search(r"<script[^>]+src\s*=|<link[^>]+href\s*=|<iframe\b",source,re.I)
assert not re.search(r"\bfetch\s*\(|\bXMLHttpRequest\b|\bWebSocket\b",source)
assert not re.search(r"https?://",source), "External address in application"
assert not re.search(r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}",source), "Email address in application"
assert not re.search(r"\b(?:192\.168\.|10\.\d+\.\d+\.|100\.\d+\.\d+\.)\d+",source), "Private IP address in application"
assert not re.search(r"\b[A-Z][a-z]{2,}'s Planner\b",source), "Personalised app title"
for path in root.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    assert path.suffix.lower() not in (".db",".sqlite",".sqlite3",".bundle",".zip")
    assert not (path.suffix.lower()==".txt" and path.name!="Offline_Planner_Email_as_TXT.txt"), "Unexpected data file"
print("Public release checks passed: anonymous source, no network references, compatible backups, identical HTML/TXT")
