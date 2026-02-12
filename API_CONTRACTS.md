# AURA – API Contracts

## Create Workflow
POST /workflows

### Request
```json
{
  "name": "Refund Workflow",
  "definition": {
    "nodes": ["check_amount", "fraud_check"],
    "edges": []
  }
}
