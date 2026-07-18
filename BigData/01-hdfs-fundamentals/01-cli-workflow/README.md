# 01 — HDFS CLI Pratiği

Çalışan HDFS ortamında sırasıyla aşağıdaki komutları deneyin. Her komuttan sonra `-ls` ile sonucu kontrol edin.

```bash
hdfs dfs -mkdir -p /user/$USER/bigdata-lab/input
hdfs dfs -put local-data.txt /user/$USER/bigdata-lab/input/
hdfs dfs -ls /user/$USER/bigdata-lab/input
hdfs dfs -cat /user/$USER/bigdata-lab/input/local-data.txt
hdfs dfs -du -h /user/$USER/bigdata-lab
hdfs dfs -get /user/$USER/bigdata-lab/input/local-data.txt downloaded.txt
```

Ek alıştırma: dosyayı kopyalayın, yeniden adlandırın ve yalnızca kendi laboratuvar yolunuzu silerek temizleyin. Paylaşılan veya kök HDFS yollarında silme işlemi yapmayın.
