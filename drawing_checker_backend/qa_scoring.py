def calculate_score(results):
    scores = {'PASS': 1.0, 'FLAG': 0.5, 'FAIL': 0.0}
    total = len(results)
    achieved = sum(scores.get(r['result'], 0) for r in results)
    return round((achieved / total) * 100, 1)
