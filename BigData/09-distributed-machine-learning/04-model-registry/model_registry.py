from __future__ import annotations
models=[{"version":"v1","stage":"Production","metric":.81},{"version":"v2","stage":"Staging","metric":.84}]
if __name__=="__main__":
 for model in models:print(model)
 candidate=max(models,key=lambda item:item["metric"]);print("Promotion adayı:",candidate["version"],"| önce bias, gecikme ve geri alma planını kontrol edin.")
