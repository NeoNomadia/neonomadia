# Derived Sub Projects

## The Semantical Syntactical Language Tokenizer

**Why yet another language tokenizer?**

The idea is that language tokenizers have the potential to offer much more than they currently do — especially when built to process multiple languages. There’s no compelling reason why semantic resolution and translation should be pushed downstream to the consuming systems. Instead, a modern tokenizer should be capable of handling these tasks natively.

This means enabling a truly **bidirectional solution**, one that not only tokenizes expressions across languages but also converts a universal token string back into localized phrases for any supported language. In doing so, LLMs and other consumers could operate on a single, shared token set, eliminating the need to retrain models for each specific language.

By abstracting syntax and semantics into a **universal token layer**, this tokenizer offers a bidirectional translation interface. It enables systems to operate meaningfully across languages using a unified token set — unlocking new efficiencies in LLM training, multilingual content moderation, and dialog modeling.

## The Technical Solution

The initial foundation for this tokenizer is built on the most widely accepted international language: English. Every known word is processed to generate one or more tokens — allowing for ambiguity resolution where necessary.

Each token is linked to the following semantic and structural attributes:

- Up to three **iconographic images**, in a standardized format of 32 × 32 px
- Up to three **emotional keywords** to represent connotative tone
- Up to five **contextual strong relations** that reflect dominant associations
- A **syntax definition**, derived from an expandable **Universal Syntax Dictionary** — covering elements like nouns, adjectives, verbs, tense, punctuation, proper names, and beyond

As a complementary system, a **Syntax Stream Dictionary** is established. This dictionary contains all feasible sentence constructs, with a stream length of up to 2000 syntax units — starting from minimal constructs like “noun + punctuation” and expanding in structural complexity.

Together, this tokenizer framework depends on five primary dictionaries:

- **Compound Word Dictionary**: Prevents separation of meaningful compound terms by whitespace
- **Iconographic Dictionary**: Connects tokens to visual symbols for rapid recognition
- **Emotion Dictionary**: Defines the emotional resonance of a token
- **Universal Syntax Dictionary**: Covers grammatical roles across supported languages
- **Syntax Stream Dictionary**: Models permissible sentence flows and sequencing patterns

Once this foundational structure is in place, a lightweight machine learning module handles real-time linguistic adjustment. This is crucial because most input — especially manual text — contains grammatical deviations or misspellings. During training mode, the system computes a best match and prompts the contributor for confirmation.

In live mode, the tokenizer evaluates incoming text based on its origin:

<ul>
  <li><strong>Manual input </strong>triggers the request interface, enabling clarification through contributor feedback, as long as the confidence rate does not fall below 80% (to prevent from spaming with unresolvable content)</li>
  <li><strong>Static text (from document parsing) </strong>proceeds via best-match heuristics
    <ul>
      <li>If the confidence rate falls below 98%, the processing halts. The text is stored in a dedicated resolution database for manual refinement, and a review token is issued to the consuming system. </li>
      <li>If the confidence rate falls below 80%, the tokenizer discards the input and returns an unresolvable token — usually indicating an unknown or unsupported language.</li>
    </ul>
  </li>
</ul>

The tokenizer operates through a five-step pipeline for robust multilingual and contextual parsing:

1. Full text matching against the compound word dictionary to detect the base language
2. Sentence parsing to detect the sentence language
3. Tokenization based on the sentence language
4. Full token stream parsing for detecting and coupling referencing tokens like personal pronouns
5. Full token stream parsing for token enrichment regarding additional token parameters and additional
   1. Term Tokens (e.g. temporal different terms in one sentence)
   2. Sentence Tokens (e.g. ethical/sensitive flags, itent classification, dedicated language switch)
   3. Paragraph Tokens (e.g. cultural context, dedicated language switch)
   4. Heading Content Token (e.g. base language)

|Attribute| Derived / Computed From|
|---------|------------------------|
|**Cultural Context**|Emotion keywords + contextual relations|


## How to train the system