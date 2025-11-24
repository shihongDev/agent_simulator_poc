# Webapp Setup

> Complete guide to configuring your testing environment in the Janus webapp

While the SDK handles programmatic execution, the webapp handles configuration, visualization, and analysis.

## SDK vs Webapp: When to Use Each

The Janus platform has two interfaces that work together:

<CardGroup cols={2}>
  <Card title="Python SDK" icon="code">
    **For engineers who want programmatic control**

    ✅ Run simulations from CI/CD\
    ✅ Integrate with existing architecture\
    ✅ Trace code within your IDE

    [View SDK Docs →](/quickstart)
  </Card>

  <Card title="Webapp (UI)" icon="browser">
    **For everyone who wants visual configuration**

    ✅ Create test sets and judging criteria\
    ✅ Configure simulation environments\
    ✅ View results and insights

    [Open Webapp →](https://app.withjanus.com)
  </Card>
</CardGroup>

***

## Overview

The webapp provides three main areas for configuration:

* **Test & Rules**: Define test cases, evaluation rules, and knowledge base
* **Templates**: Configure simulation templates and run simulations
* **Results**: Analyze performance and export data

## Test & Rules Configuration

### Test Cases

Navigate to **Test & Rules → Test Cases** to create and manage your test queries:

* **Create Test Cases**: Add specific queries (seed examples for simulations)
* **Set Context**: Provide background information and goals for each test case
* **Define Expectations**: Specify what constitutes a successful response
* **Organize by Category**: Group related test cases for better organization

**Example Test Case Structure:**

```
Query: "What are the side effects of medication X?"
Context: Healthcare scenario, patient asking about medication
Goal: Ensure agent provides accurate medical information
Category: Healthcare, Medication Safety
```

### Rule Sets

Go to **Test & Rules → Rule Sets** to define evaluation criteria:

* **Compliance Rules**: Ensure responses follow company policies
* **Quality Checks**: Validate response accuracy and completeness
* **Behavioral Constraints**: Set boundaries for agent behavior
* **Domain-Specific Rules**: Industry-specific requirements

**Common Rule Categories:**

* **Safety**: No medical advice, no harmful content
* **Accuracy**: Must cite sources, no hallucinations
* **Compliance**: Follow regulatory requirements
* **Tone**: Professional, helpful, appropriate

### Knowledge Base

Access **Test & Rules → Knowledge Base** to upload documents for hallucination detection:

* **Document Upload**: Support for PDF, DOCX, TXT, and other formats
* **RAG Hallucination Detection**: Automatically detect when agents make false claims
* **File Management**: Organize and manage uploaded documents
* **Status Tracking**: Monitor upload progress and processing status

**Supported File Types:**

* PDF documents
* Word documents (DOCX)
* Text files (TXT)
* Markdown files (MD)
* CSV files

## Simulation Configuration

### Templates

The **Templates** page is where you configure simulation parameters:

* **Create Templates**: Set up different simulation configurations
* **Configure Personas**: Define user characteristics and behaviors
* **Set Parameters**: Adjust simulation length, complexity, and goals
* **Star Templates**: Mark templates as active for testing

**Template Configuration Options:**

* **Test Cases**: Select specific test cases
* **Rule Sets**: Choose evaluation criteria for responses
* **User Personas**: Different personality types, knowledge levels
* **Demographics**: Age range (18-100), gender, race, residence area
* **Economic**: Annual income range ($0-$1M)
* **Psychological**: Personality types (MBTI), emotions, urgency levels
* **Communication**: Language proficiency, conversation intensity
* **Behavioral**: Patience level, complaint propensity
* **Occupation**: Custom occupation tags
* **Miscellaneous Notes**: Additional context or constraints
* **CSV Data Integration**: Upload user data for personalized simulations
* **Assignment Strategies**: Sequential, random, or round-robin user assignment
* **RAG Hallucination Judge**: Enable AI-powered factual accuracy verification

**CSV Requirements:**

* Must include a `user_id` column
* Each row becomes a unique synthetic user
* Supports custom fields for personalization

## Running Simulations

### From the SDK

Use the webapp configuration with your SDK code:

```python  theme={null}
await run_simulations(
    target_agent=lambda: MyAgent().chat,
    api_key=os.getenv("JANUS_API_KEY"),
    num_simulations=10,
    max_turns=5,
    # Webapp persona and context data
    persona_kwargs={
        "user_type": "technical_expert",
        "context": "software_development"
    }
)
```

## Results and Analysis

### Viewing Results

Navigate to **Results** to analyze your simulation outcomes:

* **Conversation Logs**: Full transcript of each simulation
* **Performance Metrics**: Response times, token usage, success rates
* **Rule Violations**: Instances where rules were broken
* **Tool Usage**: Detailed tracing of function calls and API usage
* **RAG Hallucinations**: Detected factual inaccuracies against knowledge base

**Available Analysis Tabs:**

* **Transcript**: Full conversation flow with metrics and function calls
* **Rules**: Individual rule violations with context
* **Overall**: Overall rule compliance assessment
* **Functions**: Detailed function call traces and performance
* **Hallucinations**: RAG accuracy verification results
* **Investigation**: Janus's intelligent third-party judging system that autonomously analyzes every simulation to identify potential issues, anomalies, and areas that warrant your attention - think of it as your AI-powered quality assurance team that never sleeps
* **Eval**: Evaluation comparisons (when available)
* **Identity**: User persona and backstory details used in simulation

## Exporting Data

Export simulation results for analysis, fine-tuning, or reporting.

### What You Can Export

**1. Evaluation Results (JSON)**:

* All conversations and turns
* Rule violations with context
* Hallucination detections
* Performance metrics
* Function traces

**Use for:**

* GPT clustering analysis (identify failure patterns)
* Custom analysis and monitoring
* Integration with existing tools

**How to export:**

1. Go to Results page
2. Click "Export" → "JSON"

***

**2. Training Data (RLHF Format)**:
Structured data for model fine-tuning

* Full conversation trajectories
* Reward signals (rule compliance scores)
* Positive/negative examples
* Ground truth labels

**Use for:**

* Fine-tuning your agent
* Training custom models
* RLHF post-training

***

**3. Compliance Reports**:
Structured data for reporting

* Rule violation summary
* Pass/fail rates
* Performance metrics
* Audit trail

**Use for:**

* Compliance documentation
* Stakeholder reporting
* Performance dashboards

**How to export:**

1. Go to Insights page
2. Select generate report and specified simulation
3. Click 'Run'

***

### Common Export Workflows

**Workflow 1: GPT Clustering**

1. Export failed simulations as JSON
2. Feed to GPT: "What patterns do you see?"
3. Create new rules based on patterns
4. Re-run simulations with new rules

**Workflow 2: Model Fine-Tuning**

1. Export successful simulations as RLHF
2. Use as training data
3. Fine-tune model on domain-specific examples
4. Test improved model with new simulations

**Workflow 3: Compliance Reporting**

1. Export all simulations as CSV
2. Generate monthly compliance report
3. Track improvement over time
4. Share with stakeholders

## Insights and Reporting

### AI Performance Reports

The **Insights** page provides:

* **Report Generation**: Comprehensive reports of agent behavior
* **Issue Clustering**: Groups similar problems for easier resolution
* **Recommendations**: Actionable suggestions for improvement
* **Progress Tracking**: Monitor resolved issues over time
* **Trend Analysis**: Track performance over multiple test runs

## Best Practices

### Configuration Strategy

* **Start Simple**: Begin with basic test cases and rules
* **Iterate Gradually**: Add complexity as you understand your needs
* **Document Everything**: Keep clear records of your configuration
* **Regular Reviews**: Periodically assess and update your setup

### Testing Workflow

1. **Configure**: Set up test cases, rules, and knowledge base in the webapp
2. **Develop**: Build and test your agent with the SDK
3. **Run**: Execute simulations using webapp templates
4. **Analyze**: Review results and identify improvements
5. **Iterate**: Refine your agent and configuration

### Getting Help

* **Documentation**: Review this guide and related tutorials
* **Support**: Contact [team@withjanus.com](mailto:team@withjanus.com) for assistance
