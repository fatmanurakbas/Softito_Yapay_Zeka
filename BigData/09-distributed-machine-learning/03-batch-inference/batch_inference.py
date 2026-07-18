from __future__ import annotations
def score(row):return round(min(1,max(0,.15*row["events"]+.3*row["amount"])),3)
if __name__=="__main__":
 rows=[{"customer":"u1","events":3,"amount":.5},{"customer":"u2","events":0,"amount":.1}]
 output=[{**row,"score":score(row),"model_version":"v1","feature_version":"2026-01"} for row in rows];print(output)
