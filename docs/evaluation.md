# Evaluation & Judging

> Learn how Janus evaluates AI agent performance using rule-based judging and hallucination detection

## How Janus Evaluates Agents

Janus provides three layers of evaluation:

<CardGroup cols={3}>
  <Card title="Custom Rules" icon="list-check">
    Define domain-specific requirements ("Must confirm changes", "Response time \< 2s")
  </Card>

  <Card title="Autonomous Judging" icon="magnifying-glass">
    AI-powered analysis finds issues you didn't think to check for
  </Card>

  <Card title="Hallucination Detection" icon="shield-check">
    Validate agent claims against your knowledge base documents
  </Card>
</CardGroup>

**Why three layers:** Custom rules catch known issues. Autonomous judging finds unknown issues. Hallucination detection ensures factual accuracy.

## How Evaluation Works

### 1. **Custom Rules**

Define rules that capture both quantitative and qualitative requirements. You can configure rules in the Janus webapp or pass them directly in the SDK:

**Qualitative (Subjective Metrics):**

```python  theme={null}
qualitative_rules = [
    "Agent should be empathetic and professional",
    "Agent should provide satisfying resolutions",
    "Agent should handle frustration gracefully",
    "Response should feel complete and helpful"
]
```

**Quantitative (Objective Metrics):**

```python  theme={null}
quantitative_rules = [
    "Response time must be under 2 seconds",
    "Must not exceed 500 tokens per response",
    "Must call verify_identity() before account changes",
]
```

**Domain-Specific (Compliance):**

```python  theme={null}
compliance_rules = [
    "Must confirm price changes before applying",
    "Must not provide medical diagnoses",
    "Must include legal disclaimers for financial advice",
    "Must not share personal user information"
]
```

### 2. **Autonomous Investigation**

Don't know what to test for? Janus runs a third-party proprietary judging system that evaluates agent responses for:

* **Usefulness**: How helpful and relevant the response is
* **Accuracy**: Whether the information provided is correct
* **Appropriateness**: Whether the response fits the context
* **Safety**: Whether the response follows safety guidelines

This judging system allows you to not need to put any rules if you don't know what to test - Janus verifies autonomously. Simply run simulations without specifying rules and our system will automatically evaluate agent performance.

**How it works:**

* Runs automatically on every simulation (no setup required)
* Filters to "useful" issues only (reduces false positives)
* Organized by turn with full context
* Provides reasoning for each issue

**Example investigation result:**

```
Turn 5: Issue detected
Category: Unhelpful
Issue: "Agent acknowledged the request but didn't provide the requested menu prices"
Usefulness: High
Context: User asked "Show me all burger prices" but agent only said "I can help with that"
```

<Note>
  **Pro tip:** Use autonomous investigation to discover new rules. When you see repeated patterns, convert them into explicit rules.
</Note>

### 3. **Hallucination Detection**

Detect when agents make claims that can't be verified by uploading your documents to the Janus webapp. In the dashboard at [app.withjanus.com](https://app.withjanus.com), you can upload whatever documents you want to test against, and the RAG hallucination detection will automatically verify agent claims against your knowledge base.

## Evaluation Components

### **Turn-Level Rules**

Rules that apply to each individual response:

<CardGroup cols={2}>
  <Card title="Content Rules" icon="file">
    * Accuracy of information
    * Completeness of responses
    * Relevance to the question
  </Card>

  <Card title="Behavior Rules" icon="user">
    * Politeness and professionalism
    * Helpfulness and engagement
    * Appropriate tone and style
  </Card>

  <Card title="Safety Rules" icon="shield">
    * No harmful advice
    * No personal information sharing
    * Compliance with guidelines
  </Card>

  <Card title="Context Rules" icon="brain">
    * Staying on topic
    * Maintaining conversation flow
    * Appropriate level of detail
  </Card>
</CardGroup>

## Integration with Janus Platform

### **Frontend Rule Configuration**

Through the Janus dashboard at [app.withjanus.com](https://app.withjanus.com), you can:

1. **Create Rule Sets**: Define comprehensive evaluation criteria
   * Write individual rules for each conversation turn
   * Define overall conversation rules

2. **Upload Knowledge Base**: Enable RAG hallucination detection
   * Upload documents that agents should reference
   * Configure RAG hallucination judge to detect unsupported claims

3. **Test Case Management**: Create structured evaluation scenarios
   * Define test case content and context
   * Upload evaluation datasets for comparison testing

## Evaluation Metrics

### **Rule Violations**

Rules are evaluated as binary violations - either violated or not:

* **Violation Count**: Number of times each rule was broken
* **Context**: The question and answer that triggered the violation
* **Explanation**: Detailed description of why the rule was violated
* **Turn Number**: Which conversation turn contained the violation

### **RAG Hallucination Detection**

Sophisticated scoring through confidence levels and claim verification:

* **Confidence Score**: 0-100% based on AI analysis certainty
* **Claims Checked**: Total number of factual claims analyzed
* **Claims Flagged**: Number of claims identified as potential hallucinations
* **Source Verification**: Claims checked against uploaded knowledge base documents

### **Overall Conversation Rules**

Binary assessment for conversation-wide patterns:

* **Conversation-wide Violations**: Rules that apply to the entire conversation flow
* **Pattern Analysis**: Consistency and structural rule violations
* **Flow Assessment**: Overall conversation quality and adherence

## Best Practices

**Be specific and measurable:**

* ✅ "Response time must be under 2 seconds"
* ❌ "Must respond quickly"

**When to reference specific functions:**

* ✅ Use function names when enforcing critical operations: "Must call verify\_identity() before account changes"
* ❌ "Call identity function call before changing account details"

**Use positive framing:**

* ✅ "Agent should provide helpful explanations"
* ❌ "Agent should not be unhelpful"

**Start critical, expand gradually:**

* Start with 5-10 most important rules
* Add more based on observed failures
* Remove rules that cause false positives

<Warning>
  Rules should be clear and unambiguous. Vague rules may lead to inconsistent evaluation results.
</Warning>
