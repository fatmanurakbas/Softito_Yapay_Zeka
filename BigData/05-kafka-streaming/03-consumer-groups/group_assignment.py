"""Round-robin partition ataması örneği."""
from __future__ import annotations
def assign(partitions:list[int],consumers:list[str])->dict[str,list[int]]:
 result={consumer:[] for consumer in consumers}
 for index,partition in enumerate(partitions):result[consumers[index%len(consumers)]].append(partition)
 return result
if __name__=="__main__":
 print(assign(list(range(7)),["consumer-a","consumer-b","consumer-c"]));print("Bir partition aynı consumer group içinde yalnızca bir consumer tarafından okunur.")
