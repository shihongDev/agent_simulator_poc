# Agent Testing

> Learn how Janus automatically tests your AI agents through conversation simulations

## How It Works

### 1. **Conversation Simulation**

Janus creates realistic conversation scenarios by simulating different user personas interacting with your agent:

```python  theme={null}
await janus.run_simulations(
    num_simulations=10,  # Run 10 different conversations
    max_turns=5,         # Each conversation has up to 5 turns
    target_agent=lambda: MyAgent().chat,
    api_key="your_janus_api_key"
)
```

### 2. **Diverse Personas**

Janus generates diverse user personas automatically based on your webapp template:

* **Demographics**: Age, income, gender, location
* **Behavioral traits**: Conversation intensity, patience, complaint propensity
* **Technical expertise**: Beginner to expert levels
* **Communication styles**: Formal, casual, urgent, relaxed

**Why this matters:** Real users aren't uniform. Testing with diverse personas catches edge cases that uniform test sets miss.

<Card title="Webapp Setup Guide" icon="book" href="/concepts/webapp-setup">
  Learn how to configure simulation templates and personas in the webapp
</Card>

### 3. **Systematic Testing**

Janus systematically tests your agent across multiple dimensions:

<CardGroup cols={2}>
  <Card title="Response Quality" icon="star">
    Evaluates helpfulness, accuracy, and relevance of responses
  </Card>

  <Card title="Policy Compliance" icon="shield">
    Checks adherence to safety guidelines and business rules
  </Card>

  <Card title="Context Awareness" icon="brain">
    Tests ability to maintain conversation context
  </Card>

  <Card title="Error Handling" icon="info">
    Identifies how agent handles edge cases and errors
  </Card>
</CardGroup>

## Testing Approaches

### Conversational Agent Testing

The traditional approach for testing AI agents through simulated conversations:

```python  theme={null}
class MyAgent:
    async def chat(self, prompt: str) -> str:
        # Your agent logic here
        return "Hello! I'm your AI assistant."

# Test through conversation simulation
results = await janus.run_simulations(
    num_simulations=10,
    max_turns=5,
    target_agent=lambda: MyAgent().chat,
    api_key="your_janus_api_key"
)
```

### External Workflow Testing

Test event-driven workflows, API integrations, and end-to-end business processes by simulating webhook triggers to external systems like N8N, Zapier, or custom APIs.

```python  theme={null}
# Test entire workflows by simulating webhook triggers:
target_agent = await create_webhook_target_agent(
    n8n_base_url="https://your-n8n-instance.com",
    api_key="your_api_key",
    workflow_id="your_workflow_id",
    payload={"case_id": "CASE-123", "priority": "High"}
)

results = await janus.run_simulations(
    num_simulations=5,
    max_turns=1,  # Single webhook trigger
    target_agent=target_agent,
    api_key="your_janus_api_key"
)
```

## Testing Workflow

### Step 1: Define Your Agent

Create an agent class with a `chat` method that Janus can test:

```python  theme={null}
class MyAgent:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    async def chat(self, prompt: str) -> str:
        """This method will be tested by Janus"""
        response = await self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
```

### Step 2: Configure Your Testing Environment (Webapp)

Before running simulations, you need to set up your testing environment in the Janus webapp:

1. **Create Test Cases**: Provide 5-10 examples of real test sets/queries. This will serve as the basis for creating the simulation runs.
2. **Set Up Rule Sets**: Configure evaluation criteria and compliance rules
3. **Create Simulation Templates**: Design personas and conversation parameters

<Card title="Webapp Setup Guide" icon="settings" href="/concepts/webapp-setup">
  Learn how to configure test cases, rules, and simulation templates
</Card>

### Step 3: Configure Test Parameters

Set up your testing configuration:

```python  theme={null}
# Basic testing
results = await janus.run_simulations(
    num_simulations=20,
    max_turns=8,
    target_agent=lambda: MyAgent().chat,
    api_key="your_janus_api_key"
)

# Advanced testing with custom context
results = await janus.run_simulations(
    num_simulations=50,
    max_turns=10,
    target_agent=lambda: MyAgent().chat,
    api_key="your_janus_api_key",
    context="You are a customer service representative testing a new AI assistant.",
    goal="Evaluate the AI assistant's ability to handle customer inquiries professionally."
)
```

### Step 4: Analyze Results

View comprehensive results in the Janus dashboard at [app.withjanus.com/dashboard/results](https://app.withjanus.com/dashboard/results):

* **Conversation Transcripts**: Full conversation flow with timestamps
* **Rule Violations**: Specific rules violated in each turn
* **RAG Hallucinations**: Claims that couldn't be verified against knowledge base
* **Investigation Results**: Autonomous judging and usefulness assessments
* **Performance Traces**: Technical execution details and metrics

<Card title="View Results" icon="chart-line" href="https://app.withjanus.com/dashboard/results">
  Check your simulation results in the Janus dashboard
</Card>

## Best Practices

<Tip>
  * Start with 10-20 simulations for initial testing
  * Increase simulation count for comprehensive evaluation
  * Use custom context to match your specific use case
  * Monitor results in the Janus dashboard for detailed insights
</Tip>

<Warning>
  Running many simulations can be resource-intensive. Monitor your API usage and system resources.
</Warning>

## Common Use Cases

### 1. **Replace Manual Test Case Creation**

**Traditional approach:** PMs spend 2-3 weeks writing test cases\
**Janus approach:** Upload 5 seed examples, auto-generate 10,000 realistic scenarios in hours

**How it works:**

* Provide 3-5 real conversation examples or test cases
* Janus automatically generates thousands of variations (different personas, intents, edge cases)
* Covers 80%+ of realistic user behaviors without manual annotation

**Result:** Comprehensive test coverage in hours instead of weeks

***

### 2. **Generate Fine-Tuning Data**

**Problem:** Need domain-specific training data for model improvement\
**Solution:** Every simulation run exports as RLHF-ready training data

**What you get:**

* Full conversation trajectories with reward signals
* Edge case examples for model improvement
* Ground truth labels for good/bad responses
* Domain-specific fine-tuning datasets

**Result:** Thousands of training examples without manual labeling. Your eval infrastructure doubles as a data generation engine.

***

### 3. **Continuous Regression Testing**

**Problem:** Agent improvements might break existing functionality\
**Solution:** Run simulations after every code change to catch regressions

**How it works:**

* Run 100+ simulations after each deployment
* Compare pass rates to baseline metrics
* Catch breaking changes before they reach production
* Integrate with CI/CD pipelines for automated testing

**Result:** Ship with confidence, knowing new changes don't break existing behavior

***

### 4. **Measure Qualitative Improvements**

**Problem:** Can't measure subjective KPIs like politeness, helpfulness, or satisfaction\
**Solution:** Calibrated judges that score qualitative metrics at scale

**What you can measure:**

* Empathy and professionalism in responses
* User satisfaction and resolution quality
* Appropriate handling of frustration or edge cases
* Brand voice and tone consistency

**Result:** Optimize for metrics that actually matter to users, not just task accuracy

***

### 5. **Test Event-Driven Workflows & API Integrations**

**Use case:** Validate webhook endpoints, N8N workflows, Zapier automations, or custom APIs\
**Solution:** Simulate webhook triggers and test end-to-end business processes

**What you can test:**

* Event-driven automation workflows (N8N, Zapier, Make)
* Third-party API integrations
* Webhook endpoint validation
* End-to-end business process flows

**Result:** Ensure external integrations work correctly before production deployment

## Example: Customer Service Testing

```python  theme={null}
# Test a customer service agent
results = await janus.run_simulations(
    num_simulations=30,
    max_turns=6,
    target_agent=lambda: CustomerServiceAgent().chat,
    api_key="your_janus_api_key",
    context="You are a customer testing a new AI customer service assistant.",
    goal="Test the AI assistant's ability to handle customer inquiries and resolve issues.",
    # Custom hardcoded rules for evaluation
    rules=[
        "The agent should be polite and professional",
        "The agent should provide accurate information",
        "The agent should escalate complex issues appropriately"
    ]
)
```

## Multimodal Agent Testing

For complex workflows that return structured data, files, or metadata, Janus supports multimodal agent testing:

```python  theme={null}
from janus_sdk import run_simulations, MultimodalOutput, FileAttachment

class WorkflowAgent:
    async def chat(self, prompt: str) -> MultimodalOutput:
        return MultimodalOutput(
            text="Workflow completed successfully",
            json_data={
                "case_id": "CASE-123",
                "status": "completed",
                "execution_time": 2.5
            },
            files=[
                FileAttachment(
                    name="report.pdf",
                    content=pdf_bytes,
                    mime_type="application/pdf",
                    size=len(pdf_bytes)
                )
            ],
            metadata={"api_calls": 8}
        )

# Test multimodal agent
results = await run_simulations(
    num_simulations=10,
    max_turns=1,
    target_agent=lambda: WorkflowAgent().chat,
    api_key="your_janus_api_key"
)
```

### Use Cases

* **N8N Workflows**: Test complex automation workflows with structured outputs
* **Document Generation**: Validate workflows that create PDFs, reports, or files
* **API Integrations**: Test agents that return structured data and metadata

## Next Steps

<CardGroup cols={2}>
  <Card title="Function Tracing" icon="route" href="/concepts/tracing">
    Learn how to trace function calls and tool usage
  </Card>

  <Card title="Evaluation Rules" icon="shield" href="/concepts/evaluation">
    Understand how rule-based evaluation works
  </Card>

  <Card title="Quickstart Guide" icon="rocket" href="/quickstart">
    Run your first agent test
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/run-simulations">
    Detailed API documentation
  </Card>
</CardGroup>
