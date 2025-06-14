
def run_qa_checks(data):
    results = []

    # Sample logic for 5 of the 30 questions
    if "invert level" not in data.get("notes", "").lower():
        results.append({
            "question": 1,
            "result": "❌ FAIL",
            "explanation": "Invert levels not found in drawing notes",
            "suggested_action": "Add cover/invert levels at each MH"
        })
    else:
        results.append({"question": 1, "result": "✅ PASS"})

    if data["formats_received"] == "DXF":
        results.append({"question": 2, "result": "✅ PASS"})
    else:
        results.append({
            "question": 2,
            "result": "⚠️ FLAG",
            "explanation": "Only PDF received; some QA checks may be incomplete",
            "suggested_action": "Upload DXF version for CAD-level checks"
        })

    results.append({"question": 3, "result": "✅ PASS"})
    results.append({"question": 4, "result": "✅ PASS"})
    results.append({"question": 5, "result": "✅ PASS"})

    return results
