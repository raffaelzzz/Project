
#!/bin/bash



for range in $(seq 1 254);
do
host 187.45.192.$range | grep -v "not found"
done
