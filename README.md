Hadoop mapreduce on githubdata
---

This holds the map reduce jobs for the analysis done on github data





**Note:**

1. To see the successful job resluts please go into folder by name 'performance'

2. The requests.get('http://master:5000/Credentials') in github-mapper.py is done to tackle the API ratelimit of 5000 that github enforces on users. Basicallu I have a rest server(using python flask) running there which serves map jobs with username and password once the API ratelimit is reached .

**Command:**

bin/hadoop jar contrib/streaming/hadoop-streaming-1.0.3.jar -file {mapper-file} -mapper {mapper-file} -file {reducer-file} -reducer {reducer-file}  -input {input-file} -output {output-dfs-directory}
