from __future__ import annotations
versions={0:[{"id":"a","amount":10}],1:[{"id":"a","amount":10},{"id":"b","amount":20}],2:[{"id":"a","amount":12},{"id":"b","amount":20}]}
if __name__=="__main__":
 for version in sorted(versions):print(f"version={version}:",versions[version])
 print("Gerçek Delta Lake'de versionAsOf veya timestampAsOf ile geçmiş sürüm okunur.")
