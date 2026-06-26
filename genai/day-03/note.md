# How Tokenization Works in LLM

## What is Tokenization
Tokenization means breaking text into small pieces called **tokens**, then turning each token into a number (**token ID**) so the LLM can use it. At the end, the output numbers are turned back into text.

LLM cannot read normal text or words. It can only work with **numbers**. Tokenization is the step that turns text into numbers, and later turns numbers back into text.

## Flow of how Tokenization works

```
Step 1: Input Text
   "who is prime minister of india"

Step 2: Tokenization (breaking into small pieces)
   Text is broken into tokens. These pieces are
   NOT always full words. Easy/common words stay
   whole, but long or rare words get cut into parts.
   Example: ["who", "is", "prim", "##e", "minister", "of", "india"]

Step 3: Token IDs (using a Vocabulary list)
   Every token is matched to a number using a
   fixed list called Vocabulary. This list is made
   during training, not a normal word dictionary.
   Example: [1023, 318, 4521, 68, 6390, 286, 9871]

Step 4: Embeddings
   Each number is changed into a long list of
   decimal numbers (called a vector). This vector
   carries the MEANING of that token. This is what
   actually goes inside the Transformer.

Step 5: Model Processing
   Transformer looks at all these vectors and
   guesses which token should come next.

Step 6: Output Token IDs
   Model picks one number (token ID) at a time
   from its guesses.

Step 7: Detokenization
   These output numbers are changed back into
   words using the same Vocabulary list, and shown
   to the user.
```

## Simple Summary
Tokenization works in this order:
**Text → Tokens → Token IDs → Embeddings (vectors) → Model → Output Token IDs → Text**

First the text is cut into small pieces, then each piece gets a number, then each number is turned into a meaning-vector for the model to use. The model gives out numbers one at a time, and those numbers are turned back into words for the user.

## Key Points to Remember
1. **Tokens are not always full words.** Easy words stay whole, but long or rare words get cut into smaller parts.
2. **It is called a Vocabulary, not a dictionary.** It is a fixed list made during training, with words, word-parts, and even single letters. It usually has 30,000 to 150,000 items.
3. **The model does not use the plain number directly.** Each number is first turned into a vector (meaning), and that vector goes into the Transformer.
4. **The output is not one fixed answer.** The model gives a list of guesses and picks one token at a time, again and again, until the full answer is ready.

## My Understanding
Tokenization is not just "cutting words and giving them numbers." It changes human language into numbers that also carry meaning, so the Transformer can understand the context and guess the next word correctly. Then it changes the numbers back into normal text for the user to read.


# What is Context Window (Short Note)

## Simple Meaning
Context window means how many **tokens** an LLM can handle at one time (input + output, both together).

## Lift Analogy
A lift has a fixed weight or people limit, no matter how that weight is made up. In the same way, a context window has a fixed token limit — input tokens, output tokens, and old messages all together must fit inside this one limit.

If the limit is crossed, just like extra people cannot get into a full lift, the model also drops old tokens (forgets them) so new tokens can fit.

## Key Points
1. Context window is measured in **tokens**, not words
2. It is not just input — input and output together make up the total limit
3. A bigger window means the model can remember a longer conversation, but it also needs more compute power



# Token Limit / Max Tokens (Short Note)

## Simple Meaning
Max tokens is a setting that controls how many tokens the model is allowed to use for one request. It can mean two things, so check the context:

1. **Max output tokens** — the most tokens the model is allowed to generate in its answer
2. **Max context length** — the total limit for input + output combined (this is the context window)

## Lift Analogy (continued)
Think of the lift again. The lift has a total capacity (context window). But you can also set a rule like "only 5 people can get out at this floor" — that rule is like **max output tokens**. It controls one part of the trip, not the whole lift capacity.

## Why It Matters
1. If max output tokens is set too low, the model's answer gets **cut off** in the middle
2. If input + output goes over the context window, older parts of the conversation get **dropped**
3. Setting a proper max tokens value helps control cost and response length, since longer output uses more tokens

## Key Points
1. Max tokens is a **setting**, the context window is a **fixed model limit**
2. You can set max output tokens lower than the context window, but never higher
3. Going over the limit does not crash the model — it either gets cut off or drops old data



