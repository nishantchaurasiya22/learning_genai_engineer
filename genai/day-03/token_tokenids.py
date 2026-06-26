import tiktoken
text="who is the prime minister of india"
tokenizer=tiktoken.encoding_for_model(model_name="gpt-4")
tokenIds=tokenizer.encode(text)

resultsId=tokenIds
print(resultsId)

result=tokenizer.decode(resultsId)
print(result)