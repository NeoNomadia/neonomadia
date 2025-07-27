# The Environment

The Environment is NeoNomadia’s data warehouse — hosting both structured and unstructured content, enriched with an interface to selected community contributions that can be used as supplementary facts and perspectives.

Like The Guide, this category evolves in multiple stages, gradually enabling the integration of moderated AI while preserving the possibility of fully manual interaction with the data.

## The Content Access Logic

Intelligent use of data depends on ensuring that each informational item — whether database entry, graphic, presentation, article, or document — is properly categorized, labeled, and contextually linked to dialog graph tokens. These associations are constructed from an arbitrary number of token groups, where each group may represent a single token or a structured collection.

This allows the system to process content access through a contextual chain, especially during early development stages:

~~~plaintext
[User Input]
 → [Language Tokens]
 → [Contextual Mapping Engine] 
 → [Dialog Graph Tokens] as Alternative Token Group Collection
 → [Content Identification Engine]
 → [Preformatted Content]
~~~

In its final development stage, The Environment introduces dynamic content generation:

~~~plaintext
[User Input]
 → [Language Tokens]
 → [Contextual Mapping Engine] 
 → [Dialog Graph Tokens] as Alternative Token Group Collection
 → [Content Identification Engine] 
 → [Content Generation Engine]
 → [Generated Content]
~~~

This architecture ensures that user inputs are interpreted contextually, matched meaningfully, and resolved into relevant knowledge — whether curated or composed. Structured information meets human intention, one token bridge at a time.

## Data Gathering Mechanisms

As with other components of the project, content gathering mechanisms are designed for natural growth. Each method represents an evolutionary pathway — not one replacing the other, but all existing in parallel to complement the system’s development.

So, the first question to be resolved is the one for the sources of information. For this project these are

- manual entry by information providers (manual categorization)
- usage of community posts and articles (scanned and auto-categorized)
- web crawling with AI agents (auto-detection of relevant content)
- interlinking with other systems and their already categorized content (open exchange API)

For all informational items there is one mandatory Token Group:

<ul>
  <li><strong>Geographical Context Token Group</strong>
    <ul>
      <li><strong>Country</strong> (mandatory)<br/>
        <i>defined by Country Name and international Country ISO Code</i>
      </li>
      <li><strong>Region</strong> (optional)<br/>
        <i>representing the most granular regional description, whether a state, city, or community</i>
      </li>
      <li><strong>Geographical Coordinates</strong> (mandatory)<br/>
        <i>defining the center point (best guess) of the defined region</i>
      </li>
    </ul>
  </li>
</ul>

The Geographical Context tokenization should be supported by a service that automatically resolves country and region names into geographical coordinates. Given the abundance of reliable public services, there is no need to implement a custom solution.

An optional but strongly recommended Token is the Expiration Token (This is not a real Dialog Graph Token but it uses the same logic after it is compared with the Current Timestamp token of the Dialog Graph):

<ul>
  <li><strong>Expiration Token Group</strong>
    <ul>
      <li><strong>Revalidate Until</strong> <i>YYYY-MM-DD (default 2999-12-31)</i></li>
      <li><strong>Revalidation Interval Days</strong> <i>(default 0)</i></li>
      <li><strong>Invalid From</strong> <i>YYYY-MM-DD (default 3000-01-01)</i></li>
    </ul>
  </li>
</ul>

If no Expiration Token Group is provided, the default values are applied to preserve system stability and temporal clarity.

### Manual Entry

The manual entry by **informantion providers** will be the starting point of the project. Due to its resource intensity, manual entry serves as the foundation of the project — essential for its launch, but not sufficient to sustain its growth. Nevertheless, it will remain one of the indispensable data import pathways, especially for information not accessible through the public web or in order to add some content immediately. It follows two parallel paths:

- **Dynamic Forms** enable the integration of multiple media types, with a primary focus on text. Information providers are responsible for categorizing and labeling entries. In the second development stage, they receive adaptive suggestions. Association with dialog graph tokens remains a manual and bi-directional process — if no appropriate tokens exist, providers can generate them, respecting category and label structures.
- **Linked Page Evaluation** allows providers to submit a single link for top-level analysis by the Content Extraction AI. At this stage, the AI operates in training mode. Like all NeoNomadia AI subprojects, it functions as a moderated system (see [The Moderated AI Concept](moderated-ai-concept.md)). Based on the page’s content diversity and density, the AI assembles one or more **pre-filled Dynamic Forms**, enriched with suggested categories, labels, and tokens. If these are inaccurate, incomplete, or misaligned, the provider edits the form(s) and saves the result via “Store expected result.” This action instructs the AI engine to refine its output iteratively until it reaches the expected form — without invalidating prior results.

The **information provider** is a defined user role, which is assigned to trustful users only. The **information provider** role might be given as global or country specific role.

### Community Posts and Articles

Beyond the standards of a Community section, like profiles, chats and direct contact, the NeoNomadia Community also provides the ability to create Posts (short statements) and Articles (long, comprehensive, topic-related content). These Posts and Articles will be one important base for the information store of the NeoNomadia project. After they have been validated against violations of the code of conduct, they will be parsed by the **Content Extraction AI** similar to the Linked Page Evaluation but with the fortune of possibly having some more context relations than on a single Web Page.

This process is started automatically, whenever a new Post or Article is added by using the NeoNomadia API.

According to the moderated AI concept it always generates exactly one **Dynamic Form** with the related categories, labels and tokens. The Content Extraction AI decides itself for completenes and correctness of the generated content cross-referencing against the NeoNomadia Category Catalog, Label Catalog, Dialog Graph Token Catalog and the Dialog Graph Catalog. If the confidentiality rate (AI confidence in classification accuracy) is below 99%, the Dynamic Form is scheduled to be picked up by an **information provider** to be checked and stored.

This links the Post or Article for the unstructured document store.

If the first scan resulted in multiple major categories, a second run extracts **multiple Dynamic Forms** with the related categories, labels and tokens. The further process is similar to the first scan with the difference, that the Dynamic Forms contain content extracts and not the full document, and a result is finally stored in the structured fact store. 

A further validation process for each informational item against internal information and public available information prevents from getting flooded with alternative facts and troll content. If this validation is not passed, the related Dynamic Form is always scheduled for a review, independent from the confidentiality rate.

