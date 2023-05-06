# Test task
Simple & slow proxy without hop-by-hop headers replacement which performs TMization of the HTML's contents

**To run**
- `docker build --tag proxyhn .`
- `docker run -d -p 8000:8000 --name proxyhn proxyhn`
- visit **localhost:8000/news**
