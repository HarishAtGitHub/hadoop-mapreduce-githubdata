Hadoop MapReduce on GitHub data
---

This holds the MapReduce jobs for the analysis done on GitHub data





**Note:**

1. To see the successful job results please go into folder by name 'performance'

2. The requests.get('http://master:5000/Credentials') in github-mapper.py is done to tackle the API rate limit of 5000 that GitHub enforces on users. Basically, I have a rest server(using python flask) running, which does authentication renewal once the API rate limit is reached .

**Command:**

bin/hadoop jar contrib/streaming/hadoop-streaming-1.0.3.jar -file {mapper-file} -mapper {mapper-file} -file {reducer-file} -reducer {reducer-file}  -input {input-file} -output {output-dfs-directory}
