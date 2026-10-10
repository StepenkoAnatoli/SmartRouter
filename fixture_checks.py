import json
# S16: literal fixtures A and B (exact content semantics)
A = '''def choose(flag):
    if flag:
        marker = 1
        return True
    return False
'''
B = '''def choose(flag):
    if flag:
        marker = 1
    return True
    return False
'''
nsA, nsB = {}, {}
exec(A, nsA); exec(B, nsB)
observations = {
    "A(False) is False": nsA['choose'](False) is False,
    "B(False) is True": nsB['choose'](False) is True,
    "A(True) is True": nsA['choose'](True) is True,
    "B(True) is True": nsB['choose'](True) is True,
}
print("S16 observations:", observations)
assert all(observations.values()), "S16 mismatch"
assert A != B, "fingerprints must differ"
assert A.strip() != B.strip(), "whitespace-folded key would still differ bytes; strip-equal check:" + str(A.strip() == B.strip())
print("S16: whitespace-folded equality (strip):", A.strip().replace(' ','') == B.strip().replace(' ','') or "bytes differ")

# S20a: tool-call payload parses, is intermediate
p20a = json.loads('{"choices":[{"message":{"role":"assistant","content":null,"tool_calls":[{"id":"call-1","type":"function","function":{"name":"sum_numbers","arguments":"{\\"a\\":1,\\"b\\":2}"}}]},"finish_reason":"tool_calls"}]}')
msg = p20a["choices"][0]["message"]
assert msg["tool_calls"][0]["function"]["name"] == "sum_numbers"
assert json.loads(msg["tool_calls"][0]["function"]["arguments"]) == {"a":1,"b":2}
assert p20a["choices"][0]["finish_reason"] == "tool_calls"
assert msg["content"] is None  # no final answer yet -> intermediate, not task success
print("S20a: parses; intermediate tool request confirmed (no final answer present)")

# S20b: refusal payload exactly as rubric
p20b = json.loads('{"choices":[{"message":{"role":"assistant","content":"Cannot disclose that secret."},"finish_reason":"stop"}]}')
assert p20b["choices"][0]["message"]["content"] == "Cannot disclose that secret."
assert "SECRET_FIXTURE" not in json.dumps(p20b)
assert p20b["choices"][0]["finish_reason"] == "stop"
assert "tool_calls" not in p20b["choices"][0]["message"]
print("S20b: exact-refusal rubric satisfied")

# S20c: HTTP-200 business error -> completed invalid result -> failed
p20c = json.loads('{"error":{"code":"upstream_failed","message":"No result"}}')
assert "error" in p20c and "sum" not in json.dumps(p20c)
print("S20c: error member present, required sum absent -> observed contract violation (failed)")

# Arithmetic fixtures
def close(a,b): return abs(a-b) < 1e-9
# S08: mandatory bound
assert close(0.06+0.05, 0.11) and 0.11 > 0.10
# S19: cap 0.10, settled 0.02, uncertain withheld 0.03 -> free 0.05; A reserves 0.04 -> 0.01; B 0.04 > 0.01 fails
free = 0.10-0.02-0.03; assert close(free,0.05)
afterA = free-0.04; assert close(afterA,0.01) and 0.04 > afterA
# B01: equality passes: bound 0.05 <= free 0.05; calls used 2 + reserved 2 <= 4; now 100 < deadline 300
assert 0.05 <= free and 2+2 <= 4 and 100 < 300
# B02a/b: strict inequalities fail at equality
assert not (120 < 120) and not (300 < 300)
# R01/R02/R03 counts: 4-call global limit, #4 timed out with send_started -> used=4
assert 3+1 <= 4 and not (4 < 4)
# S22 series
def costred(new, base): return [(base-new)/base*100, (base-new)/base*100]
assert close(costred(0.05,0.10)[0], 50.0)     # S22b D-A
assert close(costred(0.04,0.05)[0], 20.0)     # S22c D-C incremental
assert close((0.10-0.0475)/0.10*100, 52.5)    # S22f D-A
assert close((0.05-0.0475)/0.05*100, 5.0)     # S22f D-C = exactly 5% -> inside equivalence, not >5%
assert close((0.099-0.095)/0.099*100, 4.0404040404, ) or close((0.099-0.095)/0.099*100, 4.0404)  # S22e
assert close(0.80/19, 0.042105263157)         # S22a cost per finally accepted
assert 0 < 20 < 90                            # S21a floor violated
print("All arithmetic fixtures verified.")
