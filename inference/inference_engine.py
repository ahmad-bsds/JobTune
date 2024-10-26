API_KEY = "7e612080c6da0507f0886156df96f0db5bb3d36e5f0439a79cdd4ecbb38c3390"

import os
from together import Together

os.environ["TOGETHER_API_KEY"] = API_KEY

client = Together()

stream = client.chat.completions.create(
  model="meta-llama/Llama-Vision-Free",
  messages=[{"role": "user", "content": "What are some fun things to do in New York?"}],
  stream=True,
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="", flush=False)