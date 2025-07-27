# The Guide

The Guide serves as the user's navigator through NeoNomadia’s ever-growing information universe. At the core of the project lies a commitment: users should not be left to crawl helplessly through vast amounts of structured — and sometimes unstructured — data. The Guide empowers individuals to discover what they truly need, and how the system can support them.

The implementation unfolds in three progressive stages:

## The guided dialog system

This system offers a structured pathway through the API. Beginning with basic prompts like “What is your name?” or “Where are you now?”, it guides users through a conversational questionnaire designed to uncover their current needs and interests. Each interaction is tokenized and saved as a dialog graph, enabling the user to step backward or forward through their conversation history.

Dialog graphs are stored in relation to either the session or the user, depending on whether temporary or persistent storage has been selected. When a dialog graph appears for the first time, it is stored (anonymized) in a central graph database — ensuring that future conversations can benefit from accelerated suggestions and contextual awareness.

This first stage serves two purposes: to deliver an early MVP and to lay the foundation for Stage Two — the free chat system.

## The free chat system

The second stage introduces open text input. Users can simply write, and the system tokenizes the input in relation to the guided dialog graph from Stage One. Missing information can be requested, context gaps filled, and guided refinement encouraged. This architecture minimizes computational effort, limits confidentiality risks, and prevents out-of-scope usage.

Unlike a general-purpose AI system, the free chat interface is intentionally limited: it will not provide investment advice, explain unrelated scientific concepts, or locate car dealerships. Instead, its responses remain anchored to NeoNomadia’s vision. Dialog graphs are stored (when permitted) to preserve context, enable navigation, and support comparison across user journeys.

The system is also designed to learn. If the free chat generates new branches or identifies missing paths, these will be incorporated into the system’s graph database — allowing Stage One and Stage Two to enrich each other dynamically.

## The free speech system

The final stage introduces voice-based interaction. This requires careful attention to data economy, particularly in mobile contexts. One option is to provide basic speech-to-text and text-to-speech support for mobile app developers, while continuing to operate primarily on tokenized text.

Functionally, the voice system mirrors the free chat system — offering conversational access while retaining security, scalability, and contextual integrity.

## Specific challenges

**Multilingual support** will be implemented incrementally. English will be the default language, followed by major Latin-script languages, and then expanded to more complex linguistic structures — beginning with Cyrillic-based languages due to similar syntactic characteristics. Language support is shaped by Noto Sans (covering ~100 languages) and UTF-16 encoding for web compatibility.

The creation of a new, dedicated tokenizer would offer significant advantages: attaching graphical symbols to tokens as well as emotional categorizations, waveform examples for dialects, improved semantic typing, and advanced lookahead/lookback capabilities for contextual disambiguation. Such tools would improve both the guided dialog and translation functionality — but building this is a major subproject.

Until then, the translation layer must rely on publicly available LLMs to support multilingual access to data from The Environment and The Community APIs.

**@Contributors:** Interest in building or supporting this subproject is warmly welcomed.
