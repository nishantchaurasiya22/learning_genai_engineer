# How LLM (GPT) Works

## What is GPT
GPT = **G**enerative **P**re-trained **T**ransformer

LLM works on this GPT concept. It means:

1. LLM is trained on almost all the text data available on the internet
2. Inside it, there is a **Transformer architecture**
3. If a user talks about something where the same word can mean different items, the Transformer looks at the **surrounding/other words** to understand which item is actually being talked about (this is called understanding context)
4. Based on this understanding, the model also **predicts the next word**

## Flow of how LLM works

```
Step 1: Training
   LLM trained on huge internet text data

Step 2: Context Understanding (Transformer)
   Looks at surrounding words to understand
   which meaning/item is being talked about

Step 3: Next Word Prediction
   Based on the understanding, model predicts
   the next word, one word at a time
```

## Simple Summary
LLM works in this order:
**Training (knowledge) → Context Understanding (via Transformer) → Next Word Prediction**

First it gains knowledge from training data, then it understands the context of the current input using the Transformer, and finally it predicts the next word based on that understanding.

## My Understanding
GPT is not just predicting randomly — it first understands what is actually being asked (context), and only then generates the next word. That's why it doesn't get confused even when the same word can have different meanings.

